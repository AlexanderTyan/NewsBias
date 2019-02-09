"""

"""
__author__ = 'Alexander Tyan'
__version__ = 0.1

import datetime
from dateutil.parser import parse  # To parse date strings
# Works better than Python's native multiprocessing for Class methods:
import multiprocess
import csv
import feedparser as fp  # To parse RSS syntax
from newspaper import Source  # To build newspaper objects manually
from newspaper import news_pool  # To multithread the download of articles
from newspaper import Article
import re

import gensim
import spacy

# Constant for keys of info we retain from RSS feeds:
KEYS_TO_KEEP = ['title', 'link', 'id', 'published', 'published_parsed',
                'feedburner_origlink']


def download_rss_entries(rss_link):
    """
    TODO: add description
    :param rss_link: string, rss link URL
    :return all_entries: list of dictionaries, rss entries
    """
    rss = fp.parse(rss_link)
    all_entries = rss['entries']

    return all_entries


def try_rss_key(key_to_try, rss_entry_dict):
    """
    Try and return a key from an rss dictionary.
    :param key_to_try: str, key to search for in the rss dictionary
    :param rss_entry_dict: dict with rss entries keys
    :return: ret_tuple: tuple of key with 'rss_' prepend and value
    """
    try:
        return_val = rss_entry_dict[key_to_try]
    except KeyError:
        return_val = 'NotFound'

    ret_tuple = 'rss_' + key_to_try, return_val

    return ret_tuple


def parse_one_rss_entry(rss_entry_dict, keys_to_keep=KEYS_TO_KEEP):
    """
    Extract useful fields from an RSS entry.
    :param rss_entry_dict: dictionary, represents an RSS entry
    :param keys_to_keep: list of strings of what keys we are interested in 
        the rss feed
    :return rv_dict: dictionary of useful fields (str) and their values (str)
    """
    rv_dict = {}

    for key in keys_to_keep:
        new_key, val = try_rss_key(key_to_try=key,
                                   rss_entry_dict=rss_entry_dict)
        rv_dict[new_key] = val

    return rv_dict


def build_source(rss_entries, source_head_url, news_source_name,
                 rss_feed_name, rss_feed_url, feed_python_title):
    """
    Build newspaper source object and force articles based on rss
        into it manually (to use multithreading later)
    :param rss_entries: dict of rss entries, key is str title, value is str url
    :param source_head_url: string, e.g. 'https://www.rt.com/'
    :param news_source_name: string, e.g. 'RT'
    :param rss_feed_name: str, name of the rss feed, e.g. 'Top Stories'
    :param rss_feed_url: str, url of the rs feed, e.g.
        'http://rss.cnn.com/rss/cnn_topstories.rss'
    :param feed_python_title: str, programmatic name for the feed,
        e.g. 'cnn_politics'
    :return paper: a newspaper Source object
    """
    # Initialize Source objects, representing newspapers:
    paper = Source(rss_feed_url, memoize_articles=False)
    paper.build()
    # Do custom description:
    paper.description = feed_python_title

    # Build article list:
    articles = []
    for entry in rss_entries:

        # Extract RSS metadata:
        rss_metadata = parse_one_rss_entry(entry)
        # Add more metadata to it, for future records:
        rss_metadata['rss_feed_name'] = rss_feed_name
        rss_metadata['rss_feed_url'] = rss_feed_url
        rss_metadata['news_source_name'] = news_source_name

        article = Article(url=rss_metadata['rss_id'],
                          source_url=source_head_url)

        # Store clean rss data into the Article object:
        article.additional_data = rss_metadata
        # Accumulate articles:
        articles.append(article)

    # Force own articles into the paper object
    # (for multithread download later):
    paper.articles = articles

    return paper


def art_multithread_downloads(papers, threads_per_source):
    """
    Multithread download two papers' article downloads
    :param papers: list of newspaper Source objects, one per paper
    :param threads_per_source: int, threads per source, too many can result
        in getting blocked by the newspaper server
    :return: Mutate Source objects to download the papers
    """
    news_pool.set(papers, threads_per_source=threads_per_source)
    news_pool.join()


def multiprocess_article_downloads(many_papers_list):
    """
    Given a list of lists of newspaper objects, parallelize article downloads
        on the upper list level (i.e. multiprocess lists)
    :param many_papers_list: list of lists of newspaper objects
    :return None: multiprocess downloads
    """
    # Multiprocess parsing:
    processes = []
    for paper_list in many_papers_list:
        p = multiprocess.Process(target=art_multithread_downloads,
                                 args=(paper_list, 2))  # 2 threads per source
        processes.append(p)
        p.start()
    for process in processes:
        process.join()


