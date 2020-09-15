from selenium import webdriver
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):
    def __init__(self, driver):
        self.driver = driver
    _login_link = 'Login'
    _email_fields = 'user_email'
    _password_feild = 'user_password'
    _login_button = "commit"

    def getloginLink(self):
        return self.driver.find_element(By.LINK_TEXT, self._login_link)
    def getEmailFeild(self):
        return  self.driver.find_element(By.ID, self._email_fields)
    def getPassword(self):
        return self.driver.find_element(By.ID, self. _password_feild)
    def getLoginButton(self):
        return self.driver.find_element(By.NAME, self._login_button)

        '''action perfom'''
    def clickLoginLink(self):
        self.getloginLink().click()

    def enterEmail(self, email):
        self.getEmailFeild().send_keys(email)

    def enterPassword(self, password):
        self.getPassword().send_keys(password)
    def loginbutton(self):
        self.getLoginButton().click()

    def login(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.loginbutton()






        # loginlink = self.driver.find_element(By.LINK_TEXT, 'Login')
        # loginlink.click()
        #
        # Email_LindeEdit =  self.driver.find_element(By.ID, 'user_email')
        # Email_LindeEdit.send_keys(username)
        #
        # Password_LineEdit =  self.driver.find_element(By.ID, 'user_password')
        # Password_LineEdit.send_keys(password)
        #
        # LoginButton =  self.driver.find_element(By.NAME, 'commit')
        # LoginButton.click()