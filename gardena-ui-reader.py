#!/usr/bin/env python

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://smart.gardena.com/#/session/new?username=')

browser.find_element_by_id("ember9").send_keys('brandadrian@gmail.com')
browser.find_element_by_id("ember13").send_keys('sicher')
browser.find_element_by_id("login-button").click()

items = browser.find_elements_by_tag_name("a")

for item in items:
    print("a")
    print(item.text)
