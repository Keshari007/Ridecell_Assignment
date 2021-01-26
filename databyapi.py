from excelutils import readData,writeData
import requests
import pytest
import openpyxl

@pytest.fixture()
def setup(self):
    response=requests.get("https://api.github.com/users/django/repos")
    jsonobj= response.json()


workbook= openpyxl.load_workbook("D:/Book1.xlsx")
sheet = workbook.active

def test_reponame(self,setup):
    for i in range(len(self.jsonObj)):
        if (self.jsonobj[i]['name']== sheet.cell(row=i+1,column=1).value):
            print("The repo name is matching")
        else:
            print("repo name does not match")

