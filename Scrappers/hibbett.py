from selenium import webdriver
from .writeData import writeData
import time



time.sleep(5)

def loadAllShoes(driver):
    flag = True
    try:
        while(driver.find_element_by_link_text('Load More') and flag):
            time.sleep(5)
            try:
                driver.find_element_by_link_text('Load More').click()
            except:
                print('wrong button')
                try:
                    driver.refresh()
                    time.sleep(10)
                    driver.find_element_by_link_text('Load More').click()
                except:
                    flag = False
    except:
        return

def findAllShoes(driver):
    time.sleep(10)
    shoes = driver.find_elements_by_class_name('name-link')

    wd = writeData()
    for shoe in shoes:
        data=(shoe.text.replace('\n',''), shoe.get_attribute('href'))
        wd.openFileOrCreateFileHibbett('baseData.csv', data)
        print(shoe.get_attribute('href'))
        print(shoe.text)

def main():
    driver = webdriver.Safari()
    hibbett = driver.get('https://www.hibbett.com/men/mens-shoes/')
    loadAllShoes(driver)
    findAllShoes(driver)
    driver.close()

