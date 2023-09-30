
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
website = "http://www.ynet.co.il"


def open_website():
    # 1. Opening the website
    driver.get(website)

    # 2. Get the websote title
    website_title = driver.title
    print("Website Title:", website_title[::-1])

    # 3. Refresh
    driver.refresh()

open_website()
