import requests
import pandas as pd
import numpy as np 
from bs4 import BeautifulSoup 
from time import sleep
from random import randint

headers = {"Accept-Language": "en.US,en;q=0.5"}

Rank = []
Name = []
CoinMarketCap = []
Month = []
Year = []

CoinMarketCap = 'https://coinmarketcap.com/es/historical/20130428/'

for cripto in CoinMarketCap: 
    cripto = requests.get("https://coinmarketcap.com/es/historical/20130428/")
    soup = BeautifulSoup(cripto.content, 'html.parser')
    rank = soup.find('td', attrs = {'class': 'cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__rank'}).text
    Rank.append(rank)
print(Rank)