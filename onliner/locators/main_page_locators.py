from selenium.webdriver.common.by import By


CONSENT_BUTTON = By.XPATH, '//button[@class="fc-button fc-cta-consent fc-primary-button"]'

LI_BASKET = By.LINK_TEXT, "В корзину"

INITIAL_PRICE = By.XPATH, '//a[@class="product-aside__link product-aside__link_alter-other ' \
                          'product-aside__link_font-weight_bold product-aside__link_ellipsis product-aside__link_nodecor ' \
                          'js-short-price-link product-aside__link_huge-additional"]//span'

GO_TO_BASKET = By.XPATH, '//a[@class="button-style button-style_another button-style_base-alter ' \
                         'product-recommended__button"]'

BASKET_PRICE = By.XPATH, '//div[@class="cart-form__offers-part cart-form__offers-part_total"]//div[' \
                         '@class="cart-form__description cart-form__description_base-alter ' \
                         'cart-form__description_font-weight_semibold cart-form__description_ellipsis ' \
                         'cart-form__description_condensed"]//span'

BU_CHECKOUT = By.XPATH, '//a[@class="button-style button-style_small cart-form__button button-style_primary"]'

CATALOG_SPAN = By.LINK_TEXT, "Каталог"

SECTION = By.XPATH, "//ul[@class='catalog-navigation-classifier']//li//*[contains(text(), 'Электроника')]"

SECTION_TABLETS_BOOKS = By.XPATH, "//*[contains(text(),'Планшеты, электронные книги')]"

SECTION_TABLETS = By.XPATH, "//span[@class='catalog-navigation-list__dropdown-data']//*[contains(text(),'Планшеты')]"

CHECKBOX_APPLE = By.XPATH, "//div[@class='catalog-form__checkbox-text']//*[contains(text(),'Apple')]//..//..//..//..//label"

CHECKBOX_SAMSUNG = By.XPATH, "//div[@class='catalog-form__checkbox-text']//*[contains(text(),'Samsung')]//..//..//..//..//label"

TABLET_APPLE_IPAD_AIR_2022 = By.XPATH, "//div[@class='catalog-form__offers-part catalog-form__offers-part_data']//*[contains(text(),'Планшет Apple iPad Air 2022 64GB MM9C3 (серый космос)')]"