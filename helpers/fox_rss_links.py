"""

Dictionary containing all links from CNN as values and string descriptors as
keys.
"""

FOX_LINKS_DICT = {'news_source_name': 'Fox News',
                  'source_head_url': 'http://www.foxnews.com/',
                  'rss_feeds':
                      [
                          {'feed_python_title': 'fox_latest_headlines',
                           'feed_site_title': 'Latest Headlines',
                           'feed_rss_link':
                               'http://www.feeds.foxnews.com/foxnews/latest'},
                          {'feed_python_title': 'fox_most_popular',
                           'feed_site_title': 'Most Popular',
                           'feed_rss_link':
                               'http://feeds.foxnews.com/foxnews/most-popular'},
                          {'feed_python_title': 'fox_entertainment',
                           'feed_site_title': 'Entertainment',
                           'feed_rss_link':
                               'http://feeds.foxnews.com/foxnews/entertainment'},
                          {'feed_python_title': 'fox_health',
                           'feed_site_title': 'Health',
                           'feed_rss_link': 'http://feeds.foxnews.com/foxnews/health'},
                          {'feed_python_title': 'fox_lifestyle',
                           'feed_site_title': 'Lifestyle',
                           'feed_rss_link': 'http://feeds.foxnews.com/foxnews/section/lifestyle'},
                          {'feed_python_title': 'fox_politics',
                           'feed_site_title': 'Politics',
                           'feed_rss_link': 'http://feeds.foxnews.com/foxnews/politics'},
                          {'feed_python_title': 'fox_science',
                           'feed_site_title': 'Science',
                           'feed_rss_link': 'http://feeds.foxnews.com/foxnews/science'},
                          {'feed_python_title': 'fox_sports',
                           'feed_site_title': 'Sports',
                           'feed_rss_link': 'http://feeds.foxnews.com/foxnews/sports'},
                          {'feed_python_title': 'fox_tech',
                           'feed_site_title': 'Tech',
                           'feed_rss_link': 'http://feeds.foxnews.com/foxnews/tech'},
                          {'feed_python_title': 'fox_us',
                           'feed_site_title': 'U.S.',
                           'feed_rss_link': 'http://feeds.foxnews.com/foxnews/national'},
                          {'feed_python_title': 'fox_world',
                           'feed_site_title': 'World',
                           'feed_rss_link': 'http://feeds.foxnews.com/foxnews/world'}
                      ]
                  }

# For omitted RSS feed links:
FOX_OMITTED_LINKS_DICT = {'Opinion': 'http://feeds.foxnews.com/foxnews/opinion',
                         'Video': 'https://feeds.foxnews.com/foxnews/video',
                         'Travel':
                             'http://feeds.foxnews.com/foxnews/internal/travel/mixed'}
