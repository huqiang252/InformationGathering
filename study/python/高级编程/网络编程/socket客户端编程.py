#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-24
# 导入 socket 模块
import socket

# 创建tcp客户端套接字
# 1. AF_INET：表示ipv4
# 2. SOCK_STREAM: tcp传输协议
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 和服务端应用程序建立连接
tcp_client_socket.connect(("192.168.0.195", 8888))

# 代码执行到此，说明连接建立成功
# 准备发送的数据
send_data = "你好,我是哈利波特!".encode("gbk")
# 向服务端发送数据
tcp_client_socket.send(send_data)

# 从服务端接收数据, 这次接收的数据最大字节数是1024
recv_data = tcp_client_socket.recv(1024)
# 返回的直接是服务端程序发送的二进制数据
print(recv_data)

# 对数据进行解码
recv_content = recv_data.decode("gbk")
print("接收服务端的数据为:", recv_content)

# 关闭套接字
tcp_client_socket.close()
