from selenium import webdriver
import time

driver = webdriver.Safari()

hibbett = driver.get('https://www.hibbett.com/men/mens-shoes/')

time.sleep(5)

flag = True
while(driver.find_element_by_link_text('Load More') and flag):
    time.sleep(2)
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

time.sleep(10)
shoes = driver.find_elements_by_class_name('name-link')
for shoe in shoes:
    print(shoe.text)
