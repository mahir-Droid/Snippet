import urllib
from urllib.request import Request, urlopen
import requests
from bs4 import BeautifulSoup
import re

def remove(val,userlist):
    try:
        while True:
            userlist.remove(val)
    except ValueError:
        pass
    
    return userlist

def deleteduplicates(userlist):
    return list(dict.fromkeys(userlist))
    

def geturls(url):
    try:
        resp = urllib.request.urlopen(url)
    except:
        return []
    # Get server encoding per recommendation of Martijn Pieters.
    soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'), features="html.parser")  
    external_links = set()
    internal_links = set()
    for line in soup.find_all('a'):
        link = line.get('href')
        if not link:
            continue
        if link.startswith('http'):
            external_links.add(link)
        else:
            internal_links.add(link)

    # Depending on usage, full internal links may be preferred.
    full_internal_links = {
        urllib.parse.urljoin(url, internal_link) 
        for internal_link in internal_links
    }

    data = []

    # all unique external and full internal links.
    for link in external_links.union(full_internal_links):
        data.append(link)





    data = deleteduplicates(data)

    data = [x for x in data if not x.endswith("pdf")]
    data = [x for x in data if not x.endswith("doc")]


    data = [x for x in data if x.startswith("http")]


    data = remove(url,data)
    
    data.append(url)

    return data







def geturlswdepth(url, depth):
    depth = depth - 1
    finallist = []
    
    if depth==0:
        finallist.append(url)
        return finallist
    if depth ==1:
        finallist = geturls(url)
        return finallist
    if depth>1:
        finallist = geturls(url)
        newlist = finallist

        newlist = finallist[:-1]

        for i in range(depth-1):
            currentlist = []
            for link in newlist:
                templist = geturls(link)
                currentlist.append(templist[:-1]) 
            
            finallist = finallist + currentlist
            newlist = currentlist
        
        return finallist



def gettext(url):
    try:
        r = requests.get(url)
    except:
        return []

    soup = BeautifulSoup(r.content, 'html.parser')

    everything = soup.find_all()

    data = []

    for t in everything:
        data.append(t.text)

    return data