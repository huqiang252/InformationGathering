#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
import time
import json
from config import setting

from hstongStockApi.hst_api.financesClass import *
from hstongStockApi.hst_api.hqClass import *




THREAD_NUM = 10  #线程数量
ONE_WORKER_NUM = 50  #每次循环数量
sum_time= 0.0
success_count = 0

sid = setting.SID  #从配置出获取到SID


def send_hstApi():
    global sum_time
    global success_count
    global sid



    t1 =time.time()
    buzz ={"securityCode":"JD","startTime":"","dataType":20000}
    res=ApiHqAllDayQueryFiveAllDayMinute().set_buzz(buzz,sid).run()
    assert res.get_response().status_code==200 #状态码
    bcan=res.extract("json().data.bcan")
    t2 = time.time()
    res_time = t2 - t1
    print(f"成功请求响应时间：{res_time},当前bcan值：{bcan}")
    sum_time=sum_time+res_time
    success_count=success_count+1

def working():
    global ONE_WORKER_NUM
    for i in range(0,ONE_WORKER_NUM):
        send_hstApi()


def main():
    global THREAD_NUM
    Threads = []
    for i in range(THREAD_NUM):
        t = threading.Thread(target=working,name= "T"+str(i))
        t.setDaemon(True)
        Threads.append(t)
    for t in Threads:
        t.start()
    for t in Threads:
        t.join()

if __name__ == '__main__':
    main()
    print(f"并发请求数量：{THREAD_NUM*ONE_WORKER_NUM}")
    print(f"成功请求数量：{success_count}")
    print(f"成功率：{(success_count)*100/(THREAD_NUM*ONE_WORKER_NUM)}%")
    print(f"成功总响应时间：{sum_time}")
    print(f"成功平均响应时间：{sum_time/success_count}")
    print(f"TPS:{(success_count)/(sum_time/success_count)}")
