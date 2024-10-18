#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-10-18
json = {
    "01": [{"picname": "01_sseye.png", "主观评分": "7", "主观评价": "ok"}, {"picname": "01_ueeye.png", "主观评分": "8", "主观评价": "眼球"}],
    "02": [{"picname": "02_sshair.png", "主观评分": "5", "主观评价": "ok"}, {"picname": "02_uehair.png", "主观评分": "9", "主观评价": "ok"}]
}

if __name__ == '__main__':
    import pandas

    # 将value组成新的list
    newList = []
    for value in json.values():
        newList = newList + value

    print(newList)  # [{'picname': '01_sseye.png', '主观评分': '7', '主观评价': 'ok'}, {'picname': '01_ueeye.png', '主观评分': '8', '主观评价': '眼球'}, {'picname': '02_sshair.png', '主观评分': '5', '主观评价': 'ok'}, {'picname': '02_uehair.png', '主观评分': '9', '主观评价': 'ok'}]

    # 满足pandas二维数组
    pd = pandas.DataFrame( newList )

    # 按照要求设置标题
    pd.columns = ['', '主观评分', '主观评价']
    pd.to_csv( 'example.csv', index=False )  # index=False不写行号
