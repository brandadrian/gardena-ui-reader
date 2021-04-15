import os
import json
import time
import webbrowser
from selenium import webdriver
from pymongo import MongoClient
from flask import Flask, request

app = Flask(__name__)
#usr = 'root' #os.environ['MONGO_DB_USER']
#pwd = 'root' #os.environ['MONGO_DB_PASS']
#client = MongoClient('mongodb+srv://' + usr + ':' + pwd + '@cluster0.srbj2.mongodb.net/running-event-db?retryWrites=true&w=majority')
#db = client['running-event-db']
#collection = db['running-event']

@app.route('/gardena-api')
def get():
    return 'OK'

@app.route('/gardena-api', methods=['POST'])
def post():
    req_data = request.get_json()
    collection.insert_one(req_data).inserted_id
    return ('', 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

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
