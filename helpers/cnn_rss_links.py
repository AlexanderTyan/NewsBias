"""

Dictionary containing all links from CNN as values and string descriptors as
keys.
"""

CNN_LINKS_DICT = {'news_source_name': 'CNN',
                  'source_head_url': 'https://www.cnn.com/',
                  'rss_feeds':
                      [
                          {'feed_python_title': 'cnn_top_stories',
                           'feed_site_title': 'Top Stories',
                           'feed_rss_link':
                               'http://rss.cnn.com/rss/cnn_topstories.rss'},
                          {'feed_python_title': 'cnn_world',
                           'feed_site_title': 'World',
                           'feed_rss_link':
                               'http://rss.cnn.com/rss/cnn_world.rss'},
                          {'feed_python_title': 'cnn_us',
                           'feed_site_title': 'U.S.',
                           'feed_rss_link':
                               'http://rss.cnn.com/rss/cnn_us.rss'},
                          {'feed_python_title': 'cnn_business',
                           'feed_site_title': 'Business (CNNMoney.com)',
                           'feed_rss_link':
                               'http://rss.cnn.com/rss/money_latest.rss'},
                          {'feed_python_title': 'cnn_politics',
                           'feed_site_title': 'Politics',
                           'feed_rss_link':
                               'http://rss.cnn.com/rss/cnn_allpolitics.rss'},
                          {'feed_python_title': 'cnn_technology',
                           'feed_site_title': 'Technology',
                           'feed_rss_link':
                               'http://rss.cnn.com/rss/cnn_tech.rss'},
                          {'feed_python_title': 'cnn_health',
                           'feed_site_title': 'Health',
                           'feed_rss_link':
                           'http://rss.cnn.com/rss/cnn_health.rss'},
                          {'feed_python_title': 'cnn_entertainment',
                           'feed_site_title': 'Entertainment',
                           'feed_rss_link':
                               'http://rss.cnn.com/rss/cnn_showbiz.rss'},
                          {'feed_python_title': 'cnn_travel',
                           'feed_site_title': 'Travel',
                           'feed_rss_link':
                               'http://rss.cnn.com/rss/cnn_travel.rss'},
                          {'feed_python_title': 'cnn_most_recent',
                           'feed_site_title': 'Most Recent',
                           'feed_rss_link':
                               'http://rss.cnn.com/rss/cnn_latest.rss'}
                      ]
                  }

# For omitted RSS feed links:
CNN_OMITTED_LINKS_DICT = {'Video': 'http://rss.cnn.com/rss/cnn_freevideo.rss',
                          'CNN 10':
                              'http://rss.cnn.com/services/podcasting/cnn10/rss.xml',
                          'CNN Underscored':
                              'http://rss.cnn.com/cnn-underscored.rss'}




# news_site = CNN_LINKS_DICT['news_source_name'].lower()
# for feed_site_title, feed_rss_link in CNN_LINKS_DICT['rss_feeds'].items():
#     feed_python_title = '\'' + \
#                         news_site + '_' + \
#                         feed_site_title.lower().replace(' ', '_') + \
#                         '\','
#     print("{'feed_python_title': " + feed_python_title)
#     print(" 'feed_site_title': \'" + feed_site_title + '\',')
#     print(" 'feed_rss_link': '" + feed_rss_link + '\'},')
