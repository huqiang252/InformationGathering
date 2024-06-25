#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-24
import socket
import threading

class MultiTaskTCPServer(object):
    # 在初始化方法中对服务端socket进行初始化操作
    def __init__(self,ip="", port=8888):
        # 创建tcp服务端套接字
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置端口号复用，让程序退出端口号立即释放
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定端口号
        self.server.bind((ip, port))
        # 设置监听, listen后的套接字是被动套接字，只负责接收客户端的连接请求
        self.server.listen(128)

    # 启动服务器方法，实现多任务接受处理客户端连接请求
    def run(self):
        # 循环等待接收客户端的连接请求
        while True:
            # 等待接收客户端的连接请求
            client_socket, ip_port = self.server.accept()
            print("客户端连接成功:", ip_port)
            # 当客户端和服务端建立连接成功以后，需要创建一个子线程，不同子线程负责接收不同客户端的消息
            sub_thread = threading.Thread(target=self.handle_client_request, args=(client_socket, ip_port))
            # 设置守护主线程
            sub_thread.setDaemon(True)
            # 启动子线程
            sub_thread.start()

        # tcp服务端套接字可以不需要关闭，因为服务端程序需要一直运行
        tcp_server_socket.close()

    # 处理客户端的请求操作
    def handle_client_request(self, client, ip_port):
        # 接收客户端发送的数据并解码
        recv_data = client.recv(1024).decode("gbk")
        # 如果接收的数据长度为0，说明客户端主动断开了连接
        if len(recv_data) == 0:
            print("客户端下线了:", ip_port)
            return

        print(recv_data, ip_port)
        # 将客户端发送的数据转换成大写并编码后发送给客户端
        send_data = recv_data.upper().encode("gbk")
        client.send(send_data)

        # 终止和客户端进行通信
        client.close()


if __name__ == '__main__':
    # 创建服务器对象
    server = MultiTaskTCPServer(port=9999)
    # 启动服务器
    server.run()
