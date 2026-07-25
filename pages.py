from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import data
import helpers as helpers


class UrbanRoutesPage:
    CAMPO_DE = By.ID, "from"
    CAMPO_PARA = By.ID, "to"
    TAXI_BUTTON = (By.XPATH, '//button[contains(text(), "Chamar um táxi")]')
    CARD_COMFORT_PLAN = (By.XPATH, '//div[contains(@class, "tcard")]//div[contains(text(), "Comfort")]')
    SELECTED_COMFORT_PLAN = (By.XPATH, '//div[@class="tcard active"]//div[@class="tcard-title"]')
    PHONE_NUMBER_CONTROL = (By.XPATH, '//div[@class="np-button" or contains(@class, "np-button")]/../div[contains(@class, "np-text")]')
    PHONE_NUMBER_INPUT = (By.ID, 'phone')
    PHONE_NUMBER_CODE_INPUT = (By.ID, 'code')
    PHONE_NUMBER_NEXT_BUTTON = (By.CSS_SELECTOR, '.full')
    PHONE_NUMBER_CONFIRM_BUTTON = (By.XPATH, '//button[contains(text(), "Confirm")]')
    PHONE_NUMBER = (By.CLASS_NAME, 'np-text')

def __init__(self, driver):
    self.driver = driver

def get_from_field(self):
    return self.driver.find_element(self.CAMPO_DE).get_property('value')

def set_from_field(self, adress_from):
        self.get_from_field().senf_keys(adress_from)

def get_to_field(self):
    return self.driver.find_element(self.CAMPO_PARA).get_property('value')

def set_to_field(self, adress_to):
    self.get_to_field().senf_keys(adress_to)

def set_route(self, from_field, to_field):
    self.set_from_field(from_field)
    self.set_to_field(to_field)

def assert_route(self, from_field, to_field):
    assert self.get_from_field() == from_field
    assert self.get_to_field() == to_field

def click_taxi_button(self):
    self.drive.find_element(self.TAXI_BUTTON).click()

def click_comfort_plan_card(self):
    self.driver.find_element(self.CARD_COMFORT_PLAN).click()

def select_comfort_plan(self):
    self.click_taxi_button()
    self.click_comfort_plan_card()

def assert_comfort_plan_selected(self):
    assert self.drive.find.element(self, SELECTED_COMFORT_PLAN).text == 'Comfort'

def set_phone(self, phone_number):
    self.driver.find_element(self.PHONE_NUMBER_CONTROL).click()
    self.driver.find_element(self.PHONE_NUMBER_INPUT).send_keys(phone_number)
    self.driver.find_element(self.PHONE_NUMBER_NEXT_BUTTON).click()
    code = helpers.retrieve_phone_code(self)
    self.driver.find_element(self.PHONE_NUMBER_CODE_INPUT).send_keys(code)
    self.driver.find_element(self.PHONER_NUMBER_CONFIRM_BUTTON).click()

def assert_phone_number(self, phone_number):
    assert self.driver.find_elements(self.PHONE_NUMBER).get_property('value') == phone_number
