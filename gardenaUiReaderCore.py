import time
import webbrowser
from selenium import webdriver

class GardenaUiReader:  
    def __init__(self, url):  
        self.url = url
        self.browser = webdriver.Firefox()
      
    def login(self):
        self.browser.get(self.url)

        input_username = self.browser.find_element_by_id('ember9')
        input_password = self.browser.find_element_by_id('ember13')
        button_login = self.browser.find_element_by_id('login-button')
        
        input_username.send_keys('brandadrian@gmail.com')
        input_password.send_keys('sicher')
        
        button_login.click()

        time.sleep(5);
        


    def navigateToAbout(self):
        items = self.browser.find_elements_by_tag_name('li')

        for item in items:
            if 'About' in item.text:
                item.click()
                break;

        time.sleep(2);

    def navigateToVersions(self):
        versions = self.browser.find_element_by_id('ember64')
        time.sleep(5);
        versions.click()

        time.sleep(2);

    def getVersion(self):
        items = self.browser.find_elements_by_tag_name('li')

        for item in items:
            if 'App version' in item.text:
                version = item.text
                break
                
        return version

    def listAllElements(self):
        ids = self.browser.find_elements_by_xpath('//*[@id]')
        for i in ids:
            print(i.get_attribute('id'))

        return ids
