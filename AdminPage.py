from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AdminPage:
    def __init__(self):
        #self.driver = driver
        self.page_title = "OrangeHRM"
        self.user_management = (By.XPATH, "//span[contains(text(), 'User Management')]")
        self.job = (By.XPATH, "//li[span[contains(@class, 'oxd-topbar-body-nav-tab-item') and contains(text(), 'Job')]]") 
        self.organization = (By.XPATH, "//span[contains(text(), 'Organization')]")
        self.Qualifications = (By.XPATH, "//span[contains(text(), 'Qualifications')]") 
        self.Nationalities = (By.XPATH, "//a[contains(text(), 'Nationalities')]")
        self.Corporate = (By.XPATH, "//a[contains(text(), 'Corporate Branding')]")
        self.Configuration = (By.XPATH, "//span[contains(text(), 'Configuration')]")
        
        #Menu page
        self.Admin = (By.XPATH, "//span[contains(@class, 'oxd-main-menu-item--name') and text()='Admin']")
        self.PIM = (By.XPATH, "//a[@class='oxd-main-menu-item']/span[text()='PIM']")
        self.Leave = (By.XPATH, "//span[text()='Leave']")#//span[text()='Leave']
        self.Time = (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name' and text()='Time']") 
        self.Recruitment = (By.XPATH, "//span[text()='Recruitment']")
        self.my_info = (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name' and text()='My Info']") 
        self.Performance = (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name' and text()='Performance']")

        #Main menu list


 
