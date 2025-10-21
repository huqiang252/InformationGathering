class PrintLog:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'CALLING:{self.func.__name__}')
        return self.func(*args, **kwargs)


@PrintLog
def foo(x):
    return x + 2


print(foo(1))
