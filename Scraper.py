# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 13:15:59 2021

@author: ext17
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
response= requests.get('https://www.reuters.com/news/archive/marketsNews?view=page&page=639&pageSize=10')
soup = BeautifulSoup(response.text,"lxml")

df=pd.DataFrame({'Links':[''], 'Date':[''], 'Content':['']})
counter = 0
#This loop goes through the first 10 pages and grabs all the details of each posting
while counter < 600:
    boxes=soup.find('section',{'class':'module'})
    box=boxes.find_all('article',{'class':'story'})
    for b in box:
        try:
            link = b.find('a').get('href')
            link_full ='https://www.reuters.com'+link
            page= requests.get(link_full)
            soup1 = BeautifulSoup(page.text,"lxml")

            article=soup1.find('div',{'class':'ArticleBodyWrapper'}).text
           
            
            date = b.find('span',{'class':'timestamp'}).text
            df=df.append({'Links':link_full, 'Date':date, 'Content':article},ignore_index=True)
        except:
            pass



    next_page=soup.find('a',{'rel':'next'}).get('href')
    next_page_full='https://www.reuters.com/news/archive/marketsNews'+next_page
    response1= requests.get(next_page_full)
    soup = BeautifulSoup(response1.text,"lxml")
    counter += 1
df.to_csv(r'C:\Users\ext17\OneDrive\Рабочий стол\GBPUSD3555.csv')
