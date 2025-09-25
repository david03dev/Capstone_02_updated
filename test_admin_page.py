import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        admin_page = AdminPage()
        #admin_page.validate_title()
        assert driver.title == admin_page.page_title

        # Step 2: Validate Admin Options
        all_options = [
            admin_page.user_management, admin_page.job, admin_page.organization, admin_page.qualifications,
            admin_page.nationalities, admin_page.corporate, admin_page.configuration
        ]
        for option in all_options:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(option)
            )

        # Step 3: Validate All menu in admin page
        all_menu = [
            admin_page.PIM, admin_page.Leave, admin_page.Time, admin_page.Recruitment,admin_page.my_info, admin_page.Performance,
            admin_page.Dashboard, admin_page.Directory, admin_page.Maintenance, admin_page.Buzz
        ]
        for menu in all_menu:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(menu)
            )
