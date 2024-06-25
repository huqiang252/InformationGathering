#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-24
import socket

# 创建tcp服务端套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置端口号复用，让程序退出端口号立即释放
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# 给程序绑定端口号
tcp_server_socket.bind(("", 8888))
# 设置监听
tcp_server_socket.listen(128)
print("服务端启动成功，等待客户端连接。。。")
# 等待客户端建立连接的请求, 只有客户端和服务端建立连接成功代码才会解阻塞，代码才能继续往下执行
# 1. 专门和客户端通信的套接字： client_socket
# 2. 客户端的ip地址和端口号： ip_port
client_socket, ip_port = tcp_server_socket.accept()
# 代码执行到此说明连接建立成功
print("客户端的ip地址和端口号:", ip_port)
# 接收客户端发送的数据, 这次接收数据的最大字节数是1024
recv_data = client_socket.recv(1024)
# 获取数据的长度
recv_data_length = len(recv_data)
print("接收数据的长度为:", recv_data_length)
# 对二进制数据进行解码
recv_content = recv_data.decode("gbk")
print("接收客户端的数据为:", recv_content)
# 准备发送的数据
send_data = f"你好,{ip_port[0]}".encode("gbk")
# 发送数据给客户端
client_socket.send(send_data)
# 关闭服务与客户端的套接字， 终止和客户端通信的服务
client_socket.close()
# 关闭服务端的套接字, 终止和客户端提供建立连接请求的服务
tcp_server_socket.close()
