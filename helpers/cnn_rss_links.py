"""

Dictionary containing all links from CNN as values and string descriptors as
keys.
"""

CNN_LINKS_DICT = {'news_source_name': 'CNN',
                  'source_head_url': 'https://www.cnn.com/',
                  'rss_feeds':
                      {'Top Stories':
                          'http://rss.cnn.com/rss/cnn_topstories.rss',
                       'World': 'http://rss.cnn.com/rss/cnn_world.rss',
                       'U.S.': 'http://rss.cnn.com/rss/cnn_us.rss',
                       'Business (CNNMoney.com)':
                          'http://rss.cnn.com/rss/money_latest.rss',
                       'Politics': 'http://rss.cnn.com/rss/cnn_allpolitics.rss',
                       'Technology': 'http://rss.cnn.com/rss/cnn_tech.rss',
                       'Health': 'http://rss.cnn.com/rss/cnn_health.rss',
                       'Entertainment':
                          'http://rss.cnn.com/rss/cnn_showbiz.rss',
                       'Travel': 'http://rss.cnn.com/rss/cnn_travel.rss',
                       'Most Recent': 'http://rss.cnn.com/rss/cnn_latest.rss'
                       }
                  }

# For omitted RSS feed links:
CNN_OMITTED_LINKS_DICT = {'Video': 'http://rss.cnn.com/rss/cnn_freevideo.rss',
                          'CNN 10':
                              'http://rss.cnn.com/services/podcasting/cnn10/rss.xml',
                          'CNN Underscored':
                              'http://rss.cnn.com/cnn-underscored.rss'}
