# Import Required Libraries
import pandas as pd
import requests

# Headers
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

# URL for Scraping
url= 'https://www.swiggy.com/dapi/menu/pl?page-type=REGULAR_MENU&complete-menu=true&lat=18.56&lng=73.95&restaurantId=37968'

# Response
response = requests.request("GET", url, headers = headers)

# Error Handling
if response.status_code != 200:
    raise Exception('Failed to load page {}'.format(url))

# Coverting the Response to JSON Format
data=response.json()

# Names Dictionary
names=[]

# Fetch Names
# Only the 11th entry in response is coded differently so a different logic is required to fetch it's name
for c in range(1, 11):
    for cards in data['data']['cards'][4]['groupedCard']['cardGroupMap']['REGULAR']['cards'][c]['card']['card']['itemCards']:
        names.append(cards['card']['info']['name'])
        
for cards in data['data']['cards'][4]['groupedCard']['cardGroupMap']['REGULAR']['cards'][11]['card']['card']['categories']:
    for items in cards['itemCards']:
        names.append(items['card']['info']['name'])
        
for c in range(12, 17):
    for cards in data['data']['cards'][4]['groupedCard']['cardGroupMap']['REGULAR']['cards'][c]['card']['card']['itemCards']:
        names.append(cards['card']['info']['name'])
        
# Prices Dictionary
prices=[]

# Fetch Names
# Only the 11th entry in response is coded differently so a different logic is required to fetch it's name
for c in range(1, 11):
    for cards in data['data']['cards'][4]['groupedCard']['cardGroupMap']['REGULAR']['cards'][c]['card']['card']['itemCards']:
        prices.append(cards['card']['info']['price'])
        
for cards in data['data']['cards'][4]['groupedCard']['cardGroupMap']['REGULAR']['cards'][11]['card']['card']['categories']:
    for items in cards['itemCards']:
        prices.append(items['card']['info']['price'])
        
for c in range(12, 17):
    for cards in data['data']['cards'][4]['groupedCard']['cardGroupMap']['REGULAR']['cards'][c]['card']['card']['itemCards']:
        prices.append(cards['card']['info']['price'])


print(prices)