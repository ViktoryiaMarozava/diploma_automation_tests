import time
import pytest
import allure

from onliner.pages.main_page import MainPage


@pytest.fixture(autouse=True)
def main_page(driver):
    yield MainPage(driver)


class TestTablets:

    @allure.description("The test looks for the product and puts it in the cart")
    def test_add_tablet_in_basket(self, main_page: MainPage):
        main_page.catalog_click()
        main_page.consent_button_click()
        main_page.electronika_section_click()
        main_page.tablets_books_section()
        main_page.tablets_section()
        main_page.checkbox_apple()
        time.sleep(3)
        main_page.checkbox_samsung()
        time.sleep(3)
        main_page.tablet_apple_ipad_air_2022()
        initial_price = main_page.get_initial_price()
        main_page.add_to_basket_click()
        main_page.go_to_basket()
        main_page.driver.implicitly_wait(10)
        basket_price = main_page.get_basket_price()
        assert f"{initial_price} р." == basket_price
        main_page.checkout_click()


