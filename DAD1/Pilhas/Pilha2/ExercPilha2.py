class No_pilha:
    _nome = None
    _proximo = None

    def __init__(self):
        self._nome = ''
        self._proximo = None

    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

    def getProximo(self):
        return self._proximo

    def setProximo(self, prox):
        self._proximo = prox


class Pilha:
    def __init__(self):
        self._topo = None
        self._midd = 0
        self._idd = 0

    def push(self):
        temp_no = No_pilha()
        nome = 'Nome:'

        if temp_no:
            nome += input('Entre com um nome: ')
            nome += '   Idade:'
            self._idd = int(input('Entre com a idade: '))
            self._midd += self._idd
            nome += str(self._idd)
            temp_no.setNome(nome)
            temp_no.setProximo(self._topo)  #
            self._topo = temp_no  #

    def pop(self):
        if self._topo:
            print('\nValor a remover: ', self._topo.getNome())
            self._topo = self._topo.getProximo()  #
            self._midd -= self._idd

        else:
            print('Pilha vazia')

    def printall(self):

        if not self._topo:
            print('Pilha vazia')
            return
        temp_no = self._topo
        saida = 'Pilha:\n'

        while temp_no:
            saida += str(temp_no.getNome()) + '\n'
            temp_no = temp_no.getProximo()
        print(saida)

    def last(self):  # A
        if self._topo:
            print(self._topo.getNome())

        else:
            print('Pilha vazia')

    def med(self):

        if not self._topo:
            print('Pilha vazia')

        cont = 0
        tem_po = self._topo

        while tem_po:
            tem_po.getNome()
            tem_po = tem_po.getProximo()
            cont += 1
        print(self._midd / cont)


p = Pilha()

while True:
    op = int(input('\n1 - Empilhar\n2 – Desempilhar\n3 - Imprime apilha\n4 - Ultima entrada\n5 - Media de idade\n6 - '
                   'Sair:\n '))
    if op is 1:
        p.push()
    elif op is 2:
        p.pop()
    elif op is 3:
        p.printall()
    elif op is 4:
        p.last()
    elif op is 5:
        p.med()
    else:
        break
