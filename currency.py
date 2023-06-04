# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 08:17:39 2021

@author: ext17
"""

import pandas as pd

df = pd.read_csv(r'C:\Users\ext17\OneDrive\Рабочий стол\EURUSD1440d.csv',
                 parse_dates=["Date"])
a = df.iloc[13251:13267]
a.shape
a
b = pd.read_csv(r'C:\Users\ext17\OneDrive\Рабочий стол\datascience\GBPUSD2020.csv',
                parse_dates=["Date"])
b['Date']

bb = a['4'].diff()
bb
gg = a.drop(['1', '4', '2', '3', '5', 'Unnamed: 0', 'Time'], axis=1)
gg
tt = pd.concat([bb, gg], axis=1)
tt.shape
tt
ttt=tt.rename(columns={"4": "Value"})
ttt
ttt['Value'] = ttt.Value.shift(-1)
ttt

rr = pd.merge(ttt, b, on='Date')
rr.head(0)
rr['Date']
rr
rrr = rr.drop([ 'Unnamed: 0.1', 'Unnamed: 0', 'Links'], axis=1)
rrr.shape
rrr['Value']
rrr['Value'] = rrr.Value>0
rrr
ttt=rrr.rename(columns={"4": "Value"})
rrr

rrr.to_csv(r'C:\Users\ext17\OneDrive\Рабочий стол\GBPUSDfinal3.csv')
