import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from LoginPage import LoginPage
from AdminPage import AdminPage

@pytest.fixture
def driver_setup():
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()

class TestAdminPage:

    def test_admin_page_header_validation(self,driver_setup):
        driver = driver_setup

        # Login as Admin
        login_page = LoginPage(driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()

        #open admin page
        login_page.click_admin_page()

        # Step 1: Validate Title
        admin_page = AdminPage(driver)
        #admin_page.validate_title()
        assert driver.title == admin_page.page_title

        # Step 2: Validate Admin Options
        #admin_page.validate_admin_options()
