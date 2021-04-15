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
def exedcuteAction(id, actionText, function):
    print('Step 2.' + str(id) + ': Execute action')
    print(actionText)
    result = ''
    result = function()
    print(actionText + ' done!\n')

    return result

def writeFile(text, doOpenAfterWrite):
    print('Step 3: Generate result')
    folder = 'results'
    if not os.path.exists(folder):
        os.makedirs(folder)
    fileName = folder + '/result' + time.strftime("%Y%m%d-%H%M%S") + '.txt'
    print('Write file ' + fileName + '...')
    file = open(fileName, "a")
    file.write(text)
    file.close()

    if (doOpenAfterWrite):
        webbrowser.open(fileName)

def getVersion(gardenaUiReader):
    exedcuteAction(0, 'Login', gardenaUiReader.login)
    exedcuteAction(1, 'Navigate to About', gardenaUiReader.navigateToAbout)
    exedcuteAction(2, 'Navigate to Versions', gardenaUiReader.navigateToVersions)
    version = exedcuteAction(3, 'Read version', gardenaUiReader.getVersion)
    return version
    #writeFile(version, False)

#                                           #
#******************Methods******************#


#******************Main*********************#
#                                           #
if __name__ == '__main__':
    #Setup
    config = configparser.RawConfigParser()
    config.read_file(open(r'config.txt'))
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
    
    gardenaUiReaderCore = GardenaUiReaderCore('https://smart.gardena.com/#/session/new?username=', username, password)

    #Get Version
    version = getVersion(gardenaUiReaderCore)
    print('Results\n')
    print('Version')
    print(version)
    
#                                           #
#******************Main*********************#







    












