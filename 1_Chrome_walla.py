from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome()

website = "http://www.walla.co.il"

def open_website():
    while True:
        driver.get(website)


open_website()