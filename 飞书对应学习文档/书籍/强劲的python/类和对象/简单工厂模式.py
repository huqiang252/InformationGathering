import re
class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents
    @classmethod
    def from_pennies(cls, total_cents):
        dollars = total_cents // 100
        cents = total_cents % 100
        return cls(dollars, cents)

    @classmethod
    def from_string(cls, amount):
        match = re.search(r'^\$(?P<dollars>\d+)\.(?P<cents>\d\d)$', amount)
        if match is None:
            raise ValueError(f"Invalid amount: {amount}")
        dollars = int(match.group('dollars'))
        cents = int(match.group('cents'))
        return cls(dollars, cents)

page_bank_cash = Money.from_pennies(3217)
print(type(page_bank_cash))  # <class '__main__.Money'>
print(page_bank_cash.dollars)  # 32
print(page_bank_cash.cents)  # 17

page_bank_cash_str = Money.from_string('$32.17')
print(type(page_bank_cash_str))
print(page_bank_cash_str.dollars)
print(page_bank_cash_str.cents)
