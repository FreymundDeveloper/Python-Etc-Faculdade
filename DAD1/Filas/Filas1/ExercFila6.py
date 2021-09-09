class Qsix:
    __pilha = None
    __filap = None
    __filai = None

    def __init__(self):
        self.__pilha = []
        self.__filap = []
        self.__filai = []

    def push(self):
        x = -1

        while True:
            x = int(input('Digite um numero: '))
            if x == 0:
                break
            else:
                self.__pilha.append(x)

    def org(self):
        if not self.__pilha:
            print('pilha vazia')

        else:
            x = len(self.__pilha) - 1
            while x >= 0:
                if self.__pilha[x] % 2 > 0:
                    self.__filai.append(self.__pilha[x])

                elif self.__pilha[x] % 2 == 0:
                    self.__filap.append(self.__pilha[x])

                x -= 1

    def retn(self):
        Qsix.org(self)

        i = 1
        print('Pilha:')
        while i <= len(self.__pilha):
            print(self.__pilha[-i])
            i += 1

        if self.__filap:
            print('Par: ', self.__filap)

        else:
            print('Fila par vazia')

        if self.__filai:
            print('Impar: ', self.__filai)

        else:
            print('Fila impar vazia')


#####################################################################################################################
f = Qsix()

while True:
    op = int(input('\n1)Entar valor\n2)Sair: '))

    if op is 1:
        f.push()

    elif op is 2:
        f.retn()
        break
