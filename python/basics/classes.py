class Money (object):
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return str(self.amount) + ' ' + self.currency

# create a new instance of class
money = Money(220, 'EUR')
money.amount, money.currency
# (220, 'EUR')

print(money)
# 220 EUR

# subclasses
class VirtualMoney (Money):
    def __init__(self, date):
        self.date = date

    def __str__(self):
        return str(self.amount) + ' ' + self.currency + ' (use before ' + self.date + ')'

virtual_money = VirtualMoney('2018-12-31')
virtual_money.amount = 20
virtual_money.currency = 'DIS'

print(virtual_money)
# 20 DIS (use before 2018-12-31)