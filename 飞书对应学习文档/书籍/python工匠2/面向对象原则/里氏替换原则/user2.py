#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/2
# 文件名称   ：user2.py


class User(Model):
    """普通用户类"""
    ...
    def list_related_posts(self) -> List[int]:
        """查询所有与之相关的帖子 ID"""
        return [
            post.id
            for post in session.query(Post).filter(username=self.username)
        ]


class Admin(User):
    """管理员用户类"""
    ...
    def list_related_posts(self) -> Iterable[int]:
        # 管理员与所有帖子都有关，为了节约内存，使用生成器返回结果
        for post in session.query(Post).all():
            yield post.id



def get_user_posts_count(user: User) -> int:
    """获取与用户相关的帖子数量"""
    return len(user.list_related_posts())\



