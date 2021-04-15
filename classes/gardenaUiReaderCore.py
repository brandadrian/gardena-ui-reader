import time
import webbrowser
from pyvirtualdisplay import Display
from selenium import webdriver

class GardenaUiReaderCore:  
    def __init__(self, url, username, password):  
        self.url = url
        self.password = password
        self.username = username
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        #Window size must be set for id recognition in headless mode
        options.add_argument('window-size=1920x1080') 
        self.browser = webdriver.Chrome(options=options)
      
    def login(self):
        self.browser.get(self.url)

        input_username = self.browser.find_element_by_id('ember9')
        input_password = self.browser.find_element_by_id('ember13')
        button_login = self.browser.find_element_by_id('login-button')
        
        input_username.send_keys(self.username)
        input_password.send_keys(self.password)
        
        button_login.click()

        time.sleep(2);

    def navigateToAbout(self):
        items = self.browser.find_elements_by_tag_name('li')

        for item in items:
            if 'Info' in item.text:
                item.click()
                break;

        time.sleep(2);

    def navigateToVersions(self):
        versions = self.browser.find_element_by_id('link-versions')
        versions.click()

        time.sleep(2);

    def getVersion(self):
        item = self.browser.find_element_by_class_name('app')                
        return item.text

    def listAllElements(self):
        ids = self.browser.find_elements_by_xpath('//*[@id]')
        for i in ids:
            print(i.get_attribute('id'))

        return ids
