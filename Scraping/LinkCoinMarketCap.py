from bs4 import BeautifulSoup 
import requests


website = 'https://coinmarketcap.com/es/historical/'
result = requests.get(website)
content = result.text 


soup = BeautifulSoup(content, 'lxml')

Links = soup.find("a", class_="historical-link cmc-link").text

print(Links)



