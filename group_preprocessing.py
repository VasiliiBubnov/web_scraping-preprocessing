# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 14:21:44 2021

@author: ext17
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
import pandas as pd
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer
import string
import re
df=pd.read_csv(r'C:\Users\ext17\OneDrive\Рабочий стол\GBPUSD3555.csv')
df=df.drop(0)
df['Content'] = df.groupby(['Date'])['Content'].transform(lambda x : ' '.join(x))
df = df.drop_duplicates('Content') 
df.shape
df.head
df['Date']
a=df.iloc[7]
len(a)
df.to_csv(r'C:\Users\ext17\OneDrive\Рабочий стол\GBPUSD4444.csv')
a=df.groupby('Date')
b=a.count()
b
df[7]
df=df.drop(0)
df.columns
stop = set(stopwords.words('english')) 
print(stop)
import re
temp =[]
snow = nltk.stem.SnowballStemmer('english')
final_X = df['Content']
for sentence in final_X:
    sentence = sentence.lower()                 # Converting to lowercase
    cleanr = re.compile('<.*?>')
    sentence = re.sub(cleanr, ' ', sentence)        #Removing HTML tags
    sentence = re.sub(r'[?|!|\'|"|“|”|-|:|;|1|2|3|4|5|6|7|8|9|0|$|-|-|#]',r'',sentence)
    sentence = re.sub(r'[.|,|)|(|\|/|-|–]',r' ',sentence)        #Removing Punctuations
    
    words = [snow.stem(word) for word in sentence.split() if word not in stopwords.words('english')]   # Stemming and removing stopwords
    temp.append(words)
    
final_X = temp 
final_X[1]
print(final_X[3])
sent = []
for row in final_X:
    sequ = ''
    for word in row:
        sequ = sequ + ' ' + word
    sent.append(sequ)

final_X = sent
print(final_X[3])