



import re



_mosaic_char_index = 0

def mosaic_global_var(matchobj):
    """
    将匹配到的模式替换为其他字符，使用全局变量实现轮换字符效果
    """
    global _mosaic_char_index    #为了实现每次调用时轮换马赛克字符，小R可以直接定义一个全局变量_mosaic_char_index
    mosaic_chars = ['*', 'x']
    char = mosaic_chars[_mosaic_char_index]
    # 递增马赛克字符索引值
    _mosaic_char_index = (_mosaic_char_index + 1) % len(mosaic_chars)
    length = len(matchobj.group())
    return char * length


def mosaic_string(string):
    '''用*替换输入字符里面所有的连续数字'''
    return re.sub(r'\d+', mosaic_global_var, string)


if __name__ == '__main__':
    print(mosaic_string('商店共100个苹果，小明以12元每斤的价格买走了8个'))  #商店共***个苹果，小明以xx元每斤的价格买走了*个
    print(mosaic_string('商店共100个苹果，小明以12元每斤的价格买走了8个'))  #商店共xxx个苹果，小明以**元每斤的价格买走了x个
    print(mosaic_string('商店共100个苹果，小明以12元每斤的价格买走了8个'))  #商店共***个苹果，小明以xx元每斤的价格买走了*个


