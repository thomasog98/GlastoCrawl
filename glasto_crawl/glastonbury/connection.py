from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options

class srv():
    def __init__(self,driver_path):
        
        self.chrome_services = Service(driver_path)
        self.chrome_options = Options()
        self.chrome_options.add_argument("incognito")
        self.chrome_options.add_argument("disable")
        prefs = {"profile.managed_default_content_settings.images": 2,
                 "profile.default_content_setting_values.cookies": 1,
                 "profile.managed_default_content_settings.javascript": 1, 
                 "profile.cookie_controls_mode": 0}
        self.chrome_options.add_experimental_option("prefs", prefs)

