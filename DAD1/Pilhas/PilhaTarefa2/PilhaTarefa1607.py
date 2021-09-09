class Pilha:
    _pilha1 = None
    _pilha2 = None

    def __init__(self):
        self._pilha1 = []
        self._pilha2 = []

    def push(self, dado1, dado2):
        self._pilha1.append(dado1)
        self._pilha2.append(dado2)

    def ddaut(self):
        aunum = [18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]
        aucod = ['FREE3', 'FREE2', 'FREE7', 'PT03', 'FREE4', 'QQR01', 'FREE8', 'FREE1', 'PT01', 'FREE6', 'FREE5',
                 'PT04', 'PT02']

        x = len(aunum) - 1

        while x >= 0:
            self.push(aunum[x], aucod[x])
            x -= 1

    def ddmn(self):
        quant = int(input('Numero de dados que serão inceridos: '))

        while quant > 0:
            mnnum = int(input('\nInforme a linha: '))
            mncod = input('informe o codigo: ')
            self.push(mnnum, mncod)
            quant -= 1

    def imp(self):
        i = 1
        while i <= len(self._pilha1):
            print('Codigo: ', self._pilha2[-i], ' Linha: ', self._pilha1[-i])
            i += 1

        i -= 1

        while i >= 0:
            if self._pilha1 and self._pilha2:
                del self._pilha1[len(self._pilha1) - 1]
                del self._pilha2[len(self._pilha2) - 1]
            else:
                print('\nA PILHA ESTA VAZIA... TALVEZ VC A TENHA LIMPADO RECENTEMENTE')
                break
            i -= 1


#################################################################################################################
p = Pilha()

while True:
    op = int(input('1)Cadastra automaticamente \n2)Cadastrar manualmente \n3)Imprimir(E LIMPAR) \n4)Sair\n'))

    if op is 1:
        p.ddaut()

    elif op is 2:
        p.ddmn()

    elif op is 3:
        p.imp()

    elif op is 4:
        break

    elif op < 0 or op > 4:
        print('Opção inválida')
