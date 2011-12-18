import sys
import os
#!/usr/bin/python
# Filename : mp3Scrape.py
from BeautifulSoup import BeautifulSoup
import urllib2
import re
from BitTorrent import URL


def fetch_urls(base_url , relative_url ) :
  
#    req = '';
#    relative_url = urllib.urlencode(relative_url)
    regex = relative_url + '\w+'
    relative_url = relative_url.replace(' ','%20')
    full_url = base_url + relative_url
#    print full_url
    
#    print 'reg ex --' + regex
#    print 'Encode ---' + full_url
    req = urllib2.Request(full_url)
    page = urllib2.urlopen(req)

    

    soup = BeautifulSoup(page)
    #soup = BeautifulSoup(soup.prettify())
    links =  soup.findAll('a')
    level1_url = []
    #count = 0
    for x in  links :
        match = re.search(regex, x['href'])
        if match :
            level1_url.append(x['href'])
#                print str(x['href'])

    return level1_url

base_url = "http://mp3.tamilmp3songs.mobi"
urls = fetch_urls(base_url, '/load/')
count = 1
for x in urls:
    
    x = x.replace(' ','%20')
#    x = x.replace('/','\/')
    command = "python mp3Scrapper2.py " + x + " " +str(count)+".mp3.txt &"
    print command
    os.system(command)
    count = count +1

















