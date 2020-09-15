from selenium import webdriver
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import logging
import utilitiess.custom_logger as cl


class LoginPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)
    def __init__(self, driver):
        self.driver = driver
    _login_link = 'Login'
    _email_fields = 'user_email'
    _password_feild = 'user_password'
    _login_button = "commit"



    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType='linktext')

    def enterEmail(self, email):
        self.sendKeys(email, self._email_fields)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_feild)

    def loginbutton(self):
        self.elementClick(self._login_button , locatorType='name')

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.loginbutton()

    def verifyLoginSuccessfull(self):
        result = self.isElementPresent( "//input[@placeholder='Find a course']", 'xpath')
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[@class='alert alert-danger']", 'xpath')
        return result

