"""

"""
__author__ = 'Alexander Tyan'
__version__ = 0.1

from dateutil.parser import parse  # To parse date strings
import csv
import feedparser as fp  # To parse RSS syntax
from newspaper import Source  # To build newspaper objects manually
from newspaper import news_pool  # To multithread the download of articles
from newspaper import Article

# Constant for keys of info we retain from RSS feeds:
KEYS_TO_KEEP = ['title', 'link', 'id', 'published', 'published_parsed',
                'feedburner_origlink']


def download_rss_entries(rss_link):
    """
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
                 rss_feed_name, rss_feed_url):
    """
    Build newspaper source object and force articles based on rss
        into it manually (to use multithreading later)
    :param rss_entries: dict of rss entries, key is str title, value is str url
    :param source_head_url: string, e.g. 'https://www.rt.com/'
    :param news_source_name: string, e.g. 'RT'
    :param rss_feed_name: str, name of the rss feed, e.g. 'Top Stories'
    :param rss_feed_url: str, url of the rs feed, e.g.
        'http://rss.cnn.com/rss/cnn_topstories.rss'
    :return paper: a newspaper Source object
    """
    # Initialize Source objects, representing newspapers:
    paper = Source(rss_feed_url, memoize_articles=False)
    paper.build()
    # Do custom description:
    paper.description = news_source_name + ' ' + rss_feed_name

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
    for a_feed in rss_feeds.items():
        rss_feed_name, rss_feed_url = a_feed
        rss_entries = download_rss_entries(rss_feed_url)
        a_paper = build_source(rss_entries=rss_entries,
                               source_head_url=source_head_url,
                               news_source_name=news_source_name,
                               rss_feed_name=rss_feed_name,
                               rss_feed_url=rss_feed_url)
        papers.append(a_paper)

    return papers


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


def write_out_articles(csv_output, newspaper_obj):
    """

    :param csv_output:
    :param newspaper_obj:
    :return:
    """
    with open(csv_output, 'w') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(['source_url', 'url', 'title', 'movies', 'text',
                         'keywords', 'meta_keywords', 'tags', 'authors',
                         'publish_date', 'summary', 'html', 'article_html',
                         'meta_description', 'meta_data', 'canonical_link',
                         'rss_title', 'rss_link', 'rss_id', 'rss_published',
                         'rss_published_parsed', 'rss_feedburner_origlink'])
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
            rss_title = article.additional_data['rss_title']
            rss_link = article.additional_data['rss_link']
            rss_id = article.additional_data['rss_id']
            rss_published = article.additional_data['rss_published']
            rss_published_parsed = \
                article.additional_data['rss_published_parsed']
            rss_feedburner_origlink = \
                article.additional_data['rss_feedburner_origlink']

            writer.writerow([source_url, url, title, movies, text, keywords,
                             meta_keywords, tags, authors, publish_date,
                             summary, html, article_html, meta_description,
                             meta_data, canonical_link, rss_title, rss_link,
                             rss_id, rss_published, rss_published_parsed,
                             rss_feedburner_origlink])
