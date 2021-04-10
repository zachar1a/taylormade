import requests, json
import urllib.request
from bs4 import BeautifulSoup as bs
from bs4 import BeautifulSoup



# This is a basic get request to stockX and in order
# for it to work we have to pass in a user-agent so
# that they won't detect that we are using an automated
# service

url = 'https://stockx.com/buy/adidas-yeezy-450-cloud-white'
#url = 'http://worldagnetwork.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15'}

result = requests.get(url, headers=headers)
soup = BeautifulSoup(result.text, 'html.parser')

allP = soup.find_all('div')
print(allP)
