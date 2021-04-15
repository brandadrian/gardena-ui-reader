#!/usr/bin/env python
import time
import webbrowser
from gardenaUiReaderCore import GardenaUiReader

#---Methods---#
def exedcuteAction(actionText, function):
    try:
        print(actionText)
        global result
        result = function()
        print(actionText + ' done!')
    except:
        print('Error during executing ' + actionText)
    finally:
        print('\n')
        return result

def writeFile(text, doOpenAfterWrite):
    fileName = 'result' + time.strftime("%Y%m%d-%H%M%S") + '.txt'
    print('Write file ' + fileName + '...')
    file = open(fileName, "a")
    file.write(version)
    file.close()
    print('File written ' + fileName + '!')

    if (doOpenAfterWrite):
        webbrowser.open(fileName)
#---Methods End---#
        
#---Main---#
if __name__ == '__main__':      
    p = GardenaUiReader('https://smart.gardena.com/#/session/new?username=')  

    exedcuteAction('Login', p.login)
    exedcuteAction('Navigate to About', p.navigateToAbout)
    exedcuteAction('Navigate to Versions', p.navigateToVersions)
    version = exedcuteAction('Read version', p.getVersion)
    writeFile(version, True)
#---Main End---#






    












