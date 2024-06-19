import requests
import random 
from bs4 import BeautifulSoup
from requests_html import HTMLSession

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/89.0 Safari/537.36',
]

# url = 'https://react-amazon-bestsellers-books-dy.netlify.app/'
url = "https://www.lazada.sg/#hp-official-stores"

session = HTMLSession()

headers = {
    'User-Agent': random.choice(USER_AGENTS),
}

response = session.get(url)
response.html.render(sleep=2)

# print (response.html)
# print (response.html.find('div.card-jfy-wrapper'))
soup = BeautifulSoup(response.html.html, 'html.parser')
products = soup.find_all('div', class_='ripple-container')

for product in products:
    product_name = product.find('class.card-jfy-title').text
    
    print (product_name)

# for product in response.html.find('div.ripple-container'): 
#     print (product)