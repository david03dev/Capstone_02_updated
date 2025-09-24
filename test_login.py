import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from LoginPage import LoginPage
from ForgotPasswordPage import ForgotPasswordPage

@pytest.fixture()
def setup_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    yield driver
    driver.quit()


class TestLogin:

    def test_forgot_password(self,setup_driver):
        driver = setup_driver
        forgot_password_page = ForgotPasswordPage(driver)
        login_page = LoginPage(driver)

        # Step 1: Click Forgot Password
        login_page.click_forgot_password()

        # Step 2: Enter Username
        forgot_password_page.enter_username("admin")

        # Step 3: Click Reset Password
        forgot_password_page.click_reset()

        # Step 4: Verify Success Message
        success_message = forgot_password_page.get_success_message()
        assert "Reset Password link sent successfully" == success_message,"Reset password - Successful"
        #Reset Password link sent successfully


