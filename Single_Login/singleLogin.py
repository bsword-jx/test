from 智慧城管.Base_Page.login import Login
from selenium import webdriver
import time


'''
输入username，password
'''
class single_Login():

    def __init__(self,driver,base_url,username,password):
        login = Login(driver,base_url)
        login.open_url()
        login.input_username(username)
        login.input_password(password)
        login.click_login()
        time.sleep(3)
        pass