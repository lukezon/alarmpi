#!/usr/bin/env python

import feedparser
import ConfigParser
Config=ConfigParser.ConfigParser()
try:
  Config.read('alarm.config')
except:
  raise Exception('Sorry, Failed reading alarm.config file.')

try: 
    rss = feedparser.parse('http://feeds.bbci.co.uk/news/world/rss.xml')


#for entry in rss.entries[:4]:
#    print entry['title']
#    print entry['description']
#    
#print rss.entries[0]['title']
#print rss.entries[0]['description']
#print rss.entries[1]['title']
#print rss.entries[1]['description']
#print rss.entries[2]['title']
#print rss.entries[2]['description']
#print rss.entries[3]['title']
#print rss.entries[3]['description']

    newsfeed = rss.entries[0]['title'] + '. Description: ' + rss.entries[0]['description'] + '.  ' + rss.entries[1]['title'] + '. description: ' + rss.entries[1]['description'] + '.  ' + rss.entries[2]['title'] + '. description: ' + rss.entries[2]['description'] + '.  ' + rss.entries[3]['title'] + '. description: ' + rss.entries[3]['description'] + '.  ' 

# print newsfeed
    newsfeed = newsfeed.encode('utf-8')

# Today's news from BBC
    news = 'And now, Luke, your morning global news. ' + newsfeed
    

except rss.bozo:
    news = 'Failed to reach BBC News'

if Config.get('main','debug') == str(1):
  print news
