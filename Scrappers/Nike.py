from selenium import webdriver
import json, time, csv, os, pathlib
from .writeData import writeData
from .expandData import expandData



# This is a basic get request to stockX and in order
# for it to work we have to pass in a user-agent so
# that they won't detect that we are using an automated
# service

# this is page one of lifestyle shoes page. I am iterating over all of the shoes
# and then going to save the links and the images
# Need to put these into a database
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

def loadCSVData(fileName):
    with open(fileName, 'r') as file:
        reader = csv.DictReader(file)
        csvData = []
        for row in reader:
            csvData.append(row['Shoe'])
        return csvData


def writeToFile(fileName, data):
    '''
    Checks if file is in dir if not
    then creates it
    '''

    resetPath = '../../'
    pathToBrandData = 'Brand Data/'

    print(os.getcwd())
    if 'Nike' in os.listdir(pathToBrandData):
        if fileName in os.listdir(pathToBrandData + 'Nike'):
            os.chdir(pathToBrandData + 'Nike')

            currShoes = loadCSVData(fileName)
            if data[0] in currShoes:
                os.chdir(resetPath)
                return
            else:
                wd = writeData()
                wd.writeToFile(fileName,data)
        else:
            os.chdir(pathToBrandData + 'Nike')
            with open(fileName, 'a', newline='') as file:
                csv.writer(file).writerow(['Shoe', 'Link'])
                file.close()
                writeToFile(fileName, data)
    os.chdir(resetPath)

def findShoesOnPage(driver, url):
    driver.get(url) 

    goToBottom(driver)

    shoes = driver.find_elements_by_class_name('product-card__body')
    for shoe in shoes:
        link = shoe.find_element_by_class_name('product-card__link-overlay')
        print(link.text)
        print(link.get_attribute('href'))
        print('')
        data = (link.text, link.get_attribute('href'))
        writeToFile('baseData.csv',data)


def main():
    driver = webdriver.Safari()
    os.chdir(pathlib.Path(__file__).parent.absolute())

    # create Brand Data if it doesnt exist
    try:
        os.listdir('Brand Data/')
    except:
        os.mkdir('Brand Data/')

    # create Nike dir if it doesnt exist
    try:
        os.listdir('Brand Data/Nike/')
    except:
        os.mkdir('Brand Data/Nike/')


    #lifestyle = 'https://www.nike.com/w/mens-lifestyle-shoes-13jrmznik1zy7ok'
    jordan = 'https://www.nike.com/w/mens-jordan-shoes-37eefznik1zy7ok'
    #running = 'https://www.nike.com/w/mens-running-shoes-37v7jznik1zy7ok'
    #basketball = 'https://www.nike.com/w/mens-basketball-shoes-3glsmznik1zy7ok'

    #findShoesOnPage(driver,lifestyle)
    findShoesOnPage(driver,jordan)
    #findShoesOnPage(driver,running)
    #findShoesOnPage(driver,basketball)

    expand = expandData()
    print(os.getcwd())
    shoes = expand.getCsvData('Nike', 'baseData.csv')

    for shoe in shoes:
        print(shoe['Link'])
        expand.getShoeDetails(driver,'Nike', 'Nike.csv', shoe['Link'])
    driver.close()

if __name__ == '__main__':
    main()

