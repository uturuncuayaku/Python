# Andres Trujillo
# Source: Engineer man on YT
# Python Web Scraping with Beautiful Soup and Regex

import requests
from bs4 import BeautifulSoup

# get the data
data = requests.get('<html location>')

soup = BeautifulSoup(data.text, 'html.parser')

# get data simply by looking for html tags
# for tr in soup.find_all('tr'):
#     for td in tr.find_all('td')
#         print(td.text)

# get data simply by looking for each tr
# for tr in soup.find_all('tr'):
#     values = td.text for td in tr.find_all('td')
#     print(values)

# data = []
# for tr in soup.find_all('tr'):
#     values = td.text for td in tr.find_all('td')
#     data.append(values)
# print(data)

# data = []
# for tr in soup.find_all('tr', {'class: 'special'}):
#     values = td.text for td in tr.find_all('td')
#     data.append(values)
# print(data)

data = []
div = soup.find('div', {'class': 'special_table'})
for tr in soup.find_all('tr'):
    values = [td.text for td in tr.find_all('td')]
    data.append(values)





