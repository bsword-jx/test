import unittest
from selenium import webdriver
from 智慧城管.Single_Login.singleLogin import single_Login


class Test_Case(unittest.TestCase):
    driver = ''
    url = ''

    @classmethod
    def init_driver(self):
        # 正在自动控制
        print('去除自动化')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        return webdriver.Chrome(options=chrome_options)  # 新版selenium参数名options
    @classmethod
    def setUpClass(cls) -> None:
        username = 'jx'
        password = '111111'
        cls.driver = cls.init_driver()
        cls.driver.maximize_window()
        cls.url = 'http://124.47.13.22:8080/#/'
        single_Login(cls.driver, cls.url,username,password)
        pass
    def test_insert(self):
        #登录
        print("九大标准操作")
        pass
    def test_ase(self):
        print("验证")

    @classmethod
    def tearDownClass(cls) -> None:
        print("退出")
        cls.driver.quit()
        pass
if __name__ == '__main__':
    unittest.main()