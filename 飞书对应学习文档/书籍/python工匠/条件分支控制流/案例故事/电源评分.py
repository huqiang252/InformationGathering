#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/24
import random

class Movie:
    """电影对象数据类"""

    def __init__(self, name, year, rating):
        self.name = name
        self.year = year
        self.rating = rating

    @property
    def rank(self):
        """按照评分对电影分级：

        - S: 8.5 分及以上
        - A：8 ~ 8.5 分
        - B：7 ~ 8 分
        - C：6 ~ 7 分
        - D：6 分以下
        """
        rating_num = float(self.rating)
        if rating_num >= 8.5:
            return 'S'
        elif rating_num >= 8:
            return 'A'
        elif rating_num >= 7:
            return 'B'
        elif rating_num >= 6:
            return 'C'
        else:
            return 'D'


def get_sorted_movies(movies, sorting_type):
    """对电影列表进行排序并返回

    :param movies: Movie 对象列表
    :param sorting_type: 排序选项，可选值
        name（名称）、rating（评分）、year（年份）、random（随机乱序）
    """
    if sorting_type == 'name':
        sorted_movies = sorted(movies, key=lambda movie: movie.name.lower())
    elif sorting_type == 'rating':
        sorted_movies = sorted(
            movies, key=lambda movie: float(movie.rating), reverse=True
        )
    elif sorting_type == 'year':
        sorted_movies = sorted(
            movies, key=lambda movie: movie.year, reverse=True
        )
    elif sorting_type == 'random':
        sorted_movies = sorted(movies, key=lambda movie: random.random())
    else:
        raise RuntimeError(f'Unknown sorting type: {sorting_type}')
    return sorted_movies


def main():
    movies = [
        {
            'name': 'The Shawshank Redemption',
            'year': 1994,
            'rating': '9.3',
        },
        {
            'name': 'The Godfather',
            'year': 1972,
            'rating': '9.2',
        },
        {
            'name': 'The Dark Knight',
            'year': 2008,
            'rating': '9.0',
        },
        {'name': 'Kaili Blues', 'year': 2015, 'rating': '7.3'}
    ]

    all_sorting_types=['name', 'rating', 'year', 'random']


    # 接收用户输入的排序选项
    sorting_type = input('Please input sorting type: ')
    if sorting_type not in all_sorting_types:
        print(
            'Sorry, "{}" is not a valid sorting type, please choose from '
            '"{}", exit now'.format(
                sorting_type,
                '/'.join(all_sorting_types),
            )
        )
        return

    # 初始化电影数据对象
    movie_items = []
    for movie_json in movies:
        movie = Movie(**movie_json)
        movie_items.append(movie)
    # 排序并输出电影列表
    sorted_movies = get_sorted_movies(movie_items, sorting_type)
    for movie in sorted_movies:
        print(
            f'- [{movie.rank}] {movie.name}({movie.year}) | rating: {movie.rating}'
        )

main()