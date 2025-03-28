import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import sys
sys.path.append('..')
from locators import Locators as L
from support_func import SupportFunction


class TestLogout:
    def test_logout_from_profile_correct_log_and_pass_login_page(self, login_password):
        sf = SupportFunction()
        sf.setup_class()
        sf.driver.get(L.MAIN_PAGE_URL)
        WebDriverWait(sf.driver, 3).until(
            expected_conditions.element_to_be_clickable(L.BUTTON_LOGIN_MAIN_PAGE_LOCATOR))
        sf.driver.find_element(*L.BUTTON_PERSONAL_ACCOUNT_LOCATOR).click()
        sf.enter_email_password(login_password)
        WebDriverWait(sf.driver, 3).until(expected_conditions.element_to_be_clickable(L.BUTTON_TAKE_ORDER_LOCATOR))
        sf.driver.find_element(*L.BUTTON_PERSONAL_ACCOUNT_LOCATOR).click()
        WebDriverWait(sf.driver, 3).until(expected_conditions.element_to_be_clickable(L.BUTTON_EXIT))
        sf.driver.find_element(*L.BUTTON_EXIT).click()
        WebDriverWait(sf.driver, 3).until(expected_conditions.element_to_be_clickable(L.BUTTON_LOGIN_PAGE_LOCATOR))
        cr_url = sf.driver.current_url
        sf.teardown_class()

        assert cr_url == L.LOGIN_URL

