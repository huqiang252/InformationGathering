def gan_sacraies(root_max):
    for i in range(root_max):
        yield i ** 2



for i in gan_sacraies(100000):
    print(i)