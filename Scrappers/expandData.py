from selenium import webdriver
import csv, time, os, pathlib
import pandas as pd
from .writeData import writeData




class expandData:


    def __init__(self):
        self.initPath = os.getcwd()
        self.pathToBrandData = 'Brand Data/'
        self.resetPath = '../../'


    def getCsvData(self, brand, fileName):
        '''
        Checks if specified file is in a specified dir
        then reads in the csv data. The files used are
        auto generated with Shoe and Link columns
        '''

        data = []
        if brand in os.listdir(self.pathToBrandData):
            if fileName in os.listdir(self.pathToBrandData + brand):
                os.chdir(self.pathToBrandData + brand)
                with open(fileName, 'r') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        data.append(
                                {'Shoe':row['Shoe'],
                                    'Link':row['Link']
                                    })

                    os.chdir(self.resetPath)
                    return data


    def writeToFile(self, brand, fileName, data):
        '''
        Writes data to specified file in speficied dir
        the files have columns Shoe, Sizes and Colorways
        The Sizes and Colorways are both arrays
        '''

        print(os.getcwd())
        if os.getcwd() == str(self.initPath) + 'Brand Data/Nike':
            os.chdir(self.resetPath)
        if brand in os.listdir(self.pathToBrandData):
            if fileName in os.listdir(self.pathToBrandData + brand):
                os.chdir(self.pathToBrandData + brand)
                wd = writeData()
                wd.writeToFile(fileName,data)
                os.chdir(self.resetPath)
            else:
                os.chdir(self.pathToBrandData + brand)
                with open(fileName, 'a', newline='') as file:
                    csv.writer(file).writerow(['Shoe', 'Sizes', 'Colorways', 'MSRP'])
                    file.close()
                    self.writeToFile('Nike',fileName, data)
                os.chdir(self.resetPath)

    def getShoeDetails(self, driver, brand, fileName, shoeLink):
        '''
        Scrapes data from specified url, the data we are getting
        are Colorways and Sizes
        '''

        driver.get(shoeLink)

        #name = driver.find_element_by_xpath('//*[@id="pdp_product_title"]').text
        time.sleep(2)
        try:
            if driver.find_element_by_class_name('not-found').text == 'THE PRODUCT YOU ARE LOOKING FOR IS NO LONGER AVAILABLE':
                print('in try')
                return
        except:
            print('in except')
            pass


        try:
            name = driver.find_element_by_id('pdp_product_title').text
        except:
            name = shoeLink
        sizes = []
        colorways = []
        
        size = driver.find_elements_by_class_name('css-xf3ahq')
        try:
            colorWay = driver.find_element_by_class_name('colorway-images').find_elements_by_tag_name('a')
            for c in colorWay:
                print(c.get_attribute('href').split('/')[-1])
                colorways.append(c.get_attribute('href').split('/')[-1]) 
        except:
            try:
                colorways.append(driver.find_element_by_class_name('description-preview__style-color').text)
            except:
                colorways = []

        for s in size:
            print(s.text)
            sizes.append(s.text)

        try:
            price = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/div[1]/div[2]/div/section[1]/div[2]/aside/div/div[1]/div[1]').text
            print(price)
        except:
            price = driver.find_element_by_xpath('//*[@id="PDP"]/div/div[3]/div[1]/div[1]/div/div[1]/div[2]/div/div').text
            print(price)

        data = (name, sizes, colorways, price)
        self.writeToFile(brand, fileName, data)

    def syncFiles(self):
        expandedData = pd.read_csv('Brand Data/Nike/Nike.csv')
        baseData     = pd.read_csv('Brand Data/Nike/baseData.csv')
        baseData['MSRP'] = expandedData['MSRP']
        baseData.to_csv('Brand Data/Nike/baseData.csv')
