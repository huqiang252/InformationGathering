# 生成器推导
NUM_SQUARES = 10
many_squares = (n * n for n in range(NUM_SQUARES))


# 等价于如下代码
def gan_many_squares(limit):
    for n in range(limit):
        yield n * n


many_squares = gan_many_squares(NUM_SQUARES)
