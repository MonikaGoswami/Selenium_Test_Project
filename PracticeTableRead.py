#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 20:33:33 2019

@author: monikasingh
"""

from selenium import webdriver

driver=webdriver.Chrome('/Users/monikasingh/Downloads/chromedriver')
driver.get('https://www.toolsqa.com/automation-practice-table/')

mytable = driver.find_element_by_css_selector('#content > table')   #To print complete table rows
print ('For table rows:')
for row in mytable.find_elements_by_css_selector('tr'):
    rowList=[]
    for cell in row.find_elements_by_tag_name('th'):
        rowList.append(cell.text)
    for cell in row.find_elements_by_tag_name('td'):
        rowList.append(cell.text)
    print (rowList)

print ('For body rows:')    
mytable = driver.find_element_by_css_selector('#content > table > tbody')   #To print only body rows
for row in mytable.find_elements_by_css_selector('tr'):
    rowList=[]
    for cell in row.find_elements_by_tag_name('th'):
        rowList.append(cell.text)
    for cell in row.find_elements_by_tag_name('td'):
        rowList.append(cell.text)

    print (rowList)
