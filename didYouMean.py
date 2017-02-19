### Based in a Script from https://github.com/bkvirendra/didyoumean
# encoding: utf-8
unicode("utf-8")
import os
import urllib2
import io
import gzip
import sys
import urllib
import re

from bs4 import BeautifulSoup
from StringIO import StringIO

def getPage(url):
    request = urllib2.Request(url)
    #request.add_header("Content-Type", "text/plain;charset=UTF-8")
    request.add_header('Accept-encoding', 'gzip')
    request.add_header('User-Agent','"Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"')

    response = urllib2.urlopen(request)
    if response.info().get('Content-Encoding') == 'gzip':
        buf = StringIO( response.read())
        f = gzip.GzipFile(fileobj=buf)
        data = f.read()
    else:
        data = response.read()
    return data

def didYouMean(q, encrypted=False, context=""):
    q = str(str.lower(q)).strip()
    if encrypted:
        url = "https://encrypted.google.com/search?q=" + urllib.quote(q + " " + context)
    else:
        url = "https://www.google.com/search?q=" + urllib.quote(q + " " + context)    
    html = getPage(url)
    soup = BeautifulSoup(html, "lxml")
    
    try:
        ans = soup.find("a", attrs={'class' : 'spell'})
        if len(ans.text) == 0:
            return q        
        result = ans.text
        if len(context) !=0:
             result = [word for word in result.split(" ") if word not in unicode(context, "utf-8")]
             result = " ".join(result)
    except AttributeError:
        return False
   
    return result

def spell_check_document(document, window=6):
    document = document.split(" ")
    document = [" ".join(document[i:i+window]) for i in range(0, len(document), window)]
    corrected_chuncks = []
    print(document)
    for chunck in document:
        corrected_chuncks.append(didYouMean(chunck))
    return " ".join(corrected_chuncks)


if __name__ == "__main__":
    response = didYouMean(sys.argv[1])
