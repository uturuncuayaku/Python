# Andres Trujillo
# Python3 script to connect to Studio Ghibli 
# API https://ghibliapi.herokuapp.com/
# 11/27/2019


import urllib.request
# place in header
# TRN-Api-Key:b957bb99-6591-46f0-9062-a70c421e6922

# GET "https://api.fortnitetracker.com/v1/profile/{pc}/{B1nary001}"
# 1 request per 2 seconds. Contact us for an increased limit. 
# r = requests.get('https://username.carto.com/endpoint/', auth=(username, 1234567890123456789012345678901234567890))

#url = "https://ghibliapi.herokuapp.com/films/58611129-2dbc-4a81-a72f-77ddfc1b1b49"

url2 = "https://api.fortnitetracker.com/v1/profile/pc/B1nary001"

request = urllib.request.Request(url2)
response = urllib.request.urlopen(request)

data_content = response.read()

# wb is write in binary mode
# w+ wont work because data_content is bytes
jsonFile = open("fortnitestats.json", "wb")
jsonFile.write(data_content)
jsonFile.close()
print(data_content)


