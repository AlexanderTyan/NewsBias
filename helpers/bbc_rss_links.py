"""

Dictionary containing all links from CNN as values and string descriptors as
keys.
"""

BBC_LINKS_DICT = {'news_source_name': 'BBC News',
                  'source_head_url': 'https://www.bbc.com/news',
                  'rss_feeds':
                      {'Home': 'http://feeds.bbci.co.uk/news/rss.xml',
                       'World': 'http://feeds.bbci.co.uk/news/world/rss.xml',
                       'US and Canada':
                           'http://feeds.bbci.co.uk/news/world/us_and_canada/rss.xml',
                       'UK': 'http://feeds.bbci.co.uk/news/uk/rss.xml',
                       'Business':
                           'http://feeds.bbci.co.uk/news/business/rss.xml',
                       'Technology':
                           'http://feeds.bbci.co.uk/news/technology/rss.xml',
                       'Science and Environment':
                           'http://feeds.bbci.co.uk/news/science_and_environment/rss.xml',
                       'Entertainment and Arts':
                           'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml',
                       'Health': 'http://feeds.bbci.co.uk/news/health/rss.xml'
                       }
                  }

# For omitted RSS feed links:
RT_OMITTED_LINKS_DICT = {'Opinion': 'http://feeds.foxnews.com/foxnews/opinion',
                         'Video': 'https://feeds.foxnews.com/foxnews/video'
                         }
