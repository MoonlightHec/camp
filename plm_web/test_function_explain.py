# _*_ coding: utf-8 _*_
"""
# @Time : 2020/11/28 15:21 
# @Author : River 
# @File : test_function_explain.py
# @desc : pytest中的一些方法执行逻辑
"""
import pytest


class Test_Function:
    @staticmethod
    def setup():
        """
        每个用例执行前调用
        :return:
        """
        print("\n--------用例执行开始--------")

    @staticmethod
    def teardown():
        """
        每个用例执行完后调用，无论用例是否执行失败
        :return:
        """
        print("\n--------用例执行结束--------")

    @staticmethod
    def setup_class():
        """
        所有用例执行前调用（类开始时调用）
        :return:
        """
        print("\n--------所有用例执行开始--------")

    @staticmethod
    def teardown_class():
        """
        每个用例执行完后调用，无论用例是否执行失败
        :return:
        """
        print("\n--------所有用例执行结束--------")

    @pytest.fixture()
    def my_setup(self):
        """
        手动设置是否在某个测试用例执行前后执行，yield分割方法执行前后执行后
        优先级高于setup和teardown，在setup前，在teardown后
        :return:
        """
        print("fixture开始")
        yield
        print("fixture结束")

    def test_f1(self):
        print("f1")

    def test_f2(self, my_setup):
        print("f2")

    def test_f3(self):
        print("f3")
