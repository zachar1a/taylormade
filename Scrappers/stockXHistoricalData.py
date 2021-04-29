from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import time
from writeData import writeData

driver = webdriver.Safari()
def activateLoadMoreButtons():
    '''
    This is called in the showDataTable function
    and locates and clicks on the load more button
    and waits 1 second after every emulated click
    '''
    #driver.find_element_by_xpath('//*[@id="chakra-modal--body-148"]/div/button').click()
    shoeName = driver.find_element_by_xpath('//*[@id="product-header"]/div[1]/div/h1').text + str('.csv')
    try:
        while(driver.find_element_by_css_selector('button.css-13xjp80')):
            driver.find_element_by_css_selector('button.css-13xjp80').click()
            time.sleep(1)
    except:
        print("Either finished or no button")
        readDataTable(shoeName)


def readDataTable(shoeName):
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
        data = (date, time, size, price)
        wd.openFileOrCreateFile(shoeName, data)
        print(tr.text)

def showDataTable(url):
    '''
    @param url
    url to desired shoe

    The function reaches the desired
    url then waits 2 seconds to allow
    the page to load and then locates
    and clicks on the button to show table
    '''
    driver.get(url)
    driver.implicitly_wait(2)
    driver.find_element_by_xpath('//*[@id="market-summary"]/div[2]/div/div[2]/div[3]/button').click()
    activateLoadMoreButtons()

# TODO  
# Create a function wrapper that takes in shoe links
# found in brand data files

# find()
showDataTable('https://stockx.com/nike-blazer-mid-77-vintage-white-black')
showDataTable('https://stockx.com/adidas-yeezy-boost-700-bright-blue')
showDataTable('https://stockx.com/nike-air-presto-off-white')
#driver.close()
