import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.service import Service

from pageObjects.HomePage import HomePage
from utilites.baseClass import BaseClass
from TestData.HomePageData import HomePageData


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("first name is "+ getData["firstname"])
        homePage.getName().send_keys(getData["firstname"])
        time.sleep(1)
        homePage.getEmail().send_keys(getData["lastname"])
        time.sleep(1)
        homePage.getCheckBox().click()
        time.sleep(1)
        self.selectOptionByText(homePage.getGender(),getData["gender"])
        time.sleep(1)
        homePage.submitForm().click()
        alertText = homePage.getSuccessMessage().text
        time.sleep(5)
        assert ("Success" in alertText)
        self.driver.refresh()

    #       print("It's OKAY")
# Run file in command line -> pytest test_HomePage.py -s
# Run file in command line -> py.test --html=report.html

    @pytest.fixture(params= HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param

