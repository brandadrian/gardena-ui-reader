#!/usr/bin/env python
import time
import webbrowser
from selenium import webdriver

class GardenaUiReader:  
    def __init__(self, url):  
        self.url = url
        self.browser = webdriver.Firefox()
      
    def login(self):
        print('Try login')

        self.browser.get(self.url)

        input_username = self.browser.find_element_by_id('ember9')
        input_password = self.browser.find_element_by_id('ember13')
        button_login = self.browser.find_element_by_id('login-button')
        
        input_username.send_keys('brandadrian@gmail.com')
        input_password.send_keys('sicher')
        
        button_login.click()

        time.sleep(5);
        
        print('Login done')

    def navigateToAbout(self):
        print('Start navigating to About')

        items = self.browser.find_elements_by_tag_name('li')

        for item in items:
            if 'About' in item.text:
                item.click()
                print('About clicked')
                break;

        time.sleep(2);

    def navigateToVersions(self):
        print('Start navigating to Versions')

        versions = self.browser.find_element_by_id('ember64')
        time.sleep(5);
        versions.click()
        print('Versions clicked')

        time.sleep(2);

    def readVersion(self):
        print('Start reading Versions')

        items = self.browser.find_elements_by_tag_name('li')

        for item in items:
            if 'App version' in item.text:
                version = item.text
                print(item.text)
                break

        fileName = 'result' + time.strftime("%Y%m%d-%H%M%S") + '.txt'
        file = open(fileName, "a")
        file.write(version)
        file.close()

        webbrowser.open(fileName)

    def listAllElements(self):
        ids = self.browser.find_elements_by_xpath('//*[@id]')
        for i in ids:
            print(i.get_attribute('id'))

        print('Read element done')

      
p = GardenaUiReader('https://smart.gardena.com/#/session/new?username=')  
p.login()
p.navigateToAbout()
p.navigateToVersions()
p.readVersion()
#p.listAllElements()










