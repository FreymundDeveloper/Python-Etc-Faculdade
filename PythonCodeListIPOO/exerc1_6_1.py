class Ret:
    comp = None
    lar = None

    def __init__(self, comp, lar):
        self.comp = comp
        self.lar = lar

    def mvdl(self, comp, lar):
        self.comp = comp
        self.lar = lar

    def rvdl(self):
        return self.comp, self.lar

    def ca(self):
        return self.comp * self.lar

    def cp(self):
        return self.comp * 2 + self.lar * 2


area = Ret(0, 0)
piso = Ret(0, 0)
rodapes = Ret(0, 0)
area.mvdl(float(input('Digite o comprimento sala:')), float(input('\nDigite a largura da sala:')))
rodapes.mvdl(float(input('\nDigite o comprimento do rodape:')), float(input('\nDigite a largura do rodape:')))
piso.mvdl(float(input('\nDigite o comprimento do piso:')), float(input('\nDigite a largura do piso:')))
print('Rodapes necessarios:', area.cp()/rodapes.comp)
print('Pisos necessarios:', area.ca()/piso.ca())
