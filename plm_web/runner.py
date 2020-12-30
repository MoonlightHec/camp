# _*_ coding: utf-8 _*_
"""
# @Time : 2020/11/26 11:04 
# @Author : River 
# @File : runner.py
# @desc :
"""
import os

import pytest

pytest.main(['-s', 'test_function_explain.py', '--alluredir', './temp'])
os.system('allure generate ./temp -o ./report --clean')
