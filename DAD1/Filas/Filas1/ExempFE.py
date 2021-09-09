class Node:
    def __init__(self):
        self.__valor = 0
        self.__prox = None

    def setValor(self, valor):
        self.__valor = valor

    def getValor(self):
        return self.__valor

    def setProx(self, p):
        self.__prox = p

    def getProx(self):
        return self.__prox


class Fila:
    def __init__(self):
        self.__valorTotal = 0
        self.__ini = None
        self.__fim = None
        self.__valorTotal = 0
        self.__cont = 0

    def push(self):
        novo = Node()
        if novo:
            novo.setValor(int(input('Valor para inserir: ')))
            if self.__fim:
                self.__fim.setProx(novo)
                self.__fim = novo
                self.__valorTotal += novo.getValor()
                self.__cont += 1
            else:
                self.__ini = self.__fim = novo
                self.__valorTotal += novo.getValor()
                self.__cont += 1

    def pop(self):
        if self.__ini:
            self.__valorTotal -= self.__ini.getValor()
            self.__cont -= 1
            self.__ini = self.__ini.getProx()
            if not self.__ini:
                self.__fim = None
        else:
            print('Fila vazia...')

    def printall(self):
        if self.__fim:
            saida = '\nFila:\n'
            temp = self.__ini
            while temp:
                saida += str(temp.getValor()) + '\t'
                temp = temp.getProx()
            print(saida)
        else:
            print('\nFila vazia...')

    def media(self):
        print(self.__valorTotal/self.__cont)


f = Fila()
while True:
    op = int(input('\nMenu\n1-Ler\n2-Excluir\n3-Imprimir\n4-Média\n5-Sair\nOpção: '))
    if op is 1:
        f.push()
    elif op is 2:
        f.pop()
    elif op is 3:
        f.printall()
    elif op is 4:
        f.media() 
    elif op is 5:
        break
    else:
        print('Opção inválida...')
