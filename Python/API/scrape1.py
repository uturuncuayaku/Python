# Andres Trujillo
# Source: Engineer man on YT
# Python Web Scraping with Beautiful Soup and Regex

import requests
import re

# get the data
data = requests.get('http://www.mg-cc.org/club-information/club-contacts')

phones = re.findall(r'(\(?[0-9]{3}\)?(?:\-|\s|\.)?[0-9]{3}(?:\-|\.)[0-9]{4})', data.text)
emails = re.findall(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)', data.text)

print(phones,emails)