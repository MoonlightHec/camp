# _*_ coding: utf-8 _*_
"""
# @Time : 2021/2/20 17:01 
# @Author : River 
# @File : douban.py
# @desc :
"""
import json
import os

import requests
from bs4 import BeautifulSoup
from ruamel import yaml

from pytest_util import sort_yaml


def get_soup(url):
    """
    获取整个页面soup对象
    :param url:
    :return:
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'Host': 'movie.douban.com'}
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    return soup


def get_movie(soup):
    movie_list = {}

    pic_list = soup.find_all('div', 'pic')
    for each in pic_list:
        movie = {'name': '', 'detail_info': '', 'imageUrl': '', 'playable': ''}
        # 获取排名
        sort = each.find('em').text.strip()
        name = each.img['alt']
        movie['name'] = name
        movie['detail_info'] = each.a['href']
        movie['imageUrl'] = each.img['src']
        movie_list[sort] = movie

    return movie_list


def main():
    path = './movies.yaml'
    if os.path.exists(path):
        os.remove(path)
    for offset in range(0, 250, 25):
        url = 'https://movie.douban.com/top250?start=' + str(offset)
        movies = get_movie(get_soup(url))
        with open('./movies2.yaml', 'w', encoding='utf8') as stream:
            print(movies)
            sort_yaml.ordered_yaml_dump(movies, stream, allow_unicode=True)
        for i in sorted(movies.items(), key=lambda x: x[1]['name'], reverse=True):
            with open(path, 'a', encoding='utf8') as stream:
                print(i)
                sort_yaml.ordered_yaml_dump(i, stream, allow_unicode=True)


if __name__ == '__main__':
    main()
