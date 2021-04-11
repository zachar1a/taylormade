import requests, json
import urllib.request
from bs4 import BeautifulSoup as bs
from bs4 import BeautifulSoup



# This is a basic get request to stockX and in order
# for it to work we have to pass in a user-agent so
# that they won't detect that we are using an automated
# service

# Instead of using bs4 to get data from stockx I am going to 
# use a web driver, the only problem is that a browser is going
# to have to be open to run the program
'''
url = 'https://stockx.com/buy/adidas-yeezy-450-cloud-white'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15'}
result = requests.get(url, headers=headers)
'''

# this is page one of lifestyle shoes page. I am iterating over all of the shoes
# and then going to save the links and the images
# Need to put these into a database

url = 'https://www.nike.com/w/mens-lifestyle-shoes-13jrmznik1zy7ok'
result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')

allP = soup.find_all('a', class_="product-card__link-overlay")

for link in allP:
    print(link.text + " " + link.attrs['href'])
