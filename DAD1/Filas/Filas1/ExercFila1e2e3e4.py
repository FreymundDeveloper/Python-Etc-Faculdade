from datetime import date


class Fila:

    def __init__(self):
        self.__fila = []
        self.__fila2 = []

    def push(self):
        dd = input('Nome: ')
        dd2 = input('Data de nascimento: ')
        nasc = 2020 - int(dd2[6:10])
        dados = dd + ' - ' + str(nasc)
        self.__fila.append(dados)
        Fila.printall(self)

    def pop(self):
        if self.__fila:
            del self.__fila[0]
            Fila.printall(self)

        else:
            print('Fila vazia')

    def printall(self):
        if not self.__fila:
            print('Fila vazia')

        else:
            saida = ''
            fila_aux = []
            while self.__fila:
                saida += self.__fila[0] + ' anos\t\t'
                fila_aux.append(self.__fila[0])
                del self.__fila[0]
            print('\nNomes:\n' + saida)
            self.__fila = fila_aux

    def pelemt(self):
        if self.__fila:
            print(self.__fila[0])

        else:
            print('Fila vazia')

    def popall(self):
        if self.__fila:
            while self.__fila:
                del self.__fila[0]

                if not self.__fila:
                    print('Fila esvaziada')

        else:
            print('Fila vazia')


##################################################################################################################
f = Fila()

while True:
    op = int(input('1)Inserir nome e data de nascimento\n2)Excluir\n3)Imprimir\n4)Primeiro elemento\n5)Excluir '
                   'Tudo\n6)Sair:'))

    if op is 1:
        f.push()

    elif op is 2:
        f.pop()

    elif op is 3:
        f.printall()

    elif op is 4:
        f.pelemt()

    elif op is 5:
        f.popall()

    elif op is 6:
        break

    else:
        print('Opc invalida')
