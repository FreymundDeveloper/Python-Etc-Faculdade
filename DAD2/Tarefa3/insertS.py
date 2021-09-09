def in_sort(lista):  # Cria uma função para realizar a ordenação em insertionSort
    comp = 0  # Variavel utilizada para armazenar o numero de comprarações
    comp_ad = 0  # Variavel auxiliar(comparações)
    mov_tr = 0  # Variavel utilizada para armazenar o numero movimentações e trocas
    # (No insertionSort, sempre que ocorre uma movimentação ocorre uma troca)

    for p in range(0, len(lista)):  # É utilizado um "for" para reconhecer o tamanho do vetor e gerar um indice
        valor = lista[p]  # A varialel "valor" armazena o valor atual da lista

        while p > 0 and lista[p - 1] > valor:  # Cria-se um loop que é percorrido enquanto "p(valor atual do indice)"
            # for maior do que 0 e "lista[p - 1](valor anterior do indice)" for maior do que "valor(valor armazenado)

            lista[p] = lista[p - 1]  # O valor da atual posição do indice é substituido pelo valor da posição anterior
            p -= 1  # Valor atual do indice é reduzido em 1
            mov_tr += 1
            comp_ad += 1

        lista[p] = valor  # O valor aramzenado na atual posição do indice é substituido pelo valor armazenado na
        # variavel "valor"
        comp += 1 + comp_ad
        comp_ad = 0

    print('lista ordenado:\n', lista)  # Retorna a lista ordenada
    print('Comparações: %i \nMovimentações e Trocas: %i ' % (comp, mov_tr))
    # Retorna as Comparações, Movimentações e Trocas


lista = [5, 8, 1, 0, 3, 1]  # cria-se um vetor para armazenar os valores da lista


in_sort(lista)  # A função in_sort é chamada
