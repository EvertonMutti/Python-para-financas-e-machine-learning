# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 19:16:19 2022

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
    acoes_df[acao[:-3]] = yf.download(acao, start = '2010-01-01')['Close']
    acoes_df[acao[:-3]].replace(np.nan, 0, inplace = True)

#acoes_df.plot(figsize = (15,7), title = 'Histórico do preço das ações')
sns.set(rc={'figure.figsize':(10,50)})
for i in np.arange(len(acoes_df.columns)):
    plt.subplot(8,1, i + 1)
    sns.histplot(acoes_df[acoes_df.columns[i]], kde = True)
    plt.title(acoes_df.columns[i])