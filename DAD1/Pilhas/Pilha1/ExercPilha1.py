class Pilha:
    _pilha = None

    def __init__(self):
        self._pilha = []

    def push(self, letra):
        self._pilha.append(letra)

    def pop(self):
        if self._pilha:
            del self._pilha[len(self._pilha) - 1]
        else:
            print('Pilha vazia')

    def ler(self):
        i = 1
        while i <= len(self._pilha):
            print(self._pilha[-i])
            i += 1


##################################################################

p = Pilha()

while True:
    op = int(input('\n1)Empilha\n2)Desempilha\n3)Ler\n4)Sair:'))
    if op is 1:
        n = int(input('Quantas letras vc deseja empilhar: '))
        for i in range(n):
            p.push(input('Digite uma letra para empilhar: '))
    elif op is 2:
        p.pop()
    elif op is 3:
        p.ler()
    elif op is 4:
        break
    else:
        print('Opç invalida')