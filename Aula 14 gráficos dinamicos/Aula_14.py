# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 15:42:29 2022

@author: Everton SSD
"""

#Rodar no Jupyther
import yfinance as yf
import numpy as np
import pandas as pd
from pandas_datareader import data
import matplotlib as plt
import seaborn as sns
import plotly.express as px



acoes_df =  pd.read_csv('Ações.csv')




figura = px.line(title = 'Histórico de preço')
for i in acoes_df.columns[1:]:
  figura.add_scatter(x = acoes_df['Date'], y = acoes_df[i], name = i)
figura.show()


figura = px.line(title = 'Histórico de preço - Normalização')
acoes_df_normalizado = acoes_df.copy()
for i in acoes_df_normalizado.columns[1:]:
    figura.add_scatter(x = acoes_df['Date'], y = acoes_df[i], name = i)
figura.show()
  