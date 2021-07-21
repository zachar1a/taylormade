from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException as NSEE
import os

import time, csv, os, pathlib
from .writeData import writeData

def goToBottom(driver):
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




#####
def activateLoadMoreButtons(driver):
    '''
    This is called in the showDataTable function
    and locates and clicks on the load more button
    and waits 1 second after every emulated click
    '''
    #driver.find_element_by_xpath('//*[@id="chakra-modal--body-148"]/div/button').click()
    shoeName = driver.find_element_by_xpath('//*[@id="product-header"]/div[1]/div/h1').text + str('.csv')
    try:
        while(driver.find_element_by_xpath("//*[contains(text(), 'Load More')]")):
            print('hello world')
            #goToBottom(driver)
            driver.find_element_by_xpath("//*[contains(text(), 'Load More')]").click()
            time.sleep(1)
    except:
        print("Either finished or no button")
        readDataTable(driver, shoeName)


def readDataTable(driver, shoeName):
    '''
    @param shoeName
    shoeName is a string with .csv appended to it

    The function reads a data table with the attributes:
    date | time | size | price
    and appends data only if the date and time don't
    show up in the same row
    '''
    table = driver.find_element_by_xpath('//*[@id="480"]')
    table = table.find_element_by_tag_name('tbody')
    tableRows = table.find_elements_by_tag_name('tr')
    wd = writeData()
    for tr in tableRows:
        date = tr.find_elements_by_tag_name('td')[0].text
        time = tr.find_elements_by_tag_name('td')[1].text
        size = tr.find_elements_by_tag_name('td')[2].text
        price= tr.find_elements_by_tag_name('td')[3].text
        msrp = driver.find_elements_by_class_name('')
        data = (date, time, size, price, msrp)
        wd.openFileOrCreateFile(shoeName, data)
        print(tr.text)

def showDataTable(driver):
    '''
    @param url
    url to desired shoe

    The function reaches the desired
    url then waits 2 seconds to allow
    the page to load and then locates
    and clicks on the button to show table
    '''
    #driver.get(url)
    driver.implicitly_wait(2)
    try:
        print('in try')
        if(driver.find_element_by_class_name('not-found-container')):
            return
    except:
        try:
            driver.find_element_by_xpath("//*[contains(text(), 'View All Sales')]").click()
        except NSEE:
            driver.find_element_by_xpath("//*[cotaines(text(), 'View Sales')]").click()
        activateLoadMoreButtons(driver)



#####

def getShoeUrl():
    shoeNames = []
    os.chdir(pathlib.Path(__file__).parent.absolute())
    print(os.getcwd())

    try:
        for d in os.listdir('Brand Data/'):
            if d == '.DS_Store':
                continue
            os.chdir('Brand Data/' + d + '/')
            for f in os.listdir():
                if f == 'baseData.csv':
                    with open(f ,'r') as file:
                        reader = csv.DictReader(file)
                        for row in reader:
                            shoeNames.append((d,row['Shoe']))

            os.chdir('../../')
        return shoeNames
    except:
        print('hello world')




def searchForShoe(driver,url, shoeName):
    driver.get(url)

    searchBar = driver.find_element_by_id('home-search')
    searchBar.send_keys(shoeName)
    goToBottom(driver)

    click = driver.find_elements_by_class_name('list-item-content')
    try:
        click[0].click()
    except:
        return
    showDataTable(driver)


def main():
    driver = webdriver.Safari()
    shoeNames = getShoeUrl()
    url = 'https://stockx.com'
    for shoe in shoeNames:
        print(shoe)
        searchForShoe(driver,url,shoe[1])
    time.sleep(3)

#main()
