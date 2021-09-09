class Pilha:
    _pilha = None
    _pinvs = None

    def __init__(self):
        self._pilha = []
        self._pinvs = []

    def push(self, letra):
        self._pilha.append(letra)

    def invs(self):
        x = len(self._pilha)

        while x > 0:
            self._pinvs.append(self._pilha[x - 1])
            x -= 1

        return self._pinvs


###################################################################

p = Pilha()

while True:
    op = int(input('\n1)Empilhar letras;\n2)Reversao:\n3)Sair:\n '))

    if op is 1:
        n = int(input('Quantas letras deseja impilhar: '))
        for i in range(n):
            p.push(input('Digite uma letra:'))

    elif op is 2:
        print(p.invs())

    elif op is 3:
        break

    else:
        print('OPÇ invalida')
