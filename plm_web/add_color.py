# _*_ coding: utf-8 _*_
"""
# @Time : 2021/2/4 14:38 
# @Author : River 
# @File : add_color.py
# @desc :
"""

from pytest_util.HttpRequest import HttpRequest


def color_change_add():
    """
    添加加色款
    :return:
    """
    url = 'http://plm.hqygou.com:8088/sample/develop/color/change/add'
    headers = {"Content-Type": "application/json", "PLM-TOKEN": "61207BABD2434549A0D4FC46A030583D"}
    data = {"inVoList": [{"id": "", "bizCode": 1, "color": "钴蓝色", "colorId": 81180, "goodsSn": "206078905", "productCode": "2060789",
                          "productImg": "http://pdm.hqygou.com/uploads/PLM/2020/7/thumb-img/1594064044393511575.jpg", "productLabel": "4",
                          "recommendFrom": 1, "errorMsg": "", "sizeId": "102733", "size": "2XL", "sku": "206078905", "purchasePrice": "",
                          "reproofingRemark": "", "reproofingLabel": "", "reproofingSn": "", "dataFrom": "", "purchaseUser": "",
                          "purchaseUserName": "", "purchaseName": "", "remark": ""}]}
    output = HttpRequest.post(url, headers, data)
    print('request: %s' % url)
    print('response:')
    print(output)


color_change_add()
