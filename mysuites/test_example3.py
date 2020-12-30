# _*_ coding: utf-8 _*_
"""
# @Time : 2020/12/14 17:09 
# @Author : River 
# @File : test_example3.py
# @desc : 参数化实例
"""
import pytest


def sum_function(x, y):
    return x + y


parameter = [[1, 1, 2], [2, 2, 4], [10, 1, 11], [1, 2, 4]]


class Test_Data:
    """
    测试sum方法
    """

    @pytest.mark.parametrize('x,y,z', parameter)
    def test_sum(self, x, y, z):
        assert sum_function(x, y) == z
