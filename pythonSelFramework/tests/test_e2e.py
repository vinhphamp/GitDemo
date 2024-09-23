import time
# from lib2to3.pgen2 import driver

import pytest
import self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilites.baseClass import BaseClass
from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from pageObjects.ConfirmPage import ConfirmPage

# @pytest.mark.usefixtures("setup") -> inherit from BaseClass, no need to use this directly

class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.shopItems().click()
        log.info("getting all the card titles")
        time.sleep(1)

        checkoutpage = CheckOutPage(self.driver)
        cards = checkoutpage.getCardTitles()

        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutpage.getCardFooters()[i].click()

        time.sleep(1)

        # Click on Checkout button primary go to Cart List of Items
        checkoutpage.checkOutPrimary().click()

        #Click on Checkout button success to go to Confirm page
        checkoutpage.checkOutItems().click()
        log.info("Entering country name as")
        time.sleep(1)

        # Input 'ind' to get suggestion list of countries
        confirmPage = ConfirmPage(self.driver)
        time.sleep(1)
        confirmPage.getCountryList().send_keys("ind")

        time.sleep(5)

#        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
        self.verifyLinkPresence("India")

        # self.driver.find_element(By.LINK_TEXT, "India").click()
        confirmPage.getIndiaLink().click()

        #self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        confirmPage.checkAgree().click()

        # self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        confirmPage.submitPurchase().click()

        textMatch = self.driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text
        # textMatch = ConfirmPage.messageSuccess().text
        log.info(("Text received from application is" + textMatch))

        assert ("Success! Thank you Vinh!" in textMatch)

        print("Completed without bug")

# Run file in command line -> pytest test_HomePage.py -s
# Run file in command line -> py.test --html=report.html

