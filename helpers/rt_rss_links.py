"""

Dictionary containing all links from CNN as values and string descriptors as
keys.
"""

RT_LINKS_DICT = {'news_source_name': 'RT',
                 'source_head_url': 'https://www.rt.com/',
                 'rss_feeds':
                     [
                         {'feed_python_title': 'rt_main_page',
                          'feed_site_title': 'Main Page',
                          'feed_rss_link': 'https://www.rt.com/rss/'},
                         {'feed_python_title': 'rt_world_news',
                          'feed_site_title': 'World News',
                          'feed_rss_link': 'https://www.rt.com/rss/news/'},
                         {'feed_python_title': 'rt_usa_news',
                          'feed_site_title': 'USA News',
                          'feed_rss_link': 'https://www.rt.com/rss/usa/'},
                         {'feed_python_title': 'rt_uk_news',
                          'feed_site_title': 'UK News',
                          'feed_rss_link': 'https://www.rt.com/rss/uk/'},
                         {'feed_python_title': 'rt_sport_news',
                          'feed_site_title': 'Sport News',
                          'feed_rss_link': 'https://www.rt.com/sport/'},
                         {'feed_python_title': 'rt_russia_news',
                          'feed_site_title': 'Russia News',
                          'feed_rss_link': 'https://www.rt.com/russia/'},
                         {'feed_python_title': 'rt_business_news',
                          'feed_site_title': 'Business News',
                          'feed_rss_link': 'https://www.rt.com/business/'}
                     ]
                 }

# For omitted RSS feed links:
RT_OMITTED_LINKS_DICT = {'Op-ed': 'https://www.rt.com/op-ed/',
                         'RT360': 'https://www.rt.com/360/'
                         }
