# collectstats 类似于 running_average
# 但支持直接访问并打印 data 字典
def collectstats(func):
    data = {"total": 0, "count": 0}
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        data["total"] += val
        data["count"] += 1
        return val
    wrapper.data = data
    return wrapper

@collectstats
def foo(x):
    return x+2


print(foo.data) #{'total': 0, 'count': 0}
foo(1)
print(foo.data) #{'total': 3, 'count': 1}
foo(2)
print(foo.data) #{'total': 7, 'count': 2}