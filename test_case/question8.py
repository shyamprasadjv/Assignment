from selenium import webdriver
driver=webdriver.Chrome(executable_path=r"C:\Users\shyam raj\untitled\atcost\drivers\chromedriver.exe")
driver.get()
rows=len(driver.find_elements_by_xpath('//tr[@class="ant-table-row-ant-table-row-level0"'))#this xpath gives the total matching data
columns=len(driver.find_elements_by_xpath('//th[@class="ant-table-head"'))
print(rows,columns)#by this we get you know structure of the table data
for r in range(1,rows+1):
    for c in range(1,columns+1):
        data=driver.find_element_by_xpath('//li[@class="ant-pagenation-item["+str(r)+"/tc["+str(c)+"')#iterate starts from row1
        print(data)
    print()

