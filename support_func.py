from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators as L


class SupportFunction:
   def setup_class(cls):
      cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
      cls.driver.maximize_window()

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

   def is_element_in_viewport(self, dri, element):
      script = """
      var elem = arguments[0];
      var rect = elem.getBoundingClientRect();
      return (
          rect.top >= 0 &&
          rect.left >= 0 &&
          rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
          rect.right <= (window.innerWidth || document.documentElement.clientWidth)
      );
      """
      return dri.execute_script(script, element)
