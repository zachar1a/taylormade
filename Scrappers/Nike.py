from selenium import webdriver
import requests, json, time, csv, os
from writeData import writeData
from expandData import expandData

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

lifestyle = 'https://www.nike.com/w/mens-lifestyle-shoes-13jrmznik1zy7ok'
jordan = 'https://www.nike.com/w/mens-jordan-shoes-37eefznik1zy7ok'
running = 'https://www.nike.com/w/mens-running-shoes-37v7jznik1zy7ok'
basketball = 'https://www.nike.com/w/mens-basketball-shoes-3glsmznik1zy7ok'


def goToBottom():
    '''
    Use this to auto scroll to bottom of page in viewport to loard more items
    in a non-pagenazed web page
    '''

    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    while(match==False):
        lastCount = lenOfPage
        time.sleep(5)
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount==lenOfPage:
            match=True

#shoes = driver.find_elements_by_class_name('product-card__title')

def writeToFile(fileName, data):
    '''
    Checks if file is in dir if not
    then creates it
    '''

    resetPath = '../../Scrappers'
    pathToBrandData = '../Brand Data/'
    if 'Nike' in os.listdir(pathToBrandData):
        if fileName in os.listdir(pathToBrandData + 'Nike'):
            os.chdir(pathToBrandData + 'Nike')
            wd = writeData()
            wd.writeToFile(fileName,data)
            os.chdir(resetPath)
        else:
            os.chdir(pathToBrandData + 'Nike')
            with open(fileName, 'a', newline='') as file:
                csv.writer(file).writerow(['Shoe', 'Link'])
                file.close()
                writeToFile(fileName, data)

def findShoesOnPage(url):
    driver.get(url) 

    goToBottom()

    shoes = driver.find_elements_by_class_name('product-card__body')
    for shoe in shoes:
        link = shoe.find_element_by_class_name('product-card__link-overlay')
        print(link.text)
        print(link.get_attribute('href'))
        print('')
        data = (link.text, link.get_attribute('href'))
        writeToFile('baseData.csv',data)


def main():
    findShoesOnPage(lifestyle)
    findShoesOnPage(jordan)
    findShoesOnPage(running)
    findShoesOnPage(basketball)

    expand = expandData()
    shoes = expand.getCsvData('Nike', 'baseData.csv')

    for shoe in shoes:
        print(shoe['Link'])
        expand.getShoeDetails(driver,'Nike', 'Nike.csv', shoe['Link'])

if __name__ == '__main__':
    main()

driver.close()
