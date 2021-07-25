from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException as NSEE
import os

import time, csv, os, pathlib
from .writeData import writeData

def goToBottom(driver):
    ''' auto-scrolls to the bottom of page  so resources can load in '''

    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    while(match==False):
        lastCount = lenOfPage
        time.sleep(5)
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount==lenOfPage:
            match=True

def getShoeUrl():
    ''' iterates through the dirs in Brand Data and finds the 'baseData' files in each '''

    shoeNamesAndMSRP = []
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
                            print(row)
                            shoeNamesAndMSRP.append((d,row['Shoe'],row['MSRP']))
            os.chdir('../../')
    except:
        print('hello world')

    return shoeNamesAndMSRP

def searchForShoe(driver,url, shoeName, shoeMSRP):
    '''
        enters search name into the stockx search bar and clicks
        on the first shoe in the drop-down menu
    '''

    driver.get(url)

    searchBar = driver.find_element_by_id('home-search')
    searchBar.send_keys(shoeName)
    goToBottom(driver)

    click = driver.find_elements_by_class_name('list-item-content')
    try:
        click[0].click()
    except:
        return
    showDataTable(driver, shoeMSRP)

def showDataTable(driver, shoeMSRP):
    ''' finds and locates the 'Load More' button in the datatable for stockx '''

    driver.implicitly_wait(2)
    try:
        print('in try')
        if driver.find_element_by_xpath("//*[contains(text(), 'OOPS!')]"):
            return
    except:
        try:
            if driver.find_element_by_xpath("//*[contains(text(), 'View All Sales')]"):
                driver.find_element_by_xpath("//*[contains(text(), 'View All Sales')]").click()
        except NSEE:
            if driver.find_element_by_xpath("//*[cotaines(text(), 'View Sales')]"):
                driver.find_element_by_xpath("//*[cotaines(text(), 'View Sales')]").click()
        activateLoadMoreButtons(driver, shoeMSRP)

def activateLoadMoreButtons(driver, shoeMSRP):
    ''' Finds the 'Load More' buttons in the table and clicks it '''

    shoeName = driver.find_element_by_xpath('//*[@id="product-header"]/div[1]/div/h1').text + str('.csv')
    try:
        while(driver.find_element_by_xpath("//*[contains(text(), 'Load More')]")):
            print('hello world')
            #goToBottom(driver)
            driver.find_element_by_xpath("//*[contains(text(), 'Load More')]").click()
            time.sleep(1)
    except:
        print("Either finished or no button")
        readDataTable(driver, shoeName, shoeMSRP)

def readDataTable(driver, shoeName, shoeMSRP):
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
        # shoeMSRP = shoeMSRP
        data = (date, time, size, price, shoeMSRP)
        wd.openFileOrCreateFile(shoeName, data)
        print(tr.text)

def main():
    driver = webdriver.Safari()
    shoeNamesAndMSRP = getShoeUrl()
    url = 'https://stockx.com'
    for shoe in shoeNamesAndMSRP:
        print(shoe)
        searchForShoe(driver,url,shoe[1], shoe[2])
    time.sleep(3)
