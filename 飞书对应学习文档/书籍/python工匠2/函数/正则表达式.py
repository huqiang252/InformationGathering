



import re

def make_cyclic_mosaic():
    """
    将匹配到的模式替换为其他字符，使用闭包实现轮换字符效果
    """
    char_index = 0
    mosaic_chars = ['*', 'x']
    def _mosaic(matchobj):
        nonlocal char_index  # nonlocal 用来标注变量来自上层作用域，如不标明，内层函数将无法直接修改外层函数变量
        char = mosaic_chars[char_index]
        char_index = (char_index + 1) % len(mosaic_chars)
        length = len(matchobj.group())
        return char * length
    return _mosaic


def mosaic_string(string):
    '''用*替换输入字符里面所有的连续数字'''

    #此处是make_cyclic_mosaic()而不是make_cyclic_mosaic，因为make_cyclic_mosaic()函数的调用结果才是真正的替换函数
    return re.sub(r'\d+', make_cyclic_mosaic(), string)  #


if __name__ == '__main__':
    print(mosaic_string('商店共100个苹果，小明以12元每斤的价格买走了8个'))  #商店共***个苹果，小明以xx元每斤的价格买走了*个
    print(mosaic_string('商店共100个苹果，小明以12元每斤的价格买走了8个'))  #商店共***个苹果，小明以xx元每斤的价格买走了*个
    print(mosaic_string('商店共100个苹果，小明以12元每斤的价格买走了8个'))  #商店共***个苹果，小明以xx元每斤的价格买走了*个


