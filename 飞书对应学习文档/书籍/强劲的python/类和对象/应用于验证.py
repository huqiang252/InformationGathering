# 最终版本，修改构造器
# 构造器不同，getter和setter不变
class Ticket:
    def __init__(self, price):
        # instead of "self._price = price"
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        # 只允许正价格
        if new_price < 0:
            raise ValueError("Nice try")
        self._price = new_price



if __name__ == '__main__':
    ticket = Ticket(1)