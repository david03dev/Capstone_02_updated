from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.page_title = "OrangeHRM"
        self.user_management = (By.XPATH, "//span[contains(text(), 'User Management')]") #//span[contains(text(), 'User Management')]
        self.job = (By.XPATH, "//li[span[contains(@class, 'oxd-topbar-body-nav-tab-item') and contains(text(), 'Job')]]") #//li[span[contains(@class, 'oxd-topbar-body-nav-tab-item') and contains(text(), 'Job')]]
        self.organization = (By.XPATH, "//span[contains(text(), 'Organization')]")#//span[contains(text(), 'Organization')]
        self.Qualifications = (By.XPATH, "//span[contains(text(), 'Qualifications')]") #//span[contains(text(), 'Qualifications')]
        self.Nationalities = (By.XPATH, "//a[contains(text(), 'Nationalities')]")#//a[contains(text(), 'Nationalities')]
        self.Corporate = (By.XPATH, "//a[contains(text(), 'Corporate Branding')]")#//a[contains(text(), 'Corporate Branding')]
        self.Configuration = (By.XPATH, "//span[contains(text(), 'Configuration')]")#//span[contains(text(), 'Configuration')]
        
        #Menu page
        self.Admin = (By.XPATH, "//span[contains(@class, 'oxd-main-menu-item--name') and text()='Admin']") #//span[contains(@class, 'oxd-main-menu-item--name') and text()='Admin']
        self.PIM = (By.XPATH, "//a[@class='oxd-main-menu-item']/span[text()='PIM']") #//a[@class='oxd-main-menu-item']/span[text()='PIM']
        self.Leave = (By.XPATH, "//span[text()='Leave']")#//span[text()='Leave']
        self.Time = (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name' and text()='Time']") #//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name' and text()='Time']
        self.Recruitment = (By.XPATH, "//span[text()='Recruitment']")#//span[text()='Recruitment']
        self.my_info = (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name' and text()='My Info']")#//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name' and text()='My Info']
        self.Performance = (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name' and text()='Performance']")#//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name' and text()='Performance']

        
        
    def validate_title(self):
        assert self.driver.title == self.page_title

    def validate_admin_options(self):
        options = [
            self.user_management, self.job, self.organization, self.Qualifications, self.Nationalities, self.Corporate, self.Configuration,self.Admin, self.PIM, self.Leave, self.Time, self.Recruitment, self.my_info, self.Performance
        ]
        for option in options:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(option)
            )
 
