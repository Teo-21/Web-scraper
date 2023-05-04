from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Driver:

    driver : webdriver

    def __init__(self):
        
        self.driver = webdriver.Chrome("chromedriver.exe")
