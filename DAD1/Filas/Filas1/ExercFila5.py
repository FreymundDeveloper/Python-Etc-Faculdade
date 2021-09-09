class Fila:

    def __init__(self):
        self.__fila = []

    def push(self):
        self.__fila.append(int(input('Digite um numero: ')))

    def pop(self):
        if self.__fila:
            del self.__fila[0]

        else:
            print('Fila vazia')

    def printall(self):
        if not self.__fila:
            print('Fila vazia')

        else:
            saida = ''
            fila_aux = []
            while self.__fila:
                saida += str(self.__fila[0]) + '\t'
                fila_aux.append(self.__fila[0])
                del self.__fila[0]
            print('\nNumeros:\n' + saida)
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

    def invert(self):
        self.__fila.reverse()
        print('Pilha invertida')

    def vpi(self):
        par = []
        impar = []
        x = 0

        while x < len(self.__fila):

            if self.__fila[x] % 2 > 0 or self.__fila[x] == 0:
                impar.append(self.__fila[x])

            elif self.__fila[x] % 2 == 0:
                par.append(self.__fila[x])

            x += 1

        print('Par: ', par)
        print('Impar: ', impar)


##################################################################################################################
f = Fila()

while True:
    op = int(input('\n1)Inserir numero ineiro\n2)Excluir\n3)Imprimir\n4)Primeiro elemento\n5)Excluir '
                   'Tudo\n6)Inverter fila\n7)Pares e inpares\n8)Sair:'))

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
        f.invert()

    elif op is 7:
        f.vpi()

    elif op is 8:
        break

    else:
        print('Opc invalida')
