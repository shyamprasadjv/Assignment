from selenium import webdriver
import openpyxl
driver=webdriver.Chrome(executable_path=r"")
driver.find_element_by_xpath()
path=r""
workbook=openpyxl.load_workbook(path)

sheet=workbook.active
for r in range(1,r+1):
    for c in range(1,c+1):
        sheet.cell(row=r,column=c).value="caseid"

workbook.save(path)



driver.find_element_by_xpath('//div[#@class=""//pre[@xpath]').__getattribute__("value")#get_text()


