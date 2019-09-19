#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:30:45 2019

@author: monika

"""
import sys
sys.path.append('/usr/local/lib/python3.6/site-packages')
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


driver=webdriver.Chrome('/Users/monikasingh/Downloads/chromedriver')
driver.get('http://automationpractice.com/index.php')
driver.find_element_by_link_text('Sign in').click()
time.sleep(2)
driver.find_element_by_name('email').send_keys('monikagoswami1991@gmail.com')
driver.find_element_by_name('passwd').send_keys('Monika@1991')
driver.find_element_by_name('SubmitLogin').click()

actions=ActionChains(driver)
category = driver.find_element_by_xpath("//a[text()='Women']")
actions.move_to_element(category).perform()

subCategory = wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='T-shirts']")))
subCategory.click()

actions=ActionChains(driver)
category = driver.find_element_by_xpath('//*[@id="center_column"]/ul/li/div/div[1]/div/a[1]/img')
actions.move_to_element(category).perform()

subCategory = wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/ul/li/div/div[2]/div[2]/a[2]/span')))
subCategory.click()

driver.find_element_by_xpath('//*[@id="quantity_wanted_p"]/a[2]/span/i').click()
driver.find_element_by_name('group_1').send_keys('L')
driver.find_element_by_id('color_14').click()
driver.find_element_by_css_selector('#add_to_cart > button > span').click()
driver.implicitly_wait(10)
driver.find_element_by_css_selector('#layer_cart > div.clearfix > div.layer_cart_cart.col-xs-12.col-md-6 > div.button-container > a > span').click()

