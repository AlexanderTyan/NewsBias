"""
Package initialization.
"""

from .cnn_rss_links import CNN_LINKS_DICT
from .rt_rss_links import RT_LINKS_DICT
from .fox_rss_links import FOX_LINKS_DICT
from .bbc_rss_links import BBC_LINKS_DICT

from .functions import download_rss_entries, \
                       try_rss_key, \
                       parse_one_rss_entry, \
                       build_source, \
                       art_multithread_downloads, \
                       compile_papers, \
                       write_out_articles, \
                       parse_paper_articles, \
                       multiprocess_article_downloads, \
                       sent_to_words, \
                       clean_text_string
