import time

import allure

from onliner.locators.main_page_locators import *
from onliner.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    @allure.step('Step 1: Go to catalog')
    def catalog_click(self):
        self.click(CATALOG_SPAN)

    @allure.step('Step 2: Consent confirmation')
    def consent_button_click(self):
        self.click(CONSENT_BUTTON)

    @allure.step('Step 3: Go to electronika section')
    def electronika_section_click(self):
        self.click(SECTION)

    @allure.step('Step 4: Choose tablets and books')
    def tablets_books_section(self):
        self.click(SECTION_TABLETS_BOOKS)

    @allure.step('Step 5: Choose tablets')
    def tablets_section(self):
        self.click(SECTION_TABLETS)

    @allure.step('Step 10: Add to basket tablet iPad air 2022')
    def add_to_basket_click(self):
        self.click(LI_BASKET)

    @allure.step('Step 9: Get current price')
    def get_initial_price(self):
        price_element = self.driver.find_element(*INITIAL_PRICE)
        return price_element.text

    @allure.step('Step 11: Go to basket')
    def go_to_basket(self):
        self.click(GO_TO_BASKET)

    @allure.step('Step 12: Get basket price')
    def get_basket_price(self):
        basket_price = self.driver.find_element(*BASKET_PRICE)
        return basket_price.text

    def checkout_click(self):
        self.click(BU_CHECKOUT)

    @allure.step('Step 6: Select filter Apple')
    def checkbox_apple(self):
        c_apple = self.driver.find_element(*CHECKBOX_APPLE)
        self.driver.execute_script("window.scrollBy(0, 600);")
        c_apple.click()

    @allure.step('Step 7: Select filter Samsung')
    def checkbox_samsung(self):
        c_samsung = self.driver.find_element(*CHECKBOX_SAMSUNG)
        c_samsung.click()

    @allure.step('Step 8: Choose tablet apple iPad air 2022')
    def tablet_apple_ipad_air_2022(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
        self.click(TABLET_APPLE_IPAD_AIR_2022)







