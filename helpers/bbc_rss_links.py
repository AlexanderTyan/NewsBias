"""

Dictionary containing all links from CNN as values and string descriptors as
keys.
"""

BBC_LINKS_DICT = {'news_source_name': 'BBC News',
                  'source_head_url': 'https://www.bbc.com/news',
                  'rss_feeds':
                      [
                          {'feed_python_title': 'bbc_news_home',
                           'feed_site_title': 'Home',
                           'feed_rss_link':
                               'http://feeds.bbci.co.uk/news/rss.xml'},
                          {'feed_python_title': 'bbc_news_world',
                           'feed_site_title': 'World',
                           'feed_rss_link':
                               'http://feeds.bbci.co.uk/news/world/rss.xml'},
                          {'feed_python_title': 'bbc_news_us_and_canada',
                           'feed_site_title': 'US and Canada',
                           'feed_rss_link':
                               'http://feeds.bbci.co.uk/news/world/us_and_canada/rss.xml'},
                          {'feed_python_title': 'bbc_news_uk',
                           'feed_site_title': 'UK',
                           'feed_rss_link':
                               'http://feeds.bbci.co.uk/news/uk/rss.xml'},
                          {'feed_python_title': 'bbc_news_business',
                           'feed_site_title': 'Business',
                           'feed_rss_link':
                               'http://feeds.bbci.co.uk/news/business/rss.xml'},
                          {'feed_python_title': 'bbc_news_technology',
                           'feed_site_title': 'Technology',
                           'feed_rss_link':
                               'http://feeds.bbci.co.uk/news/technology/rss.xml'},
                          {'feed_python_title':
                               'bbc_news_science_and_environment',
                           'feed_site_title': 'Science and Environment',
                           'feed_rss_link':
                               'http://feeds.bbci.co.uk/news/science_and_environment/rss.xml'},
                          {'feed_python_title':
                               'bbc_news_entertainment_and_arts',
                           'feed_site_title': 'Entertainment and Arts',
                           'feed_rss_link':
                               'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml'},
                          {'feed_python_title': 'bbc_news_health',
                           'feed_site_title': 'Health',
                           'feed_rss_link':
                               'http://feeds.bbci.co.uk/news/health/rss.xml'}
                      ]
                  }

# For omitted RSS feed links:
BBC_OMITTED_LINKS_DICT = {'Opinion': 'http://feeds.foxnews.com/foxnews/opinion',
                          'Video': 'https://feeds.foxnews.com/foxnews/video'
                          }

