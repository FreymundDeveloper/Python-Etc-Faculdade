class No_pilha:
    _letra = None
    _proximo = None

    def __init__(self):
        self._letra = ''
        self._proximo = None

    def getLetra(self):
        return self._letra

    def setLetra(self, ltr):
        self._letra = ltr

    def getProximo(self):
        return self._proximo

    def setProximo(self, prox):
        self._proximo = prox


class Pilha:
    def __init__(self):
        self._topo = None

    def push(self):
        temp_no = No_pilha()

        if temp_no:
            letra = input('Digite uma/s letra/s: ')
            temp_no.setLetra(letra)
            temp_no.setProximo(self._topo)  #
            self._topo = temp_no  #

    def vrfc(self):
        if not self._topo:
            print('Pilha vazia')
            return
        temp_no = self._topo
        palavra = ''

        while temp_no:
            palavra += str(temp_no.getLetra())
            temp_no = temp_no.getProximo()

        if palavra == (palavra[::-1]):
            print('A sequencia de letras que vc digitou forma uma palavra palindroma\nPalavra formada:', palavra)

        else:
            print('A sequencia de letras que vc digitou não forma uma palavra palindroma\nPalavra formada:', palavra)


#######################################################################################################################

p = Pilha()

while True:
    op = int(input('\n1)Entrar uma letra ou uma sequencia de letras na pilha\n2)Verificar se a pilha forma uma palavra '
                   'palindroma\n3)sair:'))

    if op is 1:
        p.push()
    elif op is 2:
        p.vrfc()
    else:
        break