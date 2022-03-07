import requests
from bs4 import BeautifulSoup as BS


site = requests.get('https://globus-online.kg/catalog/myaso_ptitsa_ryba/govyadina_baranina_farshi/')
html = BS(site.content, 'html.parser')

title_meat = html.find_all('div', class_='list-showcase__name')
link_meat = html.find_all('div', class_='list-showcase__name')

price_meat = html.find_all('span', class_='c-prices__value')
for el in title_meat:
    title = el.text 
    print(title)

for el in price_meat:
    title = el.text 
    print(title)