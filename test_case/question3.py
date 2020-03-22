import time

from selenium.webdriver.common.keys import Keys


from selenium import webdriver
driver = webdriver.Chrome(executable_path=r'C:\Users\shyam raj\untitled\atcost\drivers\chromedriver.exe')
from selenium.webdriver import ActionChains

driver.get('http://atcost.in/')

driver.set_page_load_timeout(30)
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(3)
def menubar():

    driver.find_element_by_xpath('//html[@dir="ltr"]').send_keys(Keys.PAGE_DOWN)
    actions=ActionChains(driver)
    atcostinhouse=driver.find_element_by_xpath('(//a[@class="sub_trigger"])[2]')
    fifthelement=driver.find_element_by_xpath("(//div[@class='wrapper'])[2]//li[5]")
    actions.move_to_element(atcostinhouse).move_to_element(fifthelement).click().perform()
    driver.find_element_by_xpath('(//button[text()="Add to Cart"])[1]').click()

menubar()

