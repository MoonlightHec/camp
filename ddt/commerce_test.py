# _*_ coding: utf-8 _*_
"""
# @Time : 2020/12/15 17:34 
# @Author : River 
# @File : commerce_test.py
# @desc :
"""
import os
import time
import pytest

from mysuites.webkeys import WebKey
from ddt.params import datas


class Test_Commerce:
    """
    电商项目Web自动化测试类
    """

    def setup_class(self):
        """
        构造函数，创建对象的时候会执行
        :return:
        """
        self.web = WebKey()
        self.web.open_browser()

    @pytest.mark.skip(reason="后面的更精彩")
    def test_login(self):
        """
        登录成功的用例
        :return: None
        """
        self.web.geturl("http://testingedu.com.cn:8000/index.php/Home/user/login.html")
        self.web.input('//*[@id="username"]', "13800138006")
        self.web.input('//*[@id="password"]', "123456")
        self.web.input('//*[@id="verify_code"]', '7777')
        self.web.click('//a[contains(text(),"登")]')
        time.sleep(1)

    @pytest.mark.parametrize('list_cases', datas['loginPage'])
    def test_login_plus(self, list_cases):
        """
        数据驱动方式
        登录成功的用例
        :return: None
        """
        login_case = list_cases['cases']
        for cases in login_case:
            list_case = list(cases.values())
            function = getattr(self.web, list_case[0])
            values = list_case[0:]
            function(*values)

    @pytest.mark.skip(reason="后面的更精彩")
    def test_user_info(self):
        """
        修改个人中心头像
        :return:
        """
        self.web.geturl("http://testingedu.com.cn:8000/index.php/Home/User/info.html")
        self.web.click('//*[@id="preview"]')
        self.web.into_iframe('//*[@id="layui-layer-iframe1"]')
        abspath = os.getcwd()
        filepath = os.path.join(abspath, "../mysuites/26.png")
        self.web.input('//div[@id="filePicker"]/div[2]/input', filepath)
        time.sleep(1)
        self.web.click('//div[text()="确定使用"]')

    def teardown_class(self):
        self.web.quit()
