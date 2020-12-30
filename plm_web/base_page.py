# _*_ coding: utf-8 _*_
"""
# @Time : 2020/11/26 16:44 
# @Author : River 
# @File : base_page.py
# @desc :
"""

from selenium import webdriver


class BasePages:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def quit(self):
        """
        关闭chromedriver
        :return:
        """
        self.driver.quit()

    def plm_login(self):
        """
        登录
        :return:
        """
        self.driver.get("plm.hqygou.com:8087/#")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys('lijun7')
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('lijun789')
        self.driver.find_element_by_xpath('//input[@name="dosubmit"]').click()
