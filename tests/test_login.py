import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import sys
sys.path.append('..')
from locators import Locators as L

class TestLogin:

    def setup_class(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def teardown_class(cls):
        cls.driver.quit()

    def get_text_take_order(cls):
        WebDriverWait(cls.driver, 3).until(expected_conditions.element_to_be_clickable(L.BUTTON_TAKE_ORDER_LOCATOR))
        return cls.driver.find_element(*L.BUTTON_TAKE_ORDER_LOCATOR).text

    def enter_email_password(self, login_password):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(L.BUTTON_LOGIN_PAGE_LOCATOR))
        self.driver.find_element(*L.EMAIL_INPUT_LOCATOR).send_keys(login_password['email'])
        self.driver.find_element(*L.PASSWORD_INPUT_LOCATOR).send_keys(login_password['password'])
        self.driver.find_element(*L.BUTTON_LOGIN_PAGE_LOCATOR).click()


    def test_login_button_login_on_main_page_correct_log_and_pass_user_logged_in(self, login_password):
        self.setup_class()
        self.driver.get(L.MAIN_PAGE_URL)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(L.BUTTON_LOGIN_MAIN_PAGE_LOCATOR))
        self.driver.find_element(*L.BUTTON_LOGIN_MAIN_PAGE_LOCATOR).click()
        self.enter_email_password(login_password)
        text_take_order = self.get_text_take_order()
        self.teardown_class()

        assert text_take_order == 'Оформить заказ'

    def test_login_button_login_in_personal_account_correct_log_and_pass_user_logged_in(self, login_password):
        self.setup_class()
        self.driver.get(L.MAIN_PAGE_URL)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(L.BUTTON_LOGIN_MAIN_PAGE_LOCATOR))
        self.driver.find_element(*L.BUTTON_PERSONAL_ACCOUNT_LOCATOR).click()
        self.enter_email_password(login_password)
        text_take_order = self.get_text_take_order()
        self.teardown_class()

        assert text_take_order == 'Оформить заказ'

    def test_login_link_login_on_page_register_correct_log_and_pass_user_logged_in(self, login_password):
        self.setup_class()
        self.driver.get(L.REGISTER_URL)
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(L.BUTTON_REGISTER_LOCATOR))
        link_login = self.driver.find_element(*L.LINK_LOGIN_ON_REGISTER_PAGE_LOCATOR)
        self.driver.execute_script("arguments[0].scrollIntoView();", link_login)
        link_login.click()
        self.enter_email_password(login_password)
        text_take_order = self.get_text_take_order()
        self.teardown_class()

        assert text_take_order == 'Оформить заказ'

    def test_login_link_login_on_page_forgot_password_correct_log_and_pass_user_logged_in(self, login_password):
        self.setup_class()
        self.driver.get(L.FORGOT_PASSWORD_PASSWORD_URL)
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(L.Button_RECOVER))
        self.driver.find_element(*L.LINK_LOGIN_ON_FORGOT_PASSWORD_PAGE_LOCATOR).click()
        self.enter_email_password(login_password)
        text_take_order = self.get_text_take_order()
        self.teardown_class()

        assert text_take_order == 'Оформить заказ'




















