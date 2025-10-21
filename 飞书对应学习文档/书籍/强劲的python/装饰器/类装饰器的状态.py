class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"# of calls: {self.count}")
        return self.func(*args, **kwargs)


@CountCalls
def foo(x):
    return x + 2

print(foo(2))
print(foo(1))
print(foo(4))