class Add:
    def __init__(self, increment):
        self.increment = increment
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) + self.increment
        return wrapper

@Add(5)
def foo(x):
    return x + 2

@Add(10)
def bean(n):
    return n+1

print(foo(1))
print(bean(4))


