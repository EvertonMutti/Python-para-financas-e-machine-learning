# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 22:10:22 2022

@author: Everton SSD
"""

import yfinance as yf
import numpy as np
import pandas as pd
from pandas_datareader import data
import matplotlib as plt
import seaborn as sns


acoes = ['BBAS3.SA', 'SANB3.SA', 'B3SA3.SA', 'PETR4.SA', 'SAPR3.SA', 'BOVA11.SA']

acoes_df = pd.DataFrame()

for acao in acoes:
    acoes_df[acao[:-3]] = yf.download(acao, start = '2010-01-01')['Close']
    acoes_df[acao[:-3]].replace(np.nan, 0, inplace = True)
    


acoes_df = acoes_df.rename(columns = lambda x: x[:5])
#acoes_df.to_csv('./Treinando com ações/Ações.csv', index=False)
acoes_df.plot(figsize = (15,7), title = 'Histórico do preço das ações')

#%%
#Normalização!!!
acoes_df_normalizado = acoes_df.copy()
for i in acoes_df_normalizado.columns:
    acoes_df_normalizado[i] = acoes_df_normalizado[i] / acoes_df_normalizado[i][0]

display(acoes_df_normalizado)
acoes_df_normalizado.plot(figsize = (15,7), title = 'Valorização dos papeis')   
