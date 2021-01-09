# _*_ coding: utf-8 _*_
"""
# @Time : 2021/1/8 16:01 
# @Author : River 
# @File : __init__.py.py
# @desc :
"""


class A:
    var_a = 17
    var_b = '小太阳'

    @staticmethod
    def fun_a(p1):
        print('执行功能a，参数：' + str(p1))
        return 'PASS', '相关信息'

    @staticmethod
    def fun_b(p1):
        print('执行功能b，参数：' + str(p1))
        return 'PASS', '相关信息'


"""
利用反射拿到类A的详细属性，包括方法和变量
"""

obj = A()
variable = getattr(obj, 'var_b')  # 获取var_a变量
function = getattr(obj, 'fun_b')  # 获取b方法
print('获取到的变量:%s' % variable)
function('7')
