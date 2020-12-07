from selenium.webdriver.common.by import By
# from Base.basePagt import Page
from 智慧城管.Base_Page.basePage import Page

'''
    获取登录元素,坐标
    username，password，submit
    一个模块写一个
'''
class Login(Page):
    user = (By.ID, 'username')
    pwd = (By.ID, 'password')
    button = (By.NAME, 'submit')
    messg = (By.CSS_SELECTOR,'#fm1>div>span')
    def __init__(self,driver,base_url):
        Page.__init__(self,driver,base_url)
    def open_url(self):
        print('open',self.base_url)
        self.driver.get(self.base_url)
    def input_username(self, username):
        self.input(self.user,username)

    def input_password(self, password):
        self.input(self.pwd,password)
    def click_login(self):
        self.click(self.button)
    def get_messgaes(self):
        return self.get_messg(self.messg)
