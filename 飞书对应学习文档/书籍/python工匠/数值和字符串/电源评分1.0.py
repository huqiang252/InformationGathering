#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/19


def render_movies(username, movies):
    """
    以文本方式展示电影列表信息
    """
    welcome_text = 'Welcome, {}.\n'.format(username)
    text_parts = [welcome_text]
    for name, rating in movies:
        # 没有提供评分的电影，以[NOT RATED] 代替
        rating_text = rating if rating else '[NOT RATED]'
        movie_item = '* {}, Rating: {}'.format(name, rating_text)
        text_parts.append(movie_item)
    return '\n'.join(text_parts)

movies = [
    ('The Shawshank Redemption', '9.3'),
    ('The Prestige', '8.5'),
    ('Mulan', None),
]
print(render_movies('piglei', movies))