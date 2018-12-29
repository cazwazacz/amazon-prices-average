import requests
import sys
import os
from bs4 import BeautifulSoup

headers = {'user-agent': os.environ['USER_AGENT_STRING']}
search_term = sys.argv[1].replace(' ', '+')
request_url = 'https://www.amazon.co.uk/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=' + search_term

body = requests.get(request_url, headers=headers)
soup = BeautifulSoup(body.text, 'html.parser')
prices = soup.findAll('span', {'class': 'a-color-price'})

prices = list(filter(lambda price: 'Only' not in price.text, prices))

def clean_price(string):
    commas_removed = string.replace(',', '')
    return (float(commas_removed[1:]))

cleaned_prices = list(map(lambda price: clean_price(price.text), prices))

def get_average(prices):
    if len(cleaned_prices) == 0:
        print('Sorry, there were no prices found')
        return

    return (sum(cleaned_prices) / float(len(cleaned_prices)))

print(get_average(cleaned_prices))
