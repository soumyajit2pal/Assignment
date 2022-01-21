from selenium_support import Selenium_Support
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configurations import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Test_Flipkart:
    
    def setUp(self):
        self.support = Selenium_Support()
        self.support.init()
        self.driver = self.support.driver
        self.driver.implicitly_wait(15)


    def launch_URL(self):
        self.driver.get("https://www.flipkart.com/")

    def LoginWindow(self, username, passoword):

        try:
            WebDriverWait(self.driver, 25).until(
        EC.presence_of_element_located((By.XPATH, "//span[.='Enter Email/Mobile number']//..//../input[@type='text']")))
            self.username__ = self.driver.find_element_by_xpath("//span[.='Enter Email/Mobile number']//..//../input[@type='text']")
        
            self.password__ = self.driver.find_element_by_xpath("//span[.='Enter Password']//..//../input[@type='password']")
            self.submit = self.driver.find_element_by_xpath("//button[.='Login']")
            self.username__.send_keys(username)
            self.password__.send_keys(passoword)
            self.submit.submit()
        except Exception as e:
            print(e)


    def Handle_PopUp_Login(self, username, password):
        try:
            WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//span[.='Login']//../../..//..//button)[1]")))

            WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[.='Login']")))
            
            print("here")
        except:
            self.driver.find_element_by_xpath("//a[.='Login']").click()
        
        finally:
            self.LoginWindow(username, password)


    def LoginToFlipkart(self):
        self.username_= getConfig()['user_details']['username']
        self.password_ = getConfig()['user_details']['password']
        print(self.username_, self.password_)
        self.Handle_PopUp_Login(self.username_ , self.password_)



    def search_item(self):
        try:
            search_box =WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.XPATH, '//input[@name="q"]')))
            search_box.send_keys(getConfig()['search']['item'])
            
            search_box.send_keys(Keys.ENTER)

        except Exception as e:
            print(e)  
            

    def set_Filter(self):

        self.range= getConfig()['search']['range'].split('-')
        print(self.range)
        if len(self.range)>0 and len(self.range)<3:
            self.lower_bound = self.range[0]
            self.upper_boud = self.range[1]
        else:
            raise 'Please give appropiate range'

        lower_price_range= WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, "(//span[.='Price']//..//..//..//select)[1]")))
        drop = Select(lower_price_range)
        drop.select_by_value(self.lower_bound)

        upper_price_range= WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, "(//span[.='Price']//..//..//..//select)[2]")))
        drop = Select(upper_price_range)
        drop.select_by_value(self.upper_boud)


    def count_of_validating_criteria(self):
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(., 'Showing')]")))
        data = self.driver.find_element_by_xpath("//span[contains(., 'Showing')]")
        str_data= data.text

        print("Total {} items matches the critetia".format(str_data.split(" ")[5]))


    def tearDown(self):
        self.driver.close()
        self.driver.quit()

test_flip= Test_Flipkart()
test_flip.setUp()
test_flip.launch_URL()
test_flip.LoginToFlipkart()
test_flip.search_item()
test_flip.set_Filter()
test_flip.count_of_validating_criteria()
test_flip.tearDown()


