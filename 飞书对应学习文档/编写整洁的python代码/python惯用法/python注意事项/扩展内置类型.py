class BadList(list):
    def __getitem__(self, index):
        value = super().__getitem__(index)
        if index % 2 == 0:
            prefix = "even"
        else:
            prefix = "odd"
        return f"[{prefix}] {value}"



from collections import UserList

class GoodList(UserList):
    def __getitem__(self, index):
        value = super().__getitem__(index)
        if index % 2 == 0:
            prefix = "even"
        else:
            prefix = "odd"
        return f"[{prefix}] {value}"


if __name__ == '__main__':
    b = BadList([1, 2, 3, 4, 5])
    print(b[0])  #[even] 1
    print(b[1]) # [odd] 2
    # print("".join(b))  #TypeError: sequence item 0: expected str instance, int found

    print("====================")
    g = GoodList([1, 2, 3, 4, 5])
    print(g[0])  #[even] 1
    print(g[1]) # [odd] 2
    print("".join(g))  #[even] 1[odd] 2[even] 3[odd] 4[even] 5
