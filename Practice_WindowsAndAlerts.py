#!/usr/bin/env python3
"""
Created on Tue Sep 24 20:33:33 2019

@author: monikasingh
"""

import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains 

driver=webdriver.Chrome('/Users/monikasingh/Downloads/chromedriver')
driver.get('http://www.seleniumframework.com/Practiceform/')
window_before = driver.window_handles[0]

driver.find_element_by_id('button1').click()
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_id('mobile-menu').click()
driver.find_element_by_css_selector('#dl-menu > div > ul > li.menu-item.menu-item-type-custom.menu-item-object-custom.menu-item-has-children.menu-item-1520.has-children.no-link > a').click()
time.sleep(5)
driver.find_element_by_css_selector('#dl-menu > div > ul > li.menu-item.menu-item-type-custom.menu-item-object-custom.menu-item-has-children.menu-item-1520.has-children.no-link.dl-subviewopen > ul > li.menu-item.menu-item-type-custom.menu-item-object-custom.menu-item-3218.level-arrows-on > a').click()
driver.close()
                                    
driver.switch_to.window(driver.window_handles[0])
driver.find_element_by_css_selector('#content > div:nth-child(2) > div:nth-child(2) > div > div.wpb_raw_code.wpb_content_element.wpb_raw_html > div > p:nth-child(5) > button').click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
#el=driver.find_element_by_xpath('/html/body')
#print(el.text())
driver.close()

driver.switch_to.window(driver.window_handles[0])                                 
driver.find_element_by_css_selector('#content > div:nth-child(2) > div:nth-child(2) > div > div.wpb_raw_code.wpb_content_element.wpb_raw_html > div > p:nth-child(6) > button').click()
driver.switch_to.window(driver.window_handles[1])
ActionChains(driver).move_to_element(driver.find_element_by_xpath('//*[@id="main-nav"]/li[2]/a/span')).perform()
ActionChains(driver).move_to_element(driver.find_element_by_xpath('//*[@id="main-nav"]/li[2]/ul/li[3]/a/span')).perform()
subCategory = wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-nav"]/li[2]/ul/li[3]/ul/li[3]/a/span')))
subCategory.click()
time.sleep(5)
driver.close()

driver.switch_to.window(driver.window_handles[0])
print(driver.find_element_by_css_selector('#content > div:nth-child(2) > div:nth-child(2) > div > div.wpb_raw_code.wpb_content_element.wpb_raw_html > div > p:nth-child(6) > a:nth-child(5)').text)

driver.find_element_by_id('alert').click()
time.sleep(5)     #Just to see next click
driver.switch_to.alert.accept()

button=wait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'timingAlert')))
button.send_keys("\n")
wait(driver, 10).until(EC.alert_is_present(),'confirmation popup to appear.')
time.sleep(5)    #Just to see next click
driver.switch_to.alert.accept()

driver.find_element_by_id('colorVar').click()

ActionChains(driver).double_click(driver.find_element_by_id('doubleClick')).perform()

source_element = driver.find_element_by_id('draga')
dest_element = driver.find_element_by_id('dragb')
#ActionChains(driver).drag_and_drop(source_element, dest_element).perform()
ActionChains(driver).click_and_hold(source_element).move_to_element(dest_element).release(dest_element).perform()

