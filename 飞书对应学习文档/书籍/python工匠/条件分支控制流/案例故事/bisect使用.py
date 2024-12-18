#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/24
import random
def get_sorted_movies(movies, sorting_type):
    """对电影列表进行排序并返回
    :param movies: Movie 对象列表
    :param sorting_type: 排序选项，可选值
        name（名称）、rating（评分）、year（年份）、random（随机乱序）
    """
    sorting_algos = {
        # sorting_type: (key_func, reverse)
        'name': (lambda movie: movie.name.lower(), False),
        'rating': (lambda movie: float(movie.rating), True),
        'year': (lambda movie: movie.year, True),
        'random': (lambda movie: random.random(), False),
    }
    try:
        key_func, reverse = sorting_algos[sorting_type]
    except KeyError:
        raise RuntimeError(f'Unknown sorting type: {sorting_type}')
    sorted_movies = sorted(movies, key=key_func, reverse=reverse)
    return sorted_movies