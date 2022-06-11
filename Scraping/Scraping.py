from bs4 import BeautifulSoup
import requests

website = ['https://coinmarketcap.com/es/historical/20130428/']

# tags del website 

tag_rank = 'cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__rank'
tag_name = 'sc-1ibw5f9-0 bpOMHJ cmc-table__column-name cmc-table__column-name--narrow-layout'
tag_marketcap = 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__market-cap'
tag_year = 'sc-1v5cdrp-0 jaLaYr cmc-historical-detail__title'

for cripto in website: 
    data = requests.get(cripto)
    soup = BeautifulSoup(data.content, 'html.parser') 

    # find_all names
    names = soup.find_all('div', {'class': tag_name})
    Name = [x.find('a').get('title') for x in names]
    print(Name)

    # find_all MarketCap
    marketscaps = soup.find_all('td', {'class': tag_marketcap})
    marketscaps_amount = [x.find('div').text for x in marketscaps]
    print(marketscaps_amount)

    # find_all Year
    years = soup.find('h1').text[-4:]
    for year in years:
        Year = [ ]
        Year.append(years)

    # find_all Month  
    months = soup.find('h1').text[20:23]
    for month in months:
        Month = [ ]
        Month.append(months)
    print(Year)  
    print(Month)  

with open('CoinMarketCap.txt', 'w') as file: 
    file.write(str(Name)) 