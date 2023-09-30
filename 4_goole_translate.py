
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

'''
4. Create a test with the following:
a. Open Google Translate web page
b. Write anything in Hebrew in the text area
'''

driver = webdriver.Firefox()
website = "https://translate.google.com/?hl=iw&sl=iw&tl=en&op=translate"

hebrew_text = "תכתוב משהו בעברית"

driver.get(website)
driver.find_element(By.CLASS_NAME, 'er8xn').send_keys(hebrew_text)

