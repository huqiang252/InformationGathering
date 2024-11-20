#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/19


from jinja2 import Template
_MOVIES_TMPL = '''\
Welcome, {{username}}.
{%for name, rating in movies %}
* {{ name }}, Rating: {{ rating|default("[NOT RATED]", True) }}
{%- endfor %}
'''

def render_movies_j2(username, movies):
    tmpl = Template(_MOVIES_TMPL)
    return tmpl.render(username=username, movies=movies)


movies = [
    ('The Shawshank Redemption', '9.3'),
    ('The Prestige', '8.5'),
    ('Mulan', None),
]
print(render_movies_j2('piglei', movies))