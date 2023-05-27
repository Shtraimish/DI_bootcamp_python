class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
        
    def __str__(self):
        return f'{self.amount} {self.currency}' + ('s' if self.amount != 1 else '')
    def __int__(self):
        return self.amount
    def __repr__(self):
        return f'{self.amount} {self.currency}'
    def __add__(self, other):
        if isinstance(other, Currency) and self.currency != other.currency:
            raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
        return Currency(self.currency, self.amount + int(other))
    def __iadd__(self, other):
        if isinstance(other, Currency) and self.currency != other.currency:
            raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
        self.amount += int(other)
        return self

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

    
