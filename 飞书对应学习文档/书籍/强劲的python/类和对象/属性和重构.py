#版本1
class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents




#重构后
class Money:
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    # dollars 的 getter 和 setter
    @property
    def dollars(self):
        # // 整除
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, new_dollars):
        self.total_cents = 100 * new_dollars + self.cents

    # cents 的 getter 和 setter
    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, new_cents):
        self.total_cents = 100 * self.dollars + new_cents
