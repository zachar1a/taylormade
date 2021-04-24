from selenium import webdriver
import requests, json, time, csv

driver = webdriver.Safari()


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


driver.get(url)

def goToBottom():
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    while(match==False):
        lastCount = lenOfPage
        time.sleep(5)
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount==lenOfPage:
            match=True

shoes = driver.find_elements_by_class_name('product-card__body')
#shoes = driver.find_elements_by_class_name('product-card__title')

goToBottom()
for shoe in shoes:
    link = shoe.find_element_by_class_name('product-card__link-overlay')
    print(link.text)
    print(link.get_attribute('href'))
    print('')
