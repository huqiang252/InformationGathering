#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-24
import socket
import threading


def receive_data(tcp_client_socket):
    while True:
        recv_data = tcp_client_socket.recv(1024)
        if not recv_data:
            break
        recv_content = recv_data.decode("gbk")
        print("接收服务端的数据为:", recv_content)


def client_handler():
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client_socket.connect(("192.168.0.195", 8888))

    receive_thread = threading.Thread(target=receive_data, args=(tcp_client_socket,))
    receive_thread.start()

    while True:
        send_data = input("请输入要发送的数据：")
        if send_data == "exit":
            break
        tcp_client_socket.send(send_data.encode("gbk"))

    tcp_client_socket.close()


if __name__ == '__main__':
    client_handler()