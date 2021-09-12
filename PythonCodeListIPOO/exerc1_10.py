class BV:
    nome = None
    fome = None
    saude = None
    idade = None

    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def an(self, nome):
        self.nome = nome

    def ran(self):
        return self.nome

    def af(self, fome):
        self.fome = fome

    def raf(self):
        return self.fome

    def asa(self, saude):
        self.saude = saude

    def rasa(self):
        return self.saude

    def ai(self, idade):
        self.idade = idade

    def rai(self):
        return self.idade

    def rh(self):
        return (self.saude + self.fome) / 2


bb = BV(None, None, None, None)
bb.nome = input('Digite o  nome:')
bb.fome = float(input('digite a fome:'))
bb.saude = float(input('Digite a saude:'))
bb.idade = int(input('Digite a idade:'))
bb.an(input('Digite o novo nome:'))
bb.af(float(input('Digite a nova fome:')))
bb.asa(float(input('Digite a nova saude:')))
bb.ai(int(input('Digite a nova idade')))
print('Nome: %s \n Fome: %2.f \n Saude: %2.f \n Idade: %i \n Humor: %2.f' % (bb.ran(), bb.raf(), bb.rasa(), bb.rai(), bb.rh()))
