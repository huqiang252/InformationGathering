#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-10-28
class MediaManager:
    def get_files(self, dir_path, recursive=True, extensions=[]):
        '''
        :param dir_path: the directory path
        :param recursive: if to search files recursively into subdirectories
        :param extensions: filter for interested file types, leave it empty to
            get files of any type.
        :return: the file paths
        '''
        pass

    def get_video_files(self, dir_path, recursive=True):
        return self.get_files(dir_path, recursive, ['.avi', '.mpg', '.mov'])