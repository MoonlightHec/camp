# _*_ coding: utf-8 _*_
"""
# @Time : 2020/11/26 10:55 
# @Author : River 
# @File : test_example2.py
# @desc : 测试模块实例 模块化封装（没有测试类）
"""
import sys
import time

from mysuites.page1 import Comm


def test_userinfo():
    """
    这是一个测试函数
    :return:
    """
    print("当前函数名：" + sys._getframe().f_code.co_name)
    comm = Comm()
    comm.login()
    comm.user_info()
    comm.quit()


def search_test():
    """
    这是一个测试函数
    :return:
    """
    print("当前函数名：" + sys._getframe().f_code.co_name)
    comm = Comm()
    comm.login()
    comm.search("手机")
    time.sleep(5)
    comm.quit()
