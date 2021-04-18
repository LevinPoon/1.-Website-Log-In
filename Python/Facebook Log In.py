#!/usr/bin/env python
# coding: utf-8

# In[27]:


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

#1. open website (facebook) base on cell B2 thru IE
chromeOptions = webdriver.ChromeOptions()
browser = webdriver.Chrome('chromedriver.exe',chrome_options=chromeOptions)
browser.get("http://www.facebook.com/")
browser.maximize_window()

#2. Checking on the load status of the website

#3. Enter ID, password and log in button
browser.find_element_by_id("email").send_keys("*******")
browser.find_element_by_id("pass").send_keys("********")
browser.find_element_by_name("login").click()


# In[ ]:




