from selenium.webdriver.common.by import By


class Locators:
    REGISTER_URL = 'https://stellarburgers.nomoreparties.site/register'
    LOGIN_URL = 'https://stellarburgers.nomoreparties.site/login'
    MAIN_PAGE_URL = 'https://stellarburgers.nomoreparties.site/'
    FORGOT_PASSWORD_PASSWORD_URL = 'https://stellarburgers.nomoreparties.site/forgot-password'
    PROFILE_URL = 'https://stellarburgers.nomoreparties.site/account/profile'
    USERNAME_INPUT_LOCATOR = (By.XPATH, "//label[text()='Имя']/parent::div/input")
    EMAIL_INPUT_LOCATOR = (By.XPATH, "//label[text()='Email']/parent::div/input")
    PASSWORD_INPUT_LOCATOR = (By.XPATH, "//label[text()='Пароль']/parent::div/input")
    BUTTON_REGISTER_LOCATOR = (By.XPATH, "//button[text()='Зарегистрироваться']")
    BUTTON_LOGIN_PAGE_LOCATOR = (By.XPATH, "//button[text()='Войти']")
    BUTTON_TAKE_ORDER_LOCATOR = (By.XPATH, "// button[text() = 'Оформить заказ']")
    TEXT_INCORRECT_PASSWORD_LOCATOR = (By.XPATH, '//p[text()="Некорректный пароль"]')
    BUTTON_LOGIN_MAIN_PAGE_LOCATOR = (By.XPATH, "//button[text()='Войти в аккаунт']")
    BUTTON_PERSONAL_ACCOUNT_LOCATOR = (By.XPATH, "//p[text()='Личный Кабинет']")
    LINK_LOGIN_ON_REGISTER_PAGE_LOCATOR = (By.XPATH, "//p[text()='Уже зарегистрированы?']//a[text()='Войти']")
    Button_RECOVER = (By.XPATH, "//button[text()='Восстановить']")
    LINK_LOGIN_ON_FORGOT_PASSWORD_PAGE_LOCATOR = (By.XPATH, "//p[text()='Вспомнили пароль?']//a[text()='Войти']")
    BUTTON_EXIT = (By.XPATH, "//button[text()='Выход']")
    LINK_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")
    LINK_LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']//a[@href='/']")
    LINK_FILLING = (By.XPATH, "//span[text()='Начинки']")
    LINK_FIRST_FILLING_IN_LIST_LOCATOR = (By.XPATH, "//p[text()='Мясо бессмертных моллюсков Protostomia']")
    LINK_SAUCE = (By.XPATH, "//span[text()='Соусы']")
    LINK_FIRST_SAUCE_IN_LIST_LOCATOR = (By.XPATH, "//p[text()='Соус Spicy-X']")
    LINK_BUNS = (By.XPATH, "//span[text()='Булки']")
    LINK_FIRST_BUN_IN_LIST_LOCATOR = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")




