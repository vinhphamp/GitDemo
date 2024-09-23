import selenium.webdriver
from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage_objects import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkoutPrimaryButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooters(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def checkOutPrimary(self):
        return self.driver.find_element(*CheckOutPage.checkoutPrimaryButton)

    def checkOutItems(self):
        self.driver.find_element(*CheckOutPage.checkOut).click()
        confirm = ConfirmPage(self.driver)
        return confirm
