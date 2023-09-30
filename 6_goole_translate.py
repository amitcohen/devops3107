
import sys, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

'''
6. Open Firefox browser on Google Translate website: https://translate.google.com/
a. Find translation text field (the one you send keys to) with 3 different locators and
print the WebElement you created.
'''

driver = webdriver.Firefox()
driver.get("https://translate.google.com/?hl=iw&sl=iw&tl=en&op=translate")

# 1
field_by_class = driver.find_element(By.CLASS_NAME, "er8xn")
# # field_by_class.send_keys("XYZ")
print("CLASS locator:", field_by_class)

# 2
field_by_xpath = driver.find_element(By.XPATH, "/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div/div[2]/div[3]/c-wiz[1]/span/span/div/textarea")
# # field_by_xpath.send_keys("XYZ")
print("XPATH locator:", field_by_xpath)


# 3
field_by_css = driver.find_element(By.CSS_SELECTOR, ".er8xn")
# field_by_css.send_keys("XYZ")
print("CSS_SELECTOR locator:", field_by_css)