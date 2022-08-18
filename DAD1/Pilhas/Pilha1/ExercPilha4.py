class Pilha:
    _pilha = None
    _pinvs = None

    def __init__(self):
        self._pilha = []
        self._pinvs = []

    def push(self, palavra):
        y = list(palavra)
        x = 0
        while x < len(y):
            self._pilha.append(y[x])
            x += 1

        x = len(self._pilha)

        while x > 0:
            self._pinvs.append(self._pilha[x - 1])
            x -= 1

        if self._pilha == self._pinvs:
            return True

        else:
            return False


################################################################

p = Pilha()

print(p.push(input('Digite uma palavra: ')))
