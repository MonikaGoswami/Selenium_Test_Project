"""
Created on Mon Sep 23 17:10:12 2019

@author: monikasingh
"""

import sys
from selenium import webdriver

sys.path.append('/usr/local/lib/python3.6/site-packages')
driver=webdriver.Chrome('/Users/monikasingh/Downloads/chromedriver')

driver.get('https://www.techlistic.com/p/selenium-practice-form.html')
driver.find_element_by_name('firstname').send_keys('Monika')
driver.find_element_by_name('lastname').send_keys('Goswami')
driver.find_element_by_id('sex-1').click()
driver.find_element_by_id('exp-4').click()
driver.find_element_by_id('datepicker').send_keys('23/09/2019')
driver.find_element_by_id('profession-1').click()
driver.find_element_by_id('tool-2').click()
driver.find_element_by_id('continents').send_keys('Asia')
driver.find_element_by_id('selenium_commands').send_keys('WebElement Commands')
driver.find_element_by_id('photo').send_keys('/Users/monikasingh/Downloads/PAN_Front.JPG')
driver.find_element_by_link_text('Click here to Download File').click()
