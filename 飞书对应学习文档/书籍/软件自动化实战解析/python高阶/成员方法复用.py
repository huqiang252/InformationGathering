#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/27

class Parent:
    def draw_dragon(self):
        print('\r\nDraw a dragon')
        print('\tdraw the head')
        print('\tdraw the body')
        print('\tdraw the tail')
        print('\tdraw the claws')

class Child(Parent):
    def draw_dragon(self):
        super().draw_dragon()
        print('\tdraw the eyes')

artists = [Parent(), Child()]
for artist in artists:
    artist.draw_dragon()