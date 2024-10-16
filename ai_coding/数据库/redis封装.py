#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-07-24

from rediscluster import RedisCluster
# from scripts.utils.log import Log

class RedisClusterClient:
    def __init__(self, startup_nodes, decode_responses=True):
        self.startup_nodes = startup_nodes
        self.decode_responses = decode_responses
        self.client = RedisCluster(startup_nodes=self.startup_nodes, decode_responses=self.decode_responses)
    def get(self, key):
        return self.client.get(key)

    def set(self, key, value, ex=None, px=None, nx=False, xx=False):
        return self.client.set(key, value, ex=ex, px=px, nx=nx, xx=xx)

    def delete(self, *keys):
        return self.client.delete(*keys)

    def incr(self, key, amount=1):
        return self.client.incr(key, amount)

    def decr(self, key, amount=1):
        return self.client.decr(key, amount)

    def expire(self, key, seconds):
        return self.client.expire(key, seconds)

    def ttl(self, key):
        return self.client.ttl(key)

    def hset(self, name, key, value):
        return self.client.hset(name, key, value)

    def hmget(self,name,keys,*args):
        return self.client.hmget(name,keys,*args)

    def hget(self, name, key):
        return self.client.hget(name, key)

    def hgetall(self, name):
        return self.client.hgetall(name)

    def hdel(self, name, *keys):
        return self.client.hdel(name, *keys)

    def keys(self,pattern,**kwargs):
        return self.client.keys(pattern,**kwargs)

    def hkeys(self,name)->list:
        return self.client.hkeys(name)

    def hlen(self,key)->int:
        return self.client.hlen(key)


if __name__ == '__main__':
    # 示例用法
    startup_nodes = [
        {"host": "127.0.0.1", "port": 7000},
        {"host": "127.0.0.1", "port": 7001},
        {"host": "127.0.0.1", "port": 7002}
    ]
    redis_client = RedisClusterClient(startup_nodes)
    redis_client.set("key", "value")
    value = redis_client.get("key")
    print(value)  # 输出: 'value'