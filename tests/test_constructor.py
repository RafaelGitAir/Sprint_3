import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import sys
sys.path.append('..')
from locators import Locators as L
from support_func import SupportFunction

class TestConstractor:

    def test_constractor_surfing_to_filling_on_main_page_click_link_filling_filling_is_visible(self):
        sf = SupportFunction()
        sf.setup_class()
        sf.driver.get(L.MAIN_PAGE_URL)
        WebDriverWait(sf.driver, 3).until(
            expected_conditions.element_to_be_clickable(L.BUTTON_LOGIN_MAIN_PAGE_LOCATOR))
        element = sf.driver.find_element(*L.LINK_FIRST_FILLING_IN_LIST_LOCATOR)
        sf.driver.find_element(*L.LINK_FILLING).click()
        time.sleep(2)

        assert sf.is_element_in_viewport(sf.driver, element)
        sf.teardown_class()

    def test_constractor_surfing_to_sauce_on_main_page_click_link_sauce_sauce_is_visible(self):
        sf = SupportFunction()
        sf.setup_class()
        sf.driver.get(L.MAIN_PAGE_URL)
        WebDriverWait(sf.driver, 3).until(
            expected_conditions.element_to_be_clickable(L.BUTTON_LOGIN_MAIN_PAGE_LOCATOR))
        sf.driver.find_element(*L.LINK_FILLING).click()
        time.sleep(1)
        sf.driver.find_element(*L.LINK_SAUCE).click()
        element = sf.driver.find_element(*L.LINK_FIRST_SAUCE_IN_LIST_LOCATOR)
        time.sleep(2)

        assert sf.is_element_in_viewport(sf.driver, element)
        sf.teardown_class()

    def test_constractor_surfing_to_buns_on_main_page_click_link_buns_buns_is_visible(self):
        sf = SupportFunction()
        sf.setup_class()
        sf.driver.get(L.MAIN_PAGE_URL)
        WebDriverWait(sf.driver, 3).until(
            expected_conditions.element_to_be_clickable(L.BUTTON_LOGIN_MAIN_PAGE_LOCATOR))
        sf.driver.find_element(*L.LINK_FILLING).click()
        time.sleep(1)
        sf.driver.find_element(*L.LINK_BUNS).click()
        element = sf.driver.find_element(*L.LINK_FIRST_BUN_IN_LIST_LOCATOR)
        time.sleep(2)

        assert sf.is_element_in_viewport(sf.driver, element)
        sf.teardown_class()




