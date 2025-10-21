def printlog(func):
    def wrapper(*args, **kwargs):
        print(F"CALING:{func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@printlog
def foo(x):
    return x+2

@printlog
def baz(x,y):
    return x+y

print(foo(4))
print(baz(4,5))