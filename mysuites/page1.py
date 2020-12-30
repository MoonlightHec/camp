# _*_ coding: utf-8 _*_
"""
# @Time : 2020/11/25 15:43 
# @Author : River 
# @File : page1.py
# @desc :
"""
import os
import time

from selenium import webdriver


class Comm:
    """
    电商项目
    """

    def __init__(self):
        self.driver = webdriver.Chrome()

    def quit(self):
        """
        关闭浏览器
        :return:
        """
        self.driver.quit()

    def login(self):
        """
        登录成功用例
        :return:
        """
        self.driver.get("http://testingedu.com.cn:8000/index.php/Home/user/login.html")
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys("13800138006")
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")
        self.driver.find_element_by_xpath('//*[@id="verify_code"]').send_keys('7777')
        self.driver.find_element_by_xpath('//a[contains(text(),"登")]').click()

    def user_info(self):
        """
        依赖登录
        用户信息图片修改
        :return:
        """
        # self.driver.implicitly_wait(10)
        time.sleep(1)
        self.driver.get("http://testingedu.com.cn:8000/index.php/Home/User/info.html")
        self.driver.find_element_by_xpath('//*[@id="preview"]').click()
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('//*[@id="layui-layer-iframe1"]'))
        # 图片转相对路径
        abspath = os.getcwd()
        filepath = os.path.join(abspath, "26.png")
        self.driver.find_element_by_xpath('//div[@id="filePicker"]/div[2]/input').send_keys(
            filepath)
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[text()="确定使用"]').click()

    def search(self, words):
        """
        依赖登录
        根据关键字搜索商品
        :param words: 要搜索的关键字
        :return:
        """
        self.driver.get("http://testingedu.com.cn:8000/index.php/Home/User/info.html")
        self.driver.find_element_by_xpath('//*[@id="q"]').send_keys(words)
        self.driver.find_element_by_xpath('//*[@id="sourch_form"]/a').click()
