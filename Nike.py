from selenium import webdriver
from Scrappers import Nike


def main():
    driver = webdriver.Safari()
    Nike.main(driver)


main()

driver.close()

