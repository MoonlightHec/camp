# _*_ coding: utf-8 _*_
"""
# @Time : 2021/2/20 17:01 
# @Author : River 
# @File : douban.py
# @desc :
"""
import requests
from bs4 import BeautifulSoup


def get_soup(url):
    """
    获取整个页面
    :param url:
    :return:
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'Host': 'movie.douban.com'}
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    return soup


def get_movie(movie_info):
    movie = {'title': '', 'detail_info': '', 'imageUrl': '', 'playable': ''}

    # 获取排名
    for sort_tag in movie_info:
        sort = sort_tag.find('em')
        movie['title'] = sort.text.strip()

    playable = movie_info.find('span', class_='playable')

    for i, hd in enumerate(title_list):
        title = hd.text.strip()
        name = title.replace('\xa0', '').replace('/', '')
        if i:
            movie['英文名'] = name
        else:
            movie['片名'] = name
    if playable:
        movie['播放源'] = playable.text.strip()
    else:
        movie['播放源'] = '无'
    return movie


def main():
    for offset in range(0, 50, 25):
        url = 'https://movie.douban.com/top250?start=' + str(offset)
        pic_list = get_soup(url).find_all('div', 'pic')
        for each in pic_list:
            print(get_movie(each))


if __name__ == '__main__':
    main()
