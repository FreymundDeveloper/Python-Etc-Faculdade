class Quad:
    tm = None

    def __init__(self, tm):
        self.tm = tm

    def mvdl(self, tm):
        self.tm = tm

    def rvl(self, tm):
        return self.tm

    def aq(self, tm):
        return self.tm * self.tm


q = Quad(None)
q.mvdl(float(input('Digite o valor do lado:')))
print(q.rvl(float()))
print(q.aq(float))
