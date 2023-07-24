# class
class Money(object):
    # constructor
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    # string representation
    def __str__(self):
        return f"{self.amount} {self.currency}"

# create new instance of class
money = Money(220, "EUR")
money.amount, money.currency

print(money)
# 220 EUR
print(money.amount, money.currency)
# 220 EUR

# subclass
class VirtualMoney(Money):
    def __init__(self, date):
        self.date = date
        # inherits amount and currency from Money

    # override string representation
    def __str__(self):
        return f"{self.amount} {self.currency} (expire: {self.date})"

# create new instance of subclass
virtual_money = VirtualMoney("2018-12-31")
virtual_money.amount = 20
virtual_money.currency = "V-Bucks"

print(virtual_money)
# 20 V-Bucks (expire: 2018-12-31)