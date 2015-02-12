import feedparser
import nltk
import pprint

# rss feeds
url = 'http://languagelog.ldc.upenn.edu/nll/?feed=atom'

feed = feedparser.parse(url)
# feed_title = feed['feed']['title']
# feed_link = feed['feed']['link']
feed_post = feed['entries'][2]['content'][0]['value'].encode('utf-8')
tokens = nltk.word_tokenize(nltk.clean_html(feed_post))

# print 'llog: ', pprint.pprint(feed)
# print 'title: ', feed_title
# print 'link: ', feed_link
# print 'feed_post: ', pprint.pprint(feed_post)

html_file = open('scrape.html', 'w')
html_file.write(feed_post)
html_file.close()
print tokens