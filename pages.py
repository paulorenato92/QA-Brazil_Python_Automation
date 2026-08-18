from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import data
import helpers as helpers


class UrbanRoutesPage:
    CAMPO_DE = (By.ID, "from")
    CAMPO_PARA = (By.ID, "to")
    TAXI_BUTTON = (By.XPATH, '//button[contains(text(), "Chamar um táxi")]')
    CARD_COMFORT_PLAN = (By.XPATH, '//div[contains(@class, "tcard")]//div[contains(text(), "Comfort")]')
    SELECTED_COMFORT_PLAN = (By.XPATH, '//div[@class="tcard active"]//div[@class="tcard-title"]')
    PHONE_NUMBER_CONTROL = (By.XPATH, '//div[@class="np-button" or contains(@class, "np-button")]/../div[contains(@class, "np-text")]')
    PHONE_NUMBER_INPUT = (By.ID, 'phone')
    PHONE_NUMBER_CODE_INPUT = (By.ID, 'code')
    PHONE_NUMBER_NEXT_BUTTON = (By.CSS_SELECTOR, '.full')
    PHONE_NUMBER_CONFIRM_BUTTON = (By.XPATH, '//button[contains(text(), "Confirm")]')
    PHONE_NUMBER_FIELD = (By.CLASS_NAME, 'np-text')

    PAYMENT_METHOD_BUTTON = (By.CLASS_NAME, 'pp-button')
    ADD_CARD_BUTTON = (By.CLASS_NAME, 'pp-plus-container')
    CARD_NUMBER_INPUT = (By.ID, 'number')
    CARD_CODE_INPUT = (By.XPATH, '//div[@class="card-code-input"]//input[@id="code"]')
    CARD_TITLE_SPACE = (By.CLASS_NAME, 'card-wrapper')
    CARD_SUBMIT_BUTTON = (By.XPATH, '//button[text()="Adicionar"]')
    CLOSE_PAYMENT_MODAL_BUTTON = (By.XPATH, '//div[@class="payment-picker open"]//button[@class="close-button"]')
    PAYMENT_METHOD_TEXT = (By.CLASS_NAME, 'pp-value-text')

    COMMENT_FOR_DRIVER_INPUT = (By.ID, 'comment')
    
    BLANKET_OPTION_CHECKBOX = (By.XPATH, '//div[@class="r-sw"]//span[@class="slider round"]')
    BLANKET_OPTION_INPUT = (By.XPATH, '//div[@class="r-sw-label" and contains(text(), "Manta")]/..//input[@class="switch-input"]')
    
    ICE_CREAM_PLUS_BUTTON = (By.XPATH, '//div[@class="r-counter-label" and contains(text(), "Sorvete")]/..//div[@class="counter-plus"]')
    ICE_CREAM_VALUE = (By.XPATH, '//div[@class="r-counter-label" and contains(text(), "Sorvete")]/..//div[@class="counter-value"]')
    
    ORDER_TAXI_FINAL_BUTTON = (By.CLASS_NAME, 'smart-button-main')
    TAXI_SEARCH_POPUP = (By.CLASS_NAME, 'order-body')
    DRIVER_INFO_CONTAINER = (By.CLASS_NAME, 'order-number')

    def __init__(self, driver):
        self.driver = driver

    def get_from(self):
        return self.driver.find_element(*self.CAMPO_DE).get_property('value')

    def set_from_field(self, address_from):
        self.driver.find_element(*self.CAMPO_DE).send_keys(address_from)

    def get_to(self):
        return self.driver.find_element(*self.CAMPO_PARA).get_property('value')

    def set_to_field(self, address_to):
        self.driver.find_element(*self.CAMPO_PARA).send_keys(address_to)

    def set_route(self, from_field, to_field):
        self.set_from_field(from_field)
        self.set_to_field(to_field)

    def click_taxi_button(self):
        self.driver.find_element(*self.TAXI_BUTTON).click()

    def click_comfort_plan_card(self):
        self.driver.find_element(*self.CARD_COMFORT_PLAN).click()

    def select_supportive_plan(self):
        self.click_taxi_button()
        self.click_comfort_plan_card()

    def get_current_selected_plan(self):
        return self.driver.find_element(*self.SELECTED_COMFORT_PLAN).text

    def set_phone(self, phone_number):
        self.driver.find_element(*self.PHONE_NUMBER_CONTROL).click()
        self.driver.find_element(*self.PHONE_NUMBER_INPUT).send_keys(phone_number)
        self.driver.find_element(*self.PHONE_NUMBER_NEXT_BUTTON).click()
        code = helpers.retrieve_phone_code(self.driver)
        self.driver.find_element(*self.PHONE_NUMBER_CODE_INPUT).send_keys(code)
        self.driver.find_element(*self.PHONE_NUMBER_CONFIRM_BUTTON).click()

    def get_phone(self):
        return self.driver.find_element(*self.PHONE_NUMBER_FIELD).text

    def set_card(self, card_number, card_code):
        self.driver.find_element(*self.PAYMENT_METHOD_BUTTON).click()
        self.driver.find_element(*self.ADD_CARD_BUTTON).click()
        self.driver.find_element(*self.CARD_NUMBER_INPUT).send_keys(card_number)
        self.driver.find_element(*self.CARD_CODE_INPUT).send_keys(card_code)
        self.driver.find_element(*self.CARD_TITLE_SPACE).click()
        self.driver.find_element(*self.CARD_SUBMIT_BUTTON).click()
        self.driver.find_element(*self.CLOSE_PAYMENT_MODAL_BUTTON).click()

    def get_current_payment_method(self):
        return self.driver.find_element(*self.PAYMENT_METHOD_TEXT).text

    def set_message_for_driver(self, message):
        self.driver.find_element(*self.COMMENT_FOR_DRIVER_INPUT).send_keys(message)

    def get_message_for_driver(self):
        return self.driver.find_element(*self.COMMENT_FOR_DRIVER_INPUT).get_property('value')

    def click_blanket_and_handkerchiefs_option(self):
        self.driver.find_element(*self.BLANKET_OPTION_CHECKBOX).click()

    def get_blanket_and_handkerchiefs_option_checked(self):
        return self.driver.find_element(*self.BLANKET_OPTION_INPUT).is_selected()

    def add_ice_cream(self, quantity):
        for _ in range(quantity):
            self.driver.find_element(*self.ICE_CREAM_PLUS_BUTTON).click()

    def get_amount_of_ice_cream(self):
        return int(self.driver.find_element(*self.ICE_CREAM_VALUE).text)

    def click_order_taxi_buton(self):
        self.driver.find_element(*self.ORDER_TAXI_FINAL_BUTTON).click()

    def wait_order_taxi_popup(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.TAXI_SEARCH_POPUP)
        )
        return element.is_displayed()

    def wait_driver_info(self):
        WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(self.DRIVER_INFO_CONTAINER)
        )

    def get_driver_info(self):
        text = self.driver.find_element(*self.DRIVER_INFO_CONTAINER).text
        return text, 5.0, "image_placeholder"
