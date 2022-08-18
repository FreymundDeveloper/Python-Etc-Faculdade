from random import randint
import sys


class No:
    def __init__(self):
        self.__valor = None
        self.__prox = None

    def setV(self, v):
        self.__valor = v

    def setP(self, p):
        self.__prox = p

    def getV(self):
        return self.__valor

    def getP(self):
        return self.__prox


class Fila:
    def __init__(self):
        self.__fim = None

    def push(self, valor):
        new = No()
        if new:
            new.setV(valor)
            if self.__fim:
                new.setP(self.__fim.getP())
                self.__fim.setP(new)
                self.__fim = new
            else:
                self.__fim = new
                self.__fim.setP(new)

    def pop(self):
        if self.__fim.getP() is not self.__fim:
            self.__fim.setP(self.__fim.getP().getP())
        else:
            self.__fim = None

    def print_all(self):
        if self.__fim:
            saida = 'Fila: \n'
            temp = self.__fim.getP()
            while temp:
                saida += str(temp.getV()) + '\t'
                if temp.getP() == self.__fim.getP():
                    break
                temp = temp.getP()
            print(saida)
        else:
            print('Fila vazia.')

    def cassino(self, num, premio):
        if self.__fim:
            temp = self.__fim.getP()
            usuario = str(temp.getV())
            termos = usuario.split()
            nome = termos[0]
            valor = float(termos[1])

            if valor <= 5:
                print('Participante %s não tinha dinheiro suficiente' % nome)
                self.pop()

            elif num == premio:
                print(' %s GANHOU!!!' % nome)
                sys.exit()

            else:
                print(' %s Não ganhou...' % nome)
                valor -= 5.0
                if valor > 5:
                    usuario = nome + ' ' + str(valor)
                    self.push(usuario)
                    self.pop()

                else:
                    self.pop()
        else:
            print("Fila vazia.")


f = Fila()
num = 1
premio = randint(1, 10)

while True:
    op = int(input('1)Entra participante\n2)Verificar atual lista de participantes\n3)Jogar\n4)Sair:'))

    if op is 1:
        f.push(input('Digite seu nome e o valor q quer apostar(Nome(ESPAÇO)Valor): '))

    elif op is 2:
        f.print_all()

    elif op is 3:
        f.cassino(num, premio)
        num += 1

    elif op is 4:
        sys.exit()

    else:
        print('Opc Invalida')
