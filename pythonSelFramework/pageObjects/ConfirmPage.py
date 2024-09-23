import selenium.webdriver
from selenium.webdriver.common.by import By
#from pageObjects.CheckOutPage import CheckOutPage

class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    country = (By.ID,"country")
    countryList = (By.LINK_TEXT, "India")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchaseButton = (By.CSS_SELECTOR, "[type='submit']")
    messageSuccess = (By.CSS_SELECTOR, "[class*='alert-success']")

    def getCountryList(self):
        return self.driver.find_element(*ConfirmPage.country)

    def getIndiaLink(self):
        return self.driver.find_element(*ConfirmPage.countryList)

    def checkAgree(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def submitPurchase(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)

    def displayMessage(self):
        return self.driver.find_element(*ConfirmPage.messageSuccess)
