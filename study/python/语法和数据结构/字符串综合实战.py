#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-07-28
story = "Once upon a time, in a land far away, lived a brave knight named Arthur."

# 统计故事中的单词数量
word_count = len(story.split())
print("单词数量:", word_count)

# 查找主人公的名字在故事中的位置
hero_name = "Arthur"
hero_position = story.find(hero_name)
print("主人公姓名在故事中的位置:", hero_position)

# 将主人公的名字替换为你的名字
your_name = "Alice"
new_story = story.replace(hero_name, your_name)
print("替换名字后:", new_story)

# 将故事改写为大写和小写形式
uppercase_story = story.upper()
lowercase_story = story.lower()
print("大写:", uppercase_story)
print("小写:", lowercase_story)
