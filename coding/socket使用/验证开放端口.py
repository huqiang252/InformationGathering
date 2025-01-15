#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2025/1/12
# 文件名称   ：验证开放端口.py


import socket

def scan_ports(host, start_port, end_port):
    """
    扫描指定主机的端口范围，返回开启的端口列表。

    参数:
    host (str): 主机地址（IP 地址或域名）。
    start_port (int): 开始扫描的端口号。
    end_port (int): 结束扫描的端口号。

    返回:
    list: 开启的端口号列表。
    """
    open_ports = []
    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)  # 设置超时时间
                result = s.connect_ex((host, port))
                if result == 0:
                    open_ports.append(port)
        except Exception as e:
            print(f"Error scanning port {port}: {e}")
    return open_ports

# 示例使用
if __name__ == "__main__":
    host = '120.77.112.223'  # 替换为你要扫描的主机地址
    start_port = 8888
    end_port = 8890
    open_ports = scan_ports(host, start_port, end_port)
    print(f"Open ports on {host}: {open_ports}")
