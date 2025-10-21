def running_average(func):
    data = {"total": 0, "count": 0}
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        data["total"] += val
        data["count"] += 1
        print("Average of {} so far: {:.1f}".format(
            func.__name__, data["total"] / data["count"])
        )
        return val
    return wrapper

@running_average
def foo(x):
    return x+2


print(foo(1))
print(foo(10))
print(foo(1))
print(foo(1))