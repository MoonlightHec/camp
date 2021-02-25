# _*_ coding: utf-8 _*_
"""
# @Time : 2021/2/25 10:35 
# @Author : River 
# @File : free_ip.py
# @desc :
"""
import requests
import yaml
from bs4 import BeautifulSoup

from study.spider.requestAttr import requestAttr
from study.spider.spider_tool import get_soup, random_useragent


def main():
    url1 = 'http://www.ip3366.net/?stype=5&page='
    url2 = ''

    # 获取ip代理集合
    with open('./pro_use.yaml', 'r', encoding='utf8') as stream:
        pro_list = yaml.safe_load(stream)
    key = 0
    for index in range(0, 1, 1):
        ip_info_dict = {}
        url = url1 + str(index) + url2
        request_attr = requestAttr(url=url, ip_list=pro_list, ip='138.117.84.161:8080')
        soup = get_soup(request_attr)
        tbody = soup.find('tbody')
        tr_list = tbody.find_all('tr')
        for each in tr_list:
            key += 1
            td = each.find_all('td')
            ip = td[0].text.strip() + ':' + td[1].text.strip()
            ip_info_dict[key] = ip
        print(ip_info_dict)


def test():
    url1 = 'https://www.kuaidaili.com/free/inha/'
    url2 = '/'
    headers = random_useragent()
    key = 0
    for index in range(1, 2, 1):
        ip_info_dict = {}
        url = url1 + str(index) + url2
        request_attr = requestAttr(url=url, headers=headers, ip='10.32.4.191')
        r = requests.get(url=request_attr.url, headers=request_attr.headers, proxies={'https': request_attr.ip})
        soup = BeautifulSoup(r.text, 'lxml')
        tbody = soup.find('tbody')
        tr_list = tbody.find_all('tr')
        for each in tr_list:
            key += 1
            td = each.find_all('td')
            ip = td[0].text.strip() + ':' + td[1].text.strip()
            ip_info_dict[key] = ip
        print(ip_info_dict)


if __name__ == '__main__':
    test()