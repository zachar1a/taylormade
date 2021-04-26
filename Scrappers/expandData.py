from selenium import webdriver
import csv, time, os
from writeData import writeData


class expandData:
    def __init__(self):
        self.pathToBrandData = '../Brand Data/'
        self.resetPath = '../../Scrappers/'

    def getCsvData(self, brand, fileName):
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
        if brand in os.listdir(self.pathToBrandData):
            if fileName in os.listdir(self.pathToBrandData + brand):
                os.chdir(self.pathToBrandData + brand)
                wd = writeData()
                wd.writeToFile(fileName,data)
                os.chdir(self.resetPath)
            else:
                os.chdir(self.pathToBrandData + brand)
                with open(fileName, 'a', newline='') as file:
                    csv.writer(file).writerow(['Shoe', 'Sizes', 'Colorways'])
                    file.close()
                    self.writeToFile('Nike',fileName, data)


    def getShoeDetails(self, driver, brand, fileName, shoeLink):
        driver.get(shoeLink)

        name = driver.find_element_by_id('pdp_product_title').text
        sizes = []
        colorways = []
        
        size = driver.find_elements_by_class_name('css-xf3ahq')
        try:
            colorWay = driver.find_element_by_class_name('colorway-images').find_elements_by_tag_name('a')
            for c in colorWay:
                print(c.get_attribute('href').split('/')[-1])
                colorways.append(c.get_attribute('href').split('/')[-1]) 
        except:
            colorways.append(driver.find_element_by_class_name('description-preview__style-color').text)

        for s in size:
            print(s.text)
            sizes.append(s.text)

        data = (name, sizes, colorways)
        self.writeToFile(brand, fileName, data)


