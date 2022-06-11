from email.mime import text
from gettext import textdomain
from bs4 import BeautifulSoup 
import requests
import pandas as pd
import numpy as np 
from time import sleep
from random import randint

website = ['https://coinmarketcap.com/es/historical/20130428/','https://coinmarketcap.com/es/historical/20130505/']

# result = requests.get(website)
# content = result.text 
# soup = BeautifulSoup(content, 'lxml')

# print(soup.prettify())

Row = [ ]
Name = [ ]
MarketCap = [ ]
Month = [ ]
Year = [ ]

tag_rank = 'cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__rank'
tag_name = 'cmc-table__column-name--name cmc-link'
tag_marketcap = 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__market-cap'
tag_year = 'sc-1v5cdrp-0 jaLaYr cmc-historical-detail__title'

for cripto in website: 
    data = requests.get(cripto)
    soup = BeautifulSoup(data.content, 'html.parser') # or 'lxml' 'html.parser'

    # find_all names
    names = soup.find_all('a', {'class': tag_name})
    for names in names:
        Name.append(names.text)
        
    # find_all MarketCap
    marketscaps = soup.find_all('td', {'class': tag_marketcap})
    for marketcap in marketscaps:
        MarketCap.append(marketscaps)

    print(MarketCap)
   
# for cripto in soup.find_all('tr'):
#    print(cripto.get('cmc-table-row))

# print('\n'.join(map(str, Row)))

# with open('CoinMarketCap.txt', 'w') as file: 
#    file.write(Crypto) 




