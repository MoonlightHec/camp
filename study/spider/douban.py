# _*_ coding: utf-8 _*_
"""
# @Time : 2021/2/20 17:01 
# @Author : River 
# @File : douban.py
# @desc :
"""
import requests
from bs4 import BeautifulSoup

movies_list = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'Host': 'movie.douban.com'}
r = requests.get(url='https://movie.douban.com/top250?start=75', headers=headers)

soup = BeautifulSoup(r.text, 'lxml')
ol_list = soup.find_all('div', class_='info')
for each in ol_list:
    title = each.div.a.span.text.strip()
    # english_title = each.div.a.span.span.text.strip()
    is_play = each.div.span
    movie = {'片名': title, '英文名': 1, '播放源': is_play}
    movies_list.append(movie)
print(movies_list)
