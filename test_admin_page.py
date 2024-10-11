import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from LoginPage import LoginPage
from AdminPage import AdminPage

class TestAdminPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()

        # Login as Admin
        login_page = LoginPage(self.driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()
        login_page.click_admin_page()

    def test_admin_page_header_validation(self):
        admin_page = AdminPage(self.driver)

        #open admin page
        
        # Step 1: Validate Title
        admin_page.validate_title()

        # Step 2: Validate Admin Options
        admin_page.validate_admin_options()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
