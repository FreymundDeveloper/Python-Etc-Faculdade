class Ret:
    base = None
    alt = None

    def __init__(self, base, alt):
        self.base = base
        self.alt = alt

    def mvdl(self, base, alt):
        self.base = base
        self.alt = alt

    def rvdl(self):
        return self.base, self.alt

    def ca(self):
        return self.base * self.alt

    def cp(self):
        return self.base * 2 + self.alt * 2


r = Ret(0, 0)
r.mvdl(float(input('Digite a base:')), float(input('\nDigite a altura:')))
print(r.rvdl())
print(r.ca())
print(r.cp())
