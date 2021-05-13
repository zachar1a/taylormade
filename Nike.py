from selenium import webdriver
from Scrappers import Nike


def main():
    driver = webdriver.Safari()
    print('test')
    Nike.main(driver)


driver.close()
