#!/usr/bin/python
# Filename : mp3Scrape.py
from BeautifulSoup import BeautifulSoup
import urllib2
import re
import sys
#import urllib

base_url = "http://114.143.5.121"
mp3List = []
#start_dir = sys.argv[1]
#filename = sys.argv[2]
start_dir = '/D8mp3/Hindi/Bollywood/'
filename = "hindiYear.txt"
server = 'apache'
#relative_url = '/load'
#
#for y in level1_url :
#    print level1_url[count]
#    count = count + 1
# lets open the first url
#full_url = base_url + level1_url[0]
#page = urllib2.urlopen(full_url)
def regexMatch(regex , fromString):
    matchfound = re.search(regex,fromString)
    if(matchfound ):
        return True
    else:
        return False
    



def fetch_urls(base_url , relative_url ) :
  
#    req = '';
#    relative_url = urllib.urlencode(relative_url)
    regex = relative_url.replace('%20',' ') 
#    regex = regex.replace('[','\[')
#    regex = regex.replace(']','\]')
    regexSpecial = '[]^$.|?*+(){}'
    for specialChar in regexSpecial :
        p = '\\' + specialChar
        regex =regex.replace(specialChar , p)
#        print y
    regex = regex + '\w+'
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
    if (server == 'apache'):
        for x in  links :
            match = re.search(regex, relative_url+x['href'])
            if match :
                level1_url.append(relative_url+x['href'])
    #                print str(x['href'])
    elif(server == 'LightSpeed'):
         for x in  links :
            match = re.search(regex, x['href'])
            if match :
                level1_url.append(x['href'])
    #                print str(x['href'])

    return level1_url
        
        
#urls = fetch_urls(base_url , '/load/')
#print base_url+urls[0]level2_url = fetch_urls(base_url , '/load/128 kbps/')
f = file(filename, 'w')
mp3Regex = r'.mp3\Z'
#for y in urls:




    
def traverse_folder(foldername):
#    print foldername
    urls2 = ''
    try:
        urls2 = fetch_urls(base_url, foldername)
    except:
        print " Url Fetching error"
    for q in urls2:
        if regexMatch('/\Z', q):
            traverse_folder(q)
        else:
            if regexMatch(mp3Regex,q):
                try:
                    f.write(q+'\n')
                    print q;
                except:
                    print "Not Ascii"
                
                


traverse_folder(start_dir)

f.close()