from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait



driver = webdriver.Safari()


def showDataTable(url):
    driver.get(url)
    driver.implicitly_wait(2)
    driver.find_element_by_xpath('//*[@id="market-summary"]/div[2]/div/div[2]/div[3]/button').click()


def find():
    driver.get('https://www.hibbett.com/men/mens-shoes/?start=0&sz=24')

    shoeList = driver.find_elements_by_class_name('name-link');
    for shoe in shoeList:
        print(shoe.text)

# find()
showDataTable('https://stockx.com/nike-blazer-mid-77-vintage-white-black')
#driver.close()
