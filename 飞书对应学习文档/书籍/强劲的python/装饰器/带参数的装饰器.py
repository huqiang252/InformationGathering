def add(increment):
    def decorator(func):
        def wrapper(n):
            return func(n) + increment
        return wrapper

    return decorator


@add(1)
def foo(x):
    return x + 2


@add(6)
def bar(n):
    return n + 3


print(foo(1))  # 4
print(bar(4))  # 13
