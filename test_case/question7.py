import time

from selenium.webdriver.common.keys import Keys


from selenium import webdriver
driver = webdriver.Chrome(executable_path=r'C:\Users\shyam raj\untitled\atcost\drivers\chromedriver.exe')


driver.get('http://atcost.in/')

driver.set_page_load_timeout(30)
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(3)

def product():
    driver.find_element_by_xpath('(//input[@type="text"])[1]').send_keys("paneer")
    driver.find_element_by_xpath('//i[@class="icon-search button-search hover_icon"]').click()
    driver.find_element_by_xpath('//a[text()="Kohinoor Punjabi Paneer Butter Masala 15g"]').click()
    description=driver.find_element_by_xpath('//a[text()="Description"]').click()
    print('the product dispcription is',description)
product()


