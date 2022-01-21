import configparser

def getConfig():
    config = configparser.ConfigParser()
    config.read('properties.ini')
    return config

