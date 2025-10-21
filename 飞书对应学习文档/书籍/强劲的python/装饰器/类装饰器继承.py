import sys
class ResultAnnouncer:
    stream = sys.stdout
    prefix = "RESULT"

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        value = self.func(*args, **kwargs)
        self.stream.write(f"{self.prefix}: {value}\n")
        return value


class StdErrResultAnnouncer(ResultAnnouncer):
    stream = sys.stderr
    prefix = "ERROR"



@StdErrResultAnnouncer
def foo(x):
    return x+2

print(foo(1))


