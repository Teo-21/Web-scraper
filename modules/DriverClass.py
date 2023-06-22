from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Driver:

    def __init__(self):
       pass 

    def scrapeData(self):

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.nekretnine.rs")
        driver.maximize_window()
        sleep(5)
        

   
        