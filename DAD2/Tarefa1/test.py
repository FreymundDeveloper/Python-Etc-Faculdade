lista = ['10 ele aaa', '8 ww q', '9 qqqq ha']
ordenar = []

for dados in lista:
    if dados is not 'Registro vazio':
        verif = dados.split()
        ordenar.append(int(verif[0]))

    else:
        print('Registro vazio')

if ordenar:
    certo = sorted(ordenar)
    lista_ordenada = []

    for dados1 in certo:

        for dados2 in lista:
            comparar = dados2.split()

            if int(comparar[0]) is dados1:
                lista_ordenada.append(dados2)

    print(lista_ordenada)