# No algoritmo InsertionSort a complexidade é definida por dois fatores. O principal deles é o tamanho do arquivo que
# o algoritmo vai organizar, tendo em vista que este tipo de algoritmo é extremamente ineficiente com arquivos com
# alto numero de valores. O segundo fator é a organização dos atuais valores do arquivo, sendo a lista ordenada o
# melhor caso, a semi ordenado o caso médio e a reversa o pior caso de complexidade. A formula que representa o
# calculo da complexidade do algoritmo é a O(n^2) ou n^2.

tamanhoVetor = 1000000
primoRepeticao = 13


# algoritmo
def in_sort(lista):  # É necessario já ter gerados os arquivos para o programa funcionar
    for p in range(0, len(lista)):  # O(n)
        valor = lista[p]  # Não considerada na contagem para comparar com o laço sem aninhar

        while p > 0 and lista[p - 1] > valor:  # O(n)
            lista[p] = lista[p - 1]  # O(1)
            p -= 1  # Não considerada na contagem para comparar com o laço sem aninhar

        lista[p] = valor  # Não considerada na contagem para comparar com o laço sem aninhar

    return lista


# O(n) * (O(n) * O(1))
# O(n^2)


# Exemplos: 1, 5, 9, 30, 500000
# (1) = O(1^2) = 1
# (5) = O(5^2) = 25
# (9) = O(9^2) = 81
# (30) = O(30^2) = 900
# (500000) = O(500000^2) = 250000000000

# Entrada
l = []
tipo = 'reverso'
with open(tipo + str(tamanhoVetor) + '.txt', 'r') as f:
    for i in f.readlines():
        l.append(int(i))

f.close()
# impressão
print(tipo, '\nLista Ordenada:\n', in_sort(l))
