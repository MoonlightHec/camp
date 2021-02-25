# _*_ coding: utf-8 _*_
"""
# @Time : 2021/2/24 14:39 
# @Author : River 
# @File : ip_useful.py
# @desc :
"""
import os
import random
import time

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from requests import TooManyRedirects

from pytest_util import sort_yaml


def random_useragent():
    """
    获取一个随机User-Agent的headers
    :return:
    """
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random,
    }
    return headers


def ip_filter(url, headers):
    """
    测试代理ip是否可用
    :return:
    """
    pro_list = sort_yaml.ordered_yaml_load('./pro_ip.yaml')
    # 可用ip储存位置
    ip_path = './pro_use.yaml'
    if os.path.exists(ip_path):
        os.remove(ip_path)
    key = 0
    for pro in pro_list:
        try:
            pro_info = {}
            time.sleep(1)
            requests.get(url=url, headers=headers, proxies={'http': pro_list[pro]})
            print('ip可用：%s' % pro_list[pro])
            key += 1
            pro_info[key] = pro_list[pro]
            with open(ip_path, 'a', encoding='utf8') as stream:
                sort_yaml.ordered_yaml_dump(pro_info, stream, allow_unicode=True)
        except TooManyRedirects:
            print('ip不可用:%s' % pro_list[pro])


def get_soup(request_attr):
    """
    获取整个页面soup对象
    :param request_attr:
    :return:
    """
    if request_attr.ip:
        requests_ip = request_attr.ip
    # 获取一个随机代理ip
    else:
        key = random.sample(request_attr.ip_list.keys(), 1)
        requests_ip = request_attr.ip_list[key[0]]
    # 获取一个随机User-Agent
    headers = random_useragent()
    if request_attr.headers:
        headers = {**headers, **request_attr.headers}
    time.sleep(1)
    try:
        r = requests.get(url=request_attr.url, headers=headers, proxies={'http': requests_ip})
        r.encoding = 'utf-8'
        print("请求ip：%s" % request_attr.ip_list[key[0]])
        soup = BeautifulSoup(r.text, 'lxml')
    except TooManyRedirects:
        print("此ip不可用：%s" % request_attr.ip_list[key[0]])
        get_soup(request_attr)
    except:
        print("系统异常")
        get_soup(request_attr)
    return soup


def main():
    url = "https://movie.douban.com/top250?start="
    headers = random_useragent()
    headers.setdefault('Host', 'movie.douban.com')
    ip_filter(url, headers)


if __name__ == '__main__':
    main()
