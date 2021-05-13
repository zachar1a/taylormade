from selenium import webdriver
#from .writeData import writeData
import time, csv, os, pathlib
import functools



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

def loadCSVData(fileName):
    with open(fileName, 'r') as file:
        reader = csv.DictReader(file)
        csvData = []
        for row in reader:
            csvData.append(row['Shoe'])
        return csvData

def writeToFile(fileName, data):
    currShoes = loadCSVData(fileName)
    if data[0] in currShoes:
        return
    else:
        with open(fileName, 'a+', newline='') as file:
            csv.writer(file).writerow(data)
            file.close()


def openOrCreateFile(fileName, data):
    pathToHibbett = 'Brand Data/Hibbett'

    if fileName in os.listdir(pathToHibbett):
        os.chdir(pathToHibbett)
        writeToFile(fileName, data)
        os.chdir('../../')
    else:
        os.chdir(pathToHibbett)
        with open(fileName, 'a', newline='') as file:
            csv.writer(file).writerow(['Shoe','Link'])
            file.close()
        writeToFile(fileName, data)
        os.chdir('../../')

def findAllShoes(driver):
    time.sleep(10)
    shoes = driver.find_elements_by_class_name('name-link')

    for shoe in shoes:
        data=(shoe.text.replace('\n',''), shoe.get_attribute('href'))
        print(data[0])
        print(data[1])
        openOrCreateFile('baseData.csv', data)

def main():
    driver = webdriver.Safari()

    os.chdir(pathlib.Path(__file__).parent.absolute())

    try:
        os.listdir('Brand Data/')
    except:
        os.mkdir('Brand Data/')

    try:
        os.listdir('Brand Data/Hibbett/')
    except:
        os.mkdir('Brand Data/Hibbett/')


    hibbett = driver.get('https://www.hibbett.com/men/mens-shoes/')
    #loadAllShoes(driver)
    findAllShoes(driver)
    driver.close()
