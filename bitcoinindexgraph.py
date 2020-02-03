# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 17:17:28 2019

@author: simasurk
"""

import requests
import matplotlib.pyplot as plt

#req = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
#req.json()

reqall = requests.get('https://api.coindesk.com/v1/bpi/historical/close.json')
data_dict = reqall.json()
dates = list(data_dict['bpi'].keys())
bitcoin_amounts = list(data_dict['bpi'].values())
#len(bitcoin_amounts)

plt.plot(range(1,32), bitcoin_amounts, color='black', linestyle='dashed', marker='o')