# Import Required Libraries
from bs4 import BeautifulSoup
import pandas as pd
import requests
import json
import time
import re

# Headers
my_header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

# URL for Scraping
url= 'https://www.swiggy.com/dapi/menu/pl?page-type=REGULAR_MENU&complete-menu=true&lat=18.56&lng=73.95&restaurantId=<restaurant_id>'
