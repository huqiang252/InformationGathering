def get_nums():
    n = 0
    while n < 4:
        yield n
        n +=1

    yield 48

for i in get_nums():
    print(i)
