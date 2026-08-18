import helpers
import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages import UrbanRoutesPage


class TestUrbanRoutes:

driver = None
page = None

@classmethod
def setup_class(cls):
chrome_options = Options()
chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
cls.driver.implicitly_wait(10)
cls.page = UrbanRoutesPage(cls.driver)

def setup_method(self):
self.driver.get(data.URBAN_ROUTES_URL)

def _prepare_route_and_plan(self):
self.page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
self.page.select_supportive_plan()

def _prepare_phone(self):
self._prepare_route_and_plan()
self.page.set_phone(data.PHONE_NUMBER)

def _prepare_card(self):
self._prepare_phone()
self.page.set_card(data.CARD_NUMBER, data.CARD_CODE)

def test_set_route(self):
self.page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
assert self.page.get_from() == data.ADDRESS_FROM
assert self.page.get_to() == data.ADDRESS_TO

def test_select_plan(self):
self.page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
self.page.select_supportive_plan()
assert self.page.get_current_selected_plan() == "Comfort"

def test_fill_phone_number(self):
self._prepare_route_and_plan()
self.page.set_phone(data.PHONE_NUMBER)
assert self.page.get_phone() == data.PHONE_NUMBER

def test_fill_card(self):
self._prepare_phone()
self.page.set_card(data.CARD_NUMBER, data.CARD_CODE)
assert self.page.get_current_payment_method() == "Cartão"

def test_comment_for_driver(self):
self._prepare_route_and_plan()
self.page.set_message_for_driver(data.MESSAGE_FOR_DRIVER)
assert self.page.get_message_for_driver() == data.MESSAGE_FOR_DRIVER

def test_order_blanket_and_handkerchiefs(self):
self._prepare_route_and_plan()
self.page.click_blanket_and_handkerchiefs_option()
assert self.page.get_blanket_and_handkerchiefs_option_checked()

def test_order_2_ice_creams(self):
self._prepare_route_and_plan()
self.page.add_ice_cream(2)
assert self.page.get_amount_of_ice_cream() == 2

def test_car_search_model_appears(self):
self._prepare_card()
self.page.set_message_for_driver(data.MESSAGE_FOR_DRIVER)
self.page.click_order_taxi_buton()
assert self.page.wait_order_taxi_popup()

def test_driver_info_appears(self):
self._prepare_card()
self.page.set_message_for_driver(data.MESSAGE_FOR_DRIVER)
self.page.click_order_taxi_buton()
self.page.wait_driver_info()
name, rating, image = self.page.get_driver_info()
assert name
assert rating
assert image

@classmethod
def teardown_class(cls):
if cls.driver:
cls.driver.quit()