def compile_papers(rss_feeds_dict):
    """
    TODO: elaborate on the format of rss_feeds_dict
    :param rss_feeds_dict: dict of string with rss feed links and other metadata
    :return papers: list of paper objects
    """
    # Get the RSS data:
    news_source_name = rss_feeds_dict['news_source_name']
    source_head_url = rss_feeds_dict['source_head_url']
    rss_feeds = rss_feeds_dict['rss_feeds']
    papers = []
    for a_feed in rss_feeds:
        feed_python_title = a_feed['feed_python_title']
        feed_site_title = a_feed['feed_site_title']
        feed_rss_link = a_feed['feed_rss_link']
        rss_entries = download_rss_entries(feed_rss_link)
        a_paper = build_source(rss_entries=rss_entries,
                               source_head_url=source_head_url,
                               news_source_name=news_source_name,
                               rss_feed_name=feed_site_title,
                               rss_feed_url=feed_rss_link,
                               feed_python_title=feed_python_title)
        papers.append(a_paper)

    return papers


def parse_paper_articles(newspaper_obj):
    """
    Given a newspaper object, parse all of its articles sequentially.
    :param newspaper_obj: newspaper object with articles already downloaded
    :return: None, just calls parse() on every article.
    """
    for article in newspaper_obj.articles:
        article.parse()


def multiprocess_parsing_paper_articles(papers_list):
    """
    Multiprocess parsing articles associated with each newspaper object in
        the papers_list. Parsing of articles withing each newspaper is
        sequential, but staring the parsing for each newspaper is parallel.
    :param papers_list: list of newspaper objects
    :return None:
    """
    # Multiprocess parsing:
    processes = []
    for paper in papers_list:
        p = multiprocess.Process(target=parse_paper_articles,
                                 args=(paper,))
        processes.append(p)
        p.start()
    for process in processes:
        process.join()


def conform_art_attrib(article_obj):
    """
    Fill attributes of an Article object the newspaper parser failed
    to fill
    :param article_obj: newspaper Article class object
    :return: mutate the attributes of the article object
    """
    rss_article_data = article_obj.additional_data
    # If an attribute is missing, try to fill out from our rss metadata:
    if (not article_obj.url) and (rss_article_data["rss_url"]):
        article_obj.url = rss_article_data["rss_url"]
    if (not article_obj.title) and (rss_article_data["rss_title"]):
        article_obj.title = rss_article_data["rss_title"]
    # if (not article.tags) and ("tags" in manual_metadata):
    #     article.tags = set(manual_metadata["tags"])
    # if (not article_obj.authors) and ("authors" in manual_metadata):
    #     article.authors.append(manual_metadata["authors"])
    if (not article_obj.publish_date) and (rss_article_data["rss_date"]):
        article_obj.publish_date = rss_article_data["rss_date"]
        # Try to convert the string date to a datetime.datetime format:
        try:
            article_obj.publish_date = parse(article_obj.publish_date)
        except:
            pass

    # Conform the text (i.e. remove meaningless lines like, "like our video"):
    #article_obj.text = clean_text_string(article_obj.text)


