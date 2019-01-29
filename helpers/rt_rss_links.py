"""

Dictionary containing all links from CNN as values and string descriptors as
keys.
"""

RT_LINKS_DICT = {'news_source_name': 'RT',
                 'source_head_url': 'https://www.rt.com/',
                 'rss_feeds':
                     {'Main Page': 'https://www.rt.com/rss/',
                      'World News': 'https://www.rt.com/rss/news/',
                      'USA News': 'https://www.rt.com/rss/usa/',
                      'UK News': 'https://www.rt.com/rss/uk/',
                      'Sport News': 'https://www.rt.com/sport/',
                      'Russia News': 'https://www.rt.com/russia/',
                      'Business News': 'https://www.rt.com/business/',
                      'Health': 'http://rss.cnn.com/rss/cnn_health.rss',
                      'Entertainment':
                          'http://rss.cnn.com/rss/cnn_showbiz.rss',
                      'Travel': 'http://rss.cnn.com/rss/cnn_travel.rss',
                      'Most Recent': 'http://rss.cnn.com/rss/cnn_latest.rss'
                      }
                 }

# For omitted RSS feed links:
RT_OMITTED_LINKS_DICT = {'Op-ed': 'https://www.rt.com/op-ed/',
                         'RT360': 'https://www.rt.com/360/'
                         }

news_site = RT_LINKS_DICT['news_source_name'].lower()
for feed_site_title, feed_rss_link in RT_LINKS_DICT['rss_feeds'].items():
    feed_python_title = '\'' + \
                        news_site + '_' + \
                        feed_site_title.lower().replace(' ', '_') + \
                        '\','
    print("{'feed_python_title':" + feed_python_title)
    print(" 'feed_site_title': \'" + feed_site_title + '\',')
    print(" 'feed_rss_link': '" + feed_rss_link + '\'}')

    #print(feed_site_title)
    #print(feed_rss_link)


