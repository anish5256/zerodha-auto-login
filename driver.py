from selenium import webdriver
import chromedriver_autoinstaller

class ChromeDriver:

    def __init__(self):
        chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome()

    def get_driver(self):
        return self.driver
