import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import sys
sys.path.append('..')
from locators import Locators as L
from generate_name_email_password import GenerateNameEmailPassword


class TestRegester:

    def setup_class(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def teardown_class(cls):
        cls.driver.quit()

    def test_register_input_correct_log_pass_email_user_is_registered(self):
        self.setup_class()
        self.driver.get(L.REGISTER_URL)
        generator = GenerateNameEmailPassword()
        name = generator.gerate_name()
        email = generator.generate_email(name)
        password = generator.generate_password()
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(L.BUTTON_REGISTER_LOCATOR))
        self.driver.find_element(*L.USERNAME_INPUT_LOCATOR).send_keys(name)
        self.driver.find_element(*L.EMAIL_INPUT_LOCATOR).send_keys(email)
        self.driver.find_element(*L.PASSWORD_INPUT_LOCATOR).send_keys(password)
        self.driver.find_element(*L.BUTTON_REGISTER_LOCATOR).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(L.BUTTON_LOGIN_PAGE_LOCATOR))
        self.driver.find_element(*L.EMAIL_INPUT_LOCATOR).send_keys(email)
        self.driver.find_element(*L.PASSWORD_INPUT_LOCATOR).send_keys(password)
        self.driver.find_element(*L.BUTTON_LOGIN_PAGE_LOCATOR).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(L.BUTTON_TAKE_ORDER_LOCATOR))
        text_take_order = self.driver.find_element(*L.BUTTON_TAKE_ORDER_LOCATOR).text
        self.teardown_class()

        assert text_take_order == 'Оформить заказ'

    incorrect_password_case = ['1', 'ff', 'sdf', 'a23f', 'a/65$']

    @pytest.mark.parametrize('incorrect_password', incorrect_password_case)
    def test_register_input_wrong_password_error_massage(self, incorrect_password):
        self.setup_class()
        self.driver.get(L.REGISTER_URL)
        generator = GenerateNameEmailPassword()
        name = generator.gerate_name()
        email = generator.generate_email(name)
        password = incorrect_password
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(L.BUTTON_REGISTER_LOCATOR))
        self.driver.find_element(*L.USERNAME_INPUT_LOCATOR).send_keys(name)
        self.driver.find_element(*L.EMAIL_INPUT_LOCATOR).send_keys(email)
        self.driver.find_element(*L.PASSWORD_INPUT_LOCATOR).send_keys(password)
        self.driver.find_element(*L.BUTTON_REGISTER_LOCATOR).click()
        incorrect_massage = self.driver.find_element(*L.TEXT_INCORRECT_PASSWORD_LOCATOR).text
        self.teardown_class()

        assert incorrect_massage == 'Некорректный пароль'
