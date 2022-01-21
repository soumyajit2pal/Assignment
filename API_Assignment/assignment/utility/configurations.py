import configparser

def getConfig():
    config = configparser.ConfigParser()
    config.read('..\\assignment\\utility\\properties.ini')
    return config

