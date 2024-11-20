#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/10
import requests
# 引入Http请求模块
from threading import Thread
# 引入线程模块

class DownloadThread (Thread):
    """下载文件的线程"""

    # 每次写文件的缓冲大小
    CHUNK_SIZE = 1024 * 512

    def __init__(self, fileName, url, savePath, callBackProgerss, callBackFinished):
        super().__init__()
        self.__fileName = fileName
        self.__url = url
        self.__savePath = savePath
        self.__callbackProgress = callBackProgerss
        self.__callBackFionished = callBackFinished

    def run(self):
        readSize = 0
        r = requests.get(self.__url, stream=True)
        totalSize = int(r.headers.get('Content-Length'))
        print(f"[下载{self.__fileName}] 文件大小:{totalSize}")
        with open(self.__savePath, "wb") as file:
            for chunk in r.iter_content(chunk_size = self.CHUNK_SIZE):
                if chunk:
                    file.write(chunk)
                    readSize += self.CHUNK_SIZE
                    self.__callbackProgress(self.__fileName, readSize, totalSize)
        self.__callBackFionished(self.__fileName)


def myDownload():
    def downloadProgress(fileName, readSize, totalSize):
        """定义下载进度的回调函数"""
        percent = (readSize / totalSize) * 100
        print("[下载%s] 下载进度:%.2f%%" % (fileName, percent))

    def downloadFinished(fileName):
        """定义下载完成后的回调函数"""
        print("[下载%s] 文件下载完成！" % fileName)

    print("开始下载TestForDownload1.pdf......")
    downloadUrl1 = "http://pe9hg91q8.bkt.clouddn.com/TestForDownload1.pdf"
    download1 = DownloadThread("TestForDownload1", downloadUrl1, "./download/TestForDownload1.pdf", downloadProgress,
                               downloadFinished)
    download1.start()
    print("开始下载TestForDownload2.zip......")
    downloadUrl2 = "http://pe9hg91q8.bkt.clouddn.com/TestForDownload2.zip"
    download2 = DownloadThread("TestForDownload2", downloadUrl2, "./download/TestForDownload2.zip", downloadProgress,
                               downloadFinished)
    download2.start()
    print("执行其它的任务......")


myDownload()