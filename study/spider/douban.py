# _*_ coding: utf-8 _*_
"""
# @Time : 2021/2/20 17:01 
# @Author : River 
# @File : douban.py
# @desc :
"""
import requests
from bs4 import BeautifulSoup


def get_ol_list(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'Host': 'movie.douban.com'}
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    return soup.find_all('div', class_='info')


def get_movie(movie_info):
    title_list = movie_info.find_all('span', class_='title')
    playable = movie_info.find('span', class_='playable')
    movie = {'片名': '', '英文名': '', '播放源': ''}
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
        for each in get_ol_list(url):
            print(get_movie(each))


if __name__ == '__main__':
    main()
