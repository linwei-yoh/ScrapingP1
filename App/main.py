#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib.error import HTTPError,URLError
from urllib.request import urlopen
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except (HTTPError,URLError) as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(),"lxml")
        title = bsObj.body.h1
    except ArithmeticError as e:
        return None
    return title

if __name__ == '__main__':
    title = getTitle("http://www.pythonscraping.com/pages/page1.html")
    if title == None:
        print("Not found")
    else:
        print(title)