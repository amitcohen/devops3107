
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

'''
7. Open Chrome browser on Facebook website https://www.facebook.com/
a. Login into Facebook (No need to send me credentials).
'''

website = "https://www.facebook.com"
username = "amitcohen@otmail.com"
password = "123456789"

def login():
    driver = webdriver.Firefox()
    driver.get(website)

    print("Login to wesite")
    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys(password)
    time.sleep(1)
    driver.find_element(By.NAME, 'login').click()



login()