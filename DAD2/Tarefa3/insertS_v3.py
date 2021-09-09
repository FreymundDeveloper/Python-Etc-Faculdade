def in_sort(lista):
    for p in range(0, len(lista)):
        valor = lista[p]

        while p > 0 and lista[p - 1] > valor:
            lista[p] = lista[p - 1]
            p -= 1

        lista[p] = valor

    print('lista ordenado:\n', lista)


lista = [5, 8, 1, 0, 3, 1]
in_sort(lista)
