import requests
from bs4 import BeautifulSoup
import urllib.parse
from urllib.parse import urlparse
import re

#function which take user question as input string,makes google search and returns a list of links appeared n the first page


def search_question(question):
    
    URL = 'https://google.com/search?q='+question
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    a = soup.find_all('a')
    g_clean = []
    for i in a:
        k = i.get('href')
        pattern = "/url\?q="
        m = re.match(pattern,k)
       # print(m)
        if(m == None):
            continue;
           # print(m)
        n = m.group(0)
        #print("here")
        temp = k[len(n):]
        #print(temp)
        rul = temp.split('&')[0]
       # print(rul)
        domain = urlparse(rul)
        if(re.search('google.com', domain.netloc)):
            continue
        else:
            g_clean.append(rul)
            
    return g_clean
    

    


