import sys, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

'''
9. Open any browser on "Github" website https://github.com/
a. Enter “Selenium” keyword in search textfield
b. Press Enter to search (through code - of course).
'''

driver = webdriver.Firefox()
driver.get("https://github.com/")

driver.find_element(By.CSS_SELECTOR, 'span.flex-1').click()
time.sleep(1)
search_input = driver.find_element('id','query-builder-test')
time.sleep(1)
search_input.send_keys('Selenium')
time.sleep(1)
search_input.send_keys(Keys.RETURN)