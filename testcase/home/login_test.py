from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage

import unittest
import pytest

class LoginTest(unittest.TestCase):
    baseurl = 'https://letskodeit.teachable.com'
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(20)
    lp = LoginPage(driver)
    driver.get(baseurl)


    def test_validLogin(self):
        self.lp.login('test@email.com', 'abcabc')
        result=self.lp.verifyLoginSuccessfull()
        assert result == True
        #self.driver.quit()


    def test_validLogin(self):
        self.driver.get(self.baseurl)
        self.lp.login('test@email.com', 'abcabcabcabc')
        result = self.lp.verifyLoginFailed()
        assert result == True



        # userIcon = driver.find_element(By.XPATH, "//input[@placeholder='Find a course']")
        # if userIcon is not None:
        #     print("login successfully")
        # else:
        #     print("not successfully login")

