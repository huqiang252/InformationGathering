#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/26

def user_get_tweets(user):
    """获取用户已发布状态"""
    if user.profile.show_random_tweets:
        return get_random_tweets(user)
    if user.profile.hide_tweets:
        return [NULL_TWEET_PLACEHOLDER]
    # 最新状态需要用token 从其他服务获取，并转换格式
    token = user.get_token()
    latest_tweets = get_latest_tweets(token)
    return [transorm_tweet(item) for item in latest_tweets]