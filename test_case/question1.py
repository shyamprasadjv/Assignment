from selenium import webdriver

driver=webdriver.Chrome(executable_path=r'C:\Users\shyam raj\untitled\atcost\drivers\chromedriver.exe')
driver.get('http://atcost.in/')
spantag=driver.find_elements_by_tag_name("span")
for i in spantag:
    targetelement=driver.find_element_by_xpath('//span[contains(text()="Contact.Jane.Doe"')
print(targetelement)








