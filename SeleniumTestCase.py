#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 15:44:58 2019

@author: monikasingh
"""
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait


driver=webdriver.Chrome('/Users/monikasingh/Downloads/chromedriver')
driver.get('http://automationpractice.com/index.php')
time.sleep(3)

ActionChains(driver).move_to_element(driver.find_element_by_css_selector('#block_top_menu > ul > li:nth-child(1) > a')).perform()
subMenu=wait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#block_top_menu > ul > li:nth-child(1) > ul > li:nth-child(1) > ul > li:nth-child(1) > a')))
subMenu.click()

itemName=driver.find_element_by_css_selector('#center_column > ul > li > div > div.right-block > h5 > a')
item=driver.find_element_by_css_selector('#center_column > ul > li').text

driver.find_element_by_id('search_query_top').send_keys(itemName.text)
driver.find_element_by_id('search_query_top').send_keys('\n')

searchedItem=driver.find_element_by_css_selector('#center_column > ul > li').text
                                                 
if(item == searchedItem): 
    print ("Test Passed.")
else:
    print ("Test Failed.")
