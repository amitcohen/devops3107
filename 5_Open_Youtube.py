
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

'''
5. Open Youtube web page
a. Type a name of a song
b. Click on search.
'''

driver = webdriver.Firefox()
driver.get("https://www.youtube.com")

search_box = driver.find_element("xpath", "//input[@id='search']")
time.sleep(2)
search_box.send_keys("Electronic Background Music For Studying Chill Out Instrumental Study Mix.")
time.sleep(2)
search_box.send_keys(Keys.RETURN)
