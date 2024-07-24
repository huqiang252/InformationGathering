#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-28
import socket
from urllib.parse import urlparse

class SocketClientError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class SocketClient:
    def __init__(self, url, timeout=10):
        parsed_url = urlparse(url)
        self.host = parsed_url.hostname
        self.port = parsed_url.port or 80  # 如果端口未指定，默认为 80
        self.timeout = timeout
        self.socket = None

    def connect(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(self.timeout)
            self.socket.connect((self.host, self.port))
        except (socket.error, socket.timeout) as e:
            raise SocketClientError(f"连接到 {self.host}:{self.port} 失败: {e}")

    def send(self, request):
        if not self.socket:
            self.connect()
        try:
            self.socket.sendall(request.encode())
        except (socket.error, socket.timeout) as e:
            raise SocketClientError(f"发送数据到 {self.host}:{self.port} 失败: {e}")

    def receive(self):
        if not self.socket:
            raise SocketClientError("未建立连接，无法接收数据")
        try:
            response = b''
            while True:
                data = self.socket.recv(4096)
                if not data:
                    break
                response += data
            return response.decode()
        except (socket.error, socket.timeout) as e:
            raise SocketClientError(f"接收数据从 {self.host}:{self.port} 失败: {e}")

    def close(self):
        if self.socket:
            self.socket.close()
            self.socket = None

