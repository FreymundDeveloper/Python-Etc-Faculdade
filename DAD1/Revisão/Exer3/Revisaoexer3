from Revisão.Exer3.Revisaoexer3 import Menu

a = Menu()
x = 0
chave = False

while x is not 6:
    x = int(input('1)Leia o valor de n e os n valores de uma lista A com valores numéricos;\n'
                  '2)Imprime os valores ordenados de forma crescente;\n'
                  '3) Determine e imprima para cada número que se repete no conjunto aquantidade de vezes que ele '
                  'aparece repetido;\n '
                  '4)Elimine os elementos repetidos formando uma nova lista B,imprimindo este novo conjunto\n'
                  '5)Determine e imprima a média dos valores da lista A,\n'
                  '6)Sair:'))

    if x is 1:
        valor = int(input('Digite a quantidade de valores:'))
        z = 0
        v = []
        chave = True
        while z < valor:
            v.append(int(input('Digite um valor: ')))
            a.receb(v)

            z += 1

    if x is 2 and chave is True:
        a.ord()

    if x is 3 and chave is True:
        a.rep()

    if x is 4 and chave is True:
        a.elim()

    if x is 5 and chave is True:
        a.med()

    elif chave is False:
        print('OPÇ 1 NECESSARIA')
