import selenium.webdriver
from selenium.webdriver.common.by import By
from pageObjects.CheckOutPage_objects import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkout = CheckOutPage(self.driver)
        return checkout
