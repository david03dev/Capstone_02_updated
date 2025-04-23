from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ForgotPasswordPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.NAME, "username")
        self.reset_button = (By.XPATH, "//button[@type='submit']")

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_input)
        ).send_keys(username)

    def click_reset(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.reset_button)
        ).click()

    def get_success_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h6[@class='oxd-text oxd-text--h6 orangehrm-forgot-password-title']"))
        ).text
