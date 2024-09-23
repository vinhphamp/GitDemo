import logging
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
from pageObjects.CheckOutPage_objects import CheckOutPage
from pageObjects.HomePage_objects import HomePage
from pageObjects.ConfirmPage_objects import ConfirmPage

class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        # Create object for each class name
        homePage = HomePage(self.driver)
        checkout = homePage.shopItems() # shopItems method call the last action to redirect to new page
        # checkout object will be created to continue the next action of new page
        log.info("Getting all the card titles")

        time.sleep(1)

        # Create object for each class name
        # checkout = CheckOutPage(self.driver)
        cards = checkout.getCardTitles()

        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkout.getCardFooters()[i].click()
        time.sleep(1)

        # Click on Checkout button primary go to Cart List of Items
        checkout.checkOutPrimary().click()

        # Click on Checkout button success to go to Confirm page
        confirm = checkout.checkOutItems() # checkOutItems method call the last action to redirect to new page
        # confirm object will be created to continue the next action of new page
        log.info("Entering country name as ind")

        time.sleep(1)

        # Create object for each class name
        # confirm = ConfirmPage(self.driver)

        # Input 'ind' to get suggestion list of countries
        confirm.getCountryList().send_keys("ind")
        time.sleep(5)

        # element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
        # element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(confirm.countryList))
        self.verifyLinkPresence("India")

        # getIndiaLink
        # self.driver.find_element(By.LINK_TEXT, "India").click()
        confirm.getIndiaLink().click()
        time.sleep(1)

        # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        confirm.checkAgree().click()
        time.sleep(1)

        # self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        confirm.submitPurchase().click()
        time.sleep(1)

        textMatch = confirm.displayMessage().text
        # textMatch = self.driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text
        # textMatch = ConfirmPage.messageSuccess().text
        log.info("Text received from application is " +textMatch)

        assert ("Success! Thank you!" in textMatch)
        print(textMatch)
        print("Completed without bug")

# Run file in command line -> pytest test_HomePage.py -s
# Run file in command line -> py.test --html=report.html

