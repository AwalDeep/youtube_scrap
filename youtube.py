# -*- coding: utf-8 -*-
"""
Created on Sun May 13 23:10:49 2018

@author: Awal
"""

from bs4 import BeautifulSoup
import urllib.request


def SearchVid(search):
    responce = urllib.request.urlopen('https://www.youtube.com/results?search_query='+search)

    soup = BeautifulSoup(responce)    
    divs = soup.find_all("div", { "class" : "yt-lockup-content"})


    for i in divs:
        href= i.find('a', href=True)
        href['href']= href['href'].replace("watch?v=", "embed/")
        print(href.text,  "\nhttps://www.youtube.com"+href['href'], '\n')
        with open(SearchString.replace("%20", "_")+'.txt', 'a') as writer:
            writer.write("https://www.youtube.com"+href['href']+'\n')

print("What are you looking for?")
SearchString = input()
SearchVid(SearchString.replace(" ", "%20"))


#code for web app integration

#<html>

#<iframe width="560" height="315" src="\nhttps://www.youtube.com"+href['href']
#frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
#</html> 