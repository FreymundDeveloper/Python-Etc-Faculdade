class Pilha:
    def __init__(self):
        self.__pilhaCPF = []

        self.__pilhaNome = []

    def push(self):
        self.__pilhaNome.append(input('Digite seu nome: '))
        self.__pilhaCPF.append(input('Digite o seu CPF: '))

    def pop(self):
        if self.__pilhaNome:
            del self.__pilhaNome[len(self.__pilhaNome) - 1]
            del self.__pilhaCPF[len(self.__pilhaCPF) - 1]
        else:
            print('Pilha vazia')

    def imprimetopo(self):
        if self.__pilhaNome:
            print('Nome: ', self.__pilhaNome[len(self.__pilhaNome) - 1])
            print('CPF: ', self.__pilhaCPF[len(self.__pilhaCPF) - 1])

    def imprimetudo(self):
        if self.__pilhaNome:
            i = 1
            while i <= len(self.__pilhaNome):
                print('Nome: ', self.__pilhaNome[-i], '\nCPF: ', self.__pilhaCPF[-i], '\n')
                i += 1

        else:
            print('Pilha Vazia')


p = Pilha()

while True:

    op = int(input("\n1-Empilhar\n2–Desempilhar\n3-ImprimeTopo\n4-ImprimePilha\n5-Sair\nOpção: "))

    if op is 1:

        p.push()

    elif op is 2:

        p.pop()

    elif op is 3:

        p.imprimetopo()

    elif op is 4:

        p.imprimetudo()

    elif op is 5:

        break

    else:
        print('OPC Invalidada')