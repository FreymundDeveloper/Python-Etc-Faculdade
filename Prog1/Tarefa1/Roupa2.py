from Tarefa1.Roupa import Roupa

v = []
x = 0
z = 0
c = False

while x is not 5:
    x = int(input('1)Objetos roupas:\n'
                  '2)Leitura de dados:\n'
                  '3)Calcular\n'
                  '4)Imprimir dados:\n'
                  '5)Sair: '))

    if x is 1:
        z = int(input('Quantas peças serão registradas: '))
        y = 0
        while y < z:
            peca = Roupa()
            v.append(peca)
            y += 1
        c = True

    elif x is 2 and c is True:
        y = 0
        while y < z:
            v[y].ler_dados()
            y += 1

    elif x is 3 and c is True:
        for e in v:
            print(e.calular())

    elif x is 4 and c is True:
        for e in v:
            e.dados()

    else:
        print('OPÇ INVALIDA')
