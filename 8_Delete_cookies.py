
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

'''
8. Open FF browser on any webpage:
a. Delete all cookies from browser.
b. Make sure all cookies are deleted by printing all cookies stored in the browser.
'''

# website = "about:preferences#privacy"
website = "https://www.amazon.co.uk"

def delete_cookies():
    # 1. Open Browser
    browser = webdriver.Firefox()
    browser.get(website)
    cookies = browser.get_cookies()
    
    list_of_all_cookies = []

    for c in cookies:
        print(c)
        print("Cookie Name:", list(c.values())[0] )
        list_of_all_cookies.append(list(c.values())[0])
        print()
    print('List Of All Cookies:', list_of_all_cookies)
    print()

    for cookie_name in list_of_all_cookies:
        print("I'm deleting the cookie:", cookie_name)
        browser.delete_cookie(cookie_name)




delete_cookies()