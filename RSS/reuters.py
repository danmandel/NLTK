import time
import urllib2
from urllib2 import urlopen
import re
import cookielib, urllib2
from cookielib import CookieJar
import datetime

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

def main():
    try:
        #page = 'http://www.huffingtonpost.com/feeds/index.xml'
        page = 'http://feeds.reuters.com/reuters/companyNews'
        sourceCode = opener.open(page).read()
        #print sourceCode

        try:
            titles = re.findall(r'<title>(.*?)</title>',sourceCode)
            links = re.findall(r'<link>(.*?)</link>',sourceCode)
            #for title in titles:
            #    print title
            for link in links:
               if '.rdf' in link:
                   pass
               else:
                    print 'let\'s visit:', link
                    linkSource = opener.open(link).read()
                    #print linkSource
                    content = re.findall(r'<p>(.*?)</p>',linkSource) # any character or new line
                    linesOfInterest = re.findall(r'<p>(.*?)</p>', str(content))
                    for theContent in content:
                        print theContent
                    time.sleep(100)

               
        except Exception, e:
            print str(e)

    except Exception,e:
        print str(e)
        pass

main()
		
