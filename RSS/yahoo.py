import time
import urllib2
from urllib2 import urlopen
import re
import cookielib, urllib2
from cookielib import CookieJar

# changes header in case site doesnt let robots pass through
cj = CookieJar() 
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]


def main():
    try:
       page = 'http://finance.yahoo.com/news/rssindex'
       sourceCode = opener.open(page).read()
       #print sourceCode

       try:
           #titles = re.findall(r'<title>(.*?)</title>',sourceCode)  
           titles = re.findall(r'<title>(.*?)</title>',sourceCode)
           descriptions = re.findall(r'<description>(.*?)&lt',sourceCode)
           counter = 0
           while counter < 5:
               
               for title in titles[2:]:
                   
                   print ("title: ",title)
                   print ("desciption: "+descriptions[counter])
                   print "                       "
                   counter +=1
    
           
       except Exception, e:
           print str(e)
           print "inner try loop failure"
       

    except Exception, e:
        print str(e)
        print "main try loop failure"

main()
