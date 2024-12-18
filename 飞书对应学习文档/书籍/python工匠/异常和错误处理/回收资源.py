#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/24
#经典的方式
conn = create_conn(host, port, timeout=None)
try:
    conn.send_text('Hello, world!')
except Exception as e:
    print(f'Unable to use connection: {e}')
finally:
    conn.close()


class create_conn_obj:
    """创建连接对象，并在退出上下文时自动关闭"""
    def __init__(self, host, port, timeout=None):
        self.conn = create_conn(host, port, timeout=timeout)
    def __enter__(self):
        return self.conn
    def __exit__(self, exc_type, exc_value, traceback):
        # __exit__会在管理器退出时调用
        self.conn.close()
        return False


if __name__ == '__main__':
    # 使用上下文管理器创建连接
    with create_conn_obj( host, port, timeout=None ) as conn:
        try:
            conn.send_text( 'Hello, world!' )
        except Exception as e:
            print( f'Unable to use connection: {e}' )