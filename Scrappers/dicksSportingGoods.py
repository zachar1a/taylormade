from selenium import webdriver
import json, time, csv, os, pathlib
from .writeData import writeData
from .expandData import expandData

'''
    This file needs to get done tomorrow
'''

def findShoesOnPage(driver, url):
    driver.get(url)
    shoes = driver.find_elements_by_class_name('rs_product_description')
    for shoe in shoes:
        print(shoe.text)

def main():
    driver = webdriver.Safari()

    os.chdir(pathlib.Path(__file__).parent.absolute())

    try:
        os.listdir('Brand Data/')
    except:
        os.mkdir('Brand Data/')


    try:
        os.listdir('Brand Data/Dicks Sporting Goods/')
    except:
        os.mkdir('Brand Data/Dicks Sporting Goods/')

    lifestyle= 'https://www.dickssportinggoods.com/f/mens-athletic-shoes'

    findShoesOnPage(driver, lifestyle)
