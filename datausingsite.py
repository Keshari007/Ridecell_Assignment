from selenium import webdriver
import openpyxl
import pytest

class testgithub():

    @pytest.fixture()
    def setup(self):
        self.driver= webdriver.Chrome("C:/chromedriver.exe")
        self.driver.get("https://github.com/django")
        yield
        self.driver.quit()

    def testGithubDjango(self,setup):
        workbook= openpyxl.load_workbook("D:/Book1.xlsx")
        sheet = workbook.active
        self.driver.find_element_by_xpath("//*[@class='UnderlineNav-item selected']").click()
        m=self.driver.find_elements_by_xpath('//*[@itemprop="name codeRepository"]')
        a=[]
        for i in range(len(m)):
            a.append(m[i].text)
        a.sort()

        for i in range(len(a)):
            sheet.cell(row=i+1,column=1).value= a[i]
            workbook.save("D:/Book1.xlsx")




