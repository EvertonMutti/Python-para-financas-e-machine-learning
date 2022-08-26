# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 16:24:49 2022

@author: Everton Castro
"""

import yfinance as yf
import numpy as np
import pandas as pd
from pandas_datareader import data
import matplotlib as plt
import seaborn as sns

#import plotly.express as px


#Petr_df =  data.DataReader(name = 'PETR4.SA', data_source = 'yahoo', start ='1975-03-12')
#print(Petr_df)
#print(Petr_df.info())

#Ceeb_df =  data.DataReader(name = 'CEEB5.SA', data_source = 'yahoo', start ='1975-03-12')
#print(Ceeb_df.tail())

##Petr_df.to_csv("Petr.csv", index=False)
#print(Petr_df[Petr_df['High'] >= 24])

acoes = ['BBAS3.SA', 'SANB3.SA', 'B3SA3.SA', 'PETR4.SA', 'SAPR3.SA', 'BOVA11.SA', 'PETZ3.SA']

acoes_df = pd.DataFrame()

for acao in acoes:
    acoes_df[acao] = yf.download(acao, start = '2010-01-01')['Close']
    acoes_df[acao].replace(np.nan, 0, inplace = True)
    
acoes_df = acoes_df.rename(columns = lambda x: x[:5])
acoes_df.plot(figsize = (15,7), title = 'Histórico do preço das ações')