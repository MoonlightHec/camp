# _*_ coding: utf-8 _*_
"""
# @Time : 2020/11/26 10:44 
# @Author : River 
# @File : test_example1.py
# @desc : 测试模块实例 面向对象封装（有测试类）
"""
import sys

from mysuites.page1 import Comm


class TestClazz:
    """
    这是一个测试类
    """

    def login(self):
        """
        这不是一个测试函数
        :return:
        """
        print("当前函数名：" + sys._getframe().f_code.co_name)

    def test_login(self):
        """
        这是一个测试函数
        :return:
        """
        print("当前函数名：" + sys._getframe().f_code.co_name)
        comm = Comm()
        comm.login()
        comm.quit()
