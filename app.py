# Author: Adrian Brand
# Date: 15.04.2021
# Description: App reads information of https://smart.gardena.com by using a selenium driver


#!/usr/bin/env python
import time
import webbrowser
import configparser
import os
from classes.gardenaUiReaderCore import GardenaUiReaderCore

#******************Methods******************#
#                                           #
def executeAction(id, actionText, function):
    print('Step 2.' + str(id) + ': Execute action')
    print(actionText)
    result = ''
    result = function()
    print(actionText + ' done!\n')

    return result

def writeFile(text):
    print('Step 3: Generate result')
    folder = 'results'
    if not os.path.exists(folder):
        os.makedirs(folder)
    fileName = folder + '/result' + time.strftime("%Y%m%d-%H%M%S") + '.txt'
    print('Write file ' + fileName + '...')
    file = open(fileName, "a")
    file.write(text)
    file.close()

def getVersion(gardenaUiReader):
    executeAction(0, 'Login', gardenaUiReader.login)
    executeAction(1, 'Navigate to About', gardenaUiReader.navigateToAbout)
    executeAction(2, 'Navigate to Versions', gardenaUiReader.navigateToVersions)
    version = executeAction(3, 'Read version', gardenaUiReader.getVersion)
    writeFile(version)
    return version

def writeLog(text):
    log = time.strftime("%Y%m%d-%H%M%S") + '; '+ text + '\n'
    fileName = 'log.txt'
    file = open(fileName, "a")
    file.write(log)
    file.close()

#                                           #
#******************Methods******************#


#******************Main*********************#
#                                           #
if __name__ == '__main__':
    #Setup
    try:
        config = configparser.RawConfigParser()
        config.read_file(open(r'config.txt'))
        url = config.get('GardenaLogin', 'url')
        username = config.get('GardenaLogin', 'username')
        password = config.get('GardenaLogin', 'password')    
        dbUsername = config.get('Database', 'username')
        database = config.get('Database', 'connection')
        
        print('``````````````````````````````````````````')
        print('```````````````Gardena UI Reader``````````')
        print('``````````````````````````````````````````\n')
        print('Step 1: Initialize application...')
        print('Connecting to https://smart.gardena.com as ' + username + '...')
        print('Connecting to Database ' + dbUsername + ' / ' + dbUsername + '...\n')
        writeLog('Info; App started')
        gardenaUiReaderCore = GardenaUiReaderCore(url, username, password)

        #Get Version
        version = getVersion(gardenaUiReaderCore)

        print('Step 4: Output Results')
        print('\n')
        print('----------------------------')
        print('Result 1 | Version; ' + version.split(':')[1].replace('\n',''))
        print('----------------------------')
        print('Result 2 | Temperatur; 42')
        print('----------------------------')
        print('Result 3 | Feuchtigkeit; 42')
        
    except Exception as e:
        print(e)
        writeLog('Error; ' + e)
    finally:
        gardenaUiReaderCore.dispose()
        writeLog('Info; App closed')
#                                           #
#******************Main*********************#







    












