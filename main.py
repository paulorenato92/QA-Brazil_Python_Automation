port helpers
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
        
        cls.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), 
            options=chrome_options
        )
        cls.driver.implicitly_wait(10)
        
        cls.page = UrbanRoutesPage(cls.driver)
        cls.driver.get(data.URBAN_ROUTES_URL)
        
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não é possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")

    @classmethod
    def teardown_class(cls):
        if cls.driver:
            cls.driver.quit()

    def test_set_route(self):
        address_from = data.ADDRESS_FROM
        address_to = data.ADDRESS_TO
        self.page.set_route(address_from, address_to)
        assert self.page.get_from() == address_from
        assert self.page.get_to() == address_to

    def test_select_plan(self):
        self.page.select_supportive_plan()
        assert self.page.get_current_selected_plan() == "Comfort"

    def test_fill_phone_number(self):
        phone_number = data.PHONE_NUMBER
        self.page.set_phone(phone_number)
        assert self.page.get_phone() == phone_number

    def test_fill_card(self):
        self.page.set_card(data.CARD_NUMBER, data.CARD_CODE)
        assert self.page.get_current_payment_method() == "Cartão"

    def test_comment_for_driver(self):
        message = data.MESSAGE_FOR_DRIVER
        self.page.set_message_for_driver(message)
        assert self.page.get_message_for_driver() == message

    def test_order_blanket_and_handkerchiefs(self):
        self.page.click_blanket_and_handkerchiefs_option()
        assert self.page.get_blanket_and_handkerchiefs_option_checked()

    def test_order_2_ice_creams(self):
        self.page.add_ice_cream(2)
        assert self.page.get_amount_of_ice_cream() == 2

    def test_car_search_model_appears(self):
        self.page.click_order_taxi_buton()
        assert self.page.wait_order_taxi_popup()

    def test_driver_info_appears(self):
        self.page.wait_driver_info()
        name, rating, image = self.page.get_driver_info()
        assert name is not None and name != ""
        assert rating is not None
        assert image

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
