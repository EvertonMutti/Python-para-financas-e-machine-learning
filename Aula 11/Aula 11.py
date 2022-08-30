# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 21:56:58 2022

@author: Everton SSD
"""

import yfinance as yf
import numpy as np
import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt
import seaborn as sns

acoes = ['BBAS3.SA', 'SANB3.SA', 'B3SA3.SA', 'PETR4.SA', 'SAPR3.SA', 'BOVA11.SA', 'SAPR3.SA']
acoes_df = pd.DataFrame()

for acao in acoes:
    acoes_df[acao[:-3]] = yf.download(acao, start = '2020-01-01')['Close']

    
sns.boxplot( x = acoes_df['BBAS3'])
acoes_df['BBAS3'].describe()

#%%
sns.set(rc={'figure.figsize':(10,50)})
for i in np.arange(len(acoes_df.columns)):
    plt.subplot(8,1, i + 1)
    sns.boxplot(x = acoes_df[acoes_df.columns[i]])
    plt.title(acoes_df.columns[i])