def write_out_articles(newspaper_obj, filepath, writeout_type='conventional'):
    """
    TODO: finish this docstring
    :param newspaper_obj:
    :param filepath: str, filepath, WITHOUT the filename
    :param writeout_type: str, 'custom' or 'conventional'
    :return:
    """
    now = datetime.datetime.now()
    current_date = '{}_{}_{}'.format(str(now.year),
                                     str(now.month),
                                     str(now.day))
    if writeout_type == 'custom':
        csv_name = filepath + current_date + '_' + newspaper_obj.description \
                   + '.csv'
    else:
        csv_name = filepath + current_date + '_' + newspaper_obj.brand + '.csv'
    with open(csv_name, 'w', encoding='utf-8') as outcsv:
        writer = csv.writer(outcsv)
        if writeout_type == 'conventional':
            header = ['source_url', 'url', 'title', 'movies', 'text',
                      'keywords', 'meta_keywords', 'tags', 'authors',
                      'publish_date', 'summary', 'html', 'article_html',
                      'meta_description', 'meta_data', 'canonical_link']
        else:
            header = ['source_url', 'url', 'title', 'movies', 'text',
                             'keywords', 'meta_keywords', 'tags', 'authors',
                             'publish_date', 'summary', 'html', 'article_html',
                             'meta_description', 'meta_data', 'canonical_link',
                             'rss_title', 'rss_link', 'rss_id', 'rss_published',
                             'rss_published_parsed', 'rss_feedburner_origlink',
                             'paper_section_name']
        writer.writerow(header)
        for article in newspaper_obj.articles:
            source_url = article.source_url
            url = article.url
            title = article.title
            movies = article.movies
            text = article.text
            keywords = article.keywords
            meta_keywords = article.meta_keywords
            tags = article.tags
            authors = article.authors
            publish_date = article.publish_date
            summary = article.summary
            html = article.html
            article_html = article.article_html
            meta_description = article.meta_description
            meta_data = article.meta_data
            canonical_link = article.canonical_link
            if writeout_type == 'custom':
                rss_title = article.additional_data['rss_title']
                rss_link = article.additional_data['rss_link']
                rss_id = article.additional_data['rss_id']
                rss_published = article.additional_data['rss_published']
                rss_published_parsed = \
                    article.additional_data['rss_published_parsed']
                rss_feedburner_origlink = \
                    article.additional_data['rss_feedburner_origlink']
                data_row = [source_url, url, title, movies, text, keywords,
                            meta_keywords, tags, authors, publish_date,
                            summary, html, article_html, meta_description,
                            meta_data, canonical_link, rss_title, rss_link,
                            rss_id, rss_published, rss_published_parsed,
                            rss_feedburner_origlink,
                            newspaper_obj.description]
            else:
                data_row = [source_url, url, title, movies, text, keywords,
                            meta_keywords, tags, authors, publish_date,
                            summary, html, article_html, meta_description,
                            meta_data, canonical_link]
            writer.writerow(data_row)


def clean_text_string(string, keep_dbl_newline=False):
    """
    Remove non-meaningful text in a string
    :param string: string, represents text
    :return clean_str: string, cleaned text
    """
    clean_str = re.sub(r"\nIf you like this story, share it with a friend!",
                       "", string, flags=re.IGNORECASE)
    clean_str = re.sub(r"\nLike this story\? Share it with a friend!",
                       "", clean_str, flags=re.IGNORECASE)
    clean_str = re.sub(r'\nREAD MORE: .*\n', '', clean_str, flags=re.IGNORECASE)
    clean_str = re.sub(r'\nREAD MORE\n', '', clean_str, flags=re.IGNORECASE)
    clean_str = re.sub(r"Media playback is unsupported on your device ",
                       "", clean_str, flags=re.IGNORECASE)
    clean_str = re.sub(r"Media caption ", "", clean_str, flags=re.IGNORECASE)
    clean_str = re.sub(r"Media playback is not supported on this device ", "", clean_str, flags=re.IGNORECASE)
    clean_str = re.sub(r"bbc radio live", "", clean_str, flags=re.IGNORECASE)
    clean_str = re.sub(r"bbc sport website", "", clean_str, flags=re.IGNORECASE)

    # A lot of topics have "say" in them, but that does not seem very meaningful,
    # so drop it:
    #clean_str = re.sub(r"say", "", clean_str, flags=re.IGNORECASE)
    #clean_str = re.sub(r"says", "", clean_str, flags=re.IGNORECASE)
    #clean_str = re.sub(r"said", "", clean_str, flags=re.IGNORECASE)

    # Artifact of web page news:
    clean_str = re.sub(r"image caption", "", clean_str, flags=re.IGNORECASE)
    clean_str = re.sub(r"video", "", clean_str, flags=re.IGNORECASE)

    if keep_dbl_newline:
        # Replace newlines not followed by another newline:
        clean_str = re.sub(r"\n(?!\n)", "", clean_str)
    else:
        clean_str = re.sub(r"\n\n", " ", clean_str)
        clean_str = re.sub(r"\n", "", clean_str)

    return clean_str


# From: https://www.machinelearningplus.com/nlp/topic-modeling-python-sklearn-examples/
def sent_to_words(sentences):
    for sentence in sentences:
        yield(gensim.utils.simple_preprocess(str(sentence),
                                             deacc=True))  # deacc=True removes punctuations


def lemmatization(texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
    """https://spacy.io/api/annotation"""

    # Initialize spacy 'en' model, keeping only tagger component (for efficiency)
    # Run in terminal: python3 -m spacy download en
    nlp = spacy.load('en', disable=['parser', 'ner'])

    texts_out = []
    for sent in texts:
        doc = nlp(" ".join(sent))
        texts_out.append(" ".join([token.lemma_ if token.lemma_ not in ['-PRON-']
                                   else '' for token in doc if token.pos_ in
                                   allowed_postags]))
    return texts_out

