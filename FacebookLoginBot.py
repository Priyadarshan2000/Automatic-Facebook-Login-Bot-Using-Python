# Priyadarshan Ghosh

import time
from bs4 import BeautifulSoup
from selenium import webdriver
browser=webdriver.Chrome('C:\\webdrivers\\chromedriver.exe')

browser.get("https://www.facebook.com")
user_id="Your Facebook id" # Here enter your facebook Id
password="your Facebook Password" # Here enter your facebook password


element=browser.find_element_by_id("email")
element.send_keys(user_id)

passwor=browser.find_element_by_id("pass")
passwor.send_keys(password)
