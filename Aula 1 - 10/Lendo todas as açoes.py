# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 09:31:56 2022

@author: Everton Castro
"""
import pandas as pd
from pandas_datareader import data


csv = pd.read_csv('./Papeis/Papeis atualizados.csv')
csv = list(csv['Cod'])
list_comprehension = [x + '.SA' for x in csv ]

for name_acao in list_comprehension:
    acao =  data.DataReader(name = name_acao, data_source = 'yahoo', start ='2021-02-03')
    acao.to_csv('./Base de dados. 1 ano/' + name_acao[:-3] + ".csv", index=False)
