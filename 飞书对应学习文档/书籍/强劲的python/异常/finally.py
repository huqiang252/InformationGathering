# fleet_config 是一个对象
# 包含虚拟机运行和连接的细节
fleet = CloudVMFleet(fleet_config)

# job_config 定义了批量计算的类型
job = BatchJob(job_config)

try:
    # .start() 发起 API 调用，以租用虚拟机实例
    # 阻塞虚拟机实例，直到接收任务
    fleet.start()

    # 提交任务，返回 RunningJob
    running_job = fleet.submit_job(job)

    # 等待执行完毕
    running_job.wait()
finally:
    # 释放虚拟机
    # 避免持续付费
    fleet.terminate()
