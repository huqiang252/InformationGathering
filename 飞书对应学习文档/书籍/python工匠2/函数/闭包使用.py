


def counter():
    value = 0
    def _counter():
        # nonlocal 用来标注变量来自上层作用域，如不标明，内层函数将无法直接修改外层函数变量
        nonlocal value
        value += 1
        return value
    return _counter