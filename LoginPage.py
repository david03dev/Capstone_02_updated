from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")
        self.forgot_password_link = (By.XPATH, "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']")
        self.admin_page_link = (By.XPATH, "//span[contains(@class, 'oxd-main-menu-item--name') and text()='Admin']")

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_input)
        ).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.password_input)
        ).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        ).click()
        

    def click_forgot_password(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.forgot_password_link)
        ).click()

    def click_admin_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.admin_page_link)
        ).click()
