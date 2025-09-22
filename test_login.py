import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from LoginPage import LoginPage
from ForgotPasswordPage import ForgotPasswordPage

class TestLogin:
    def setup(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def test_forgot_password(self):
        login_page = LoginPage(self.driver)
        forgot_password_page = ForgotPasswordPage(self.driver)

        # Step 1: Click Forgot Password
        login_page.click_forgot_password()

        # Step 2: Enter Username
        forgot_password_page.enter_username("david")

        # Step 3: Click Reset Password
        forgot_password_page.click_reset()

        # Step 4: Verify Success Message
        success_message = forgot_password_page.get_success_message()
        assert "Reset Password link sent successfully", success_message

    def teardown(self):
        self.driver.quit()

