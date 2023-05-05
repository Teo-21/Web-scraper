from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Driver:

    driver : webdriver

    def __init__(self):
        
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def openBrowser(self):
        self.driver.get("https://estitor.com/rs-en/real-estates/purpose-rent/type-apartment/city-beograd?gclid=Cj0KCQjwr82iBhCuARIsAO0EAZyH5hs24md0yToSFt0CAKOQo184URrf_Zb3Pudl-uAqicJet0X-Xl8aAqXsEALw_wcB")

    def closeBrowser(self):
        self.driver.close()    
        