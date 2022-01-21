from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
from os import environ
import argparse


class Selenium_Support:

    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Selenium support library')
        self.parser.add_argument('--browser', type=str,default='Firefox', help='Browser valid values [Chrome,Firefox,Default is Chrome]')
        self.parser.add_argument('--driverpath', type=str,default='Syspath',required=False, help='Optional parameter,Driver path for browser, default is system ')


    def init(self):
        """
        initialize browser & driver
        """
        args=self.parser.parse_args()
        print(args)

        browser = args.browser

        if browser.lower() == 'chrome':
            chrome_options = Options()
            if args.driverpath != 'Syspath':
                driver_path=args.driverpath
                service = Service(driver_path)
                self.driver = webdriver.Chrome(service=service,options=chrome_options)
            else:
                self.driver=webdriver.Chrome(options=chrome_options)
    
        elif browser.lower() == 'firefox':
            options = Options()
            if args.driverpath != 'Syspath':
                driver_path=args.driverpath
                service = Service(driver_path)
                self.driver = webdriver.Firefox(service=service,options=options)
            else:
                self.driver=webdriver.Firefox(options=options)



