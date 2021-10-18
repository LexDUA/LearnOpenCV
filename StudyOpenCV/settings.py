'''
Created on 18 окт. 2021 г.

@author: Alex
'''

import configparser

def iniSetting():

    config = configparser.ConfigParser()
    config['DEFAULT'] = {}
    config['filespath'] = {}
    config['filespath']['image_path'] = r'...testFaces.jpg'
    config['filespath']['path_filter '] = r'...\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml'
    
    with open('config.ini', 'w') as configfile:
        config.write(configfile) 
    
def getFromSetting(key):
    config = configparser.ConfigParser()
    config.read(r'config.ini')
    config.sections()
    return config['filespath'][key]  

