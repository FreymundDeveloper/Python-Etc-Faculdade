import time
tamanhoVetor = 100  # Alterar e gerar todos os vetores
primoRepeticao = 13  # utilizar 3 (três) quando gerar o vetor com 10 posições
#  É necessario que os arquivos já tenham sidos gerados antes de executar o programa


def in_sort(lista):
    for p in range(0, len(lista)):
        valor = lista[p]

        while p > 0 and lista[p - 1] > valor:
            lista[p] = lista[p - 1]
            p -= 1

        lista[p] = valor

    print('lista ordenado:\n', lista)


l = []
with open('ordenado' + str(tamanhoVetor) + '.txt', 'r') as f:
    for i in f.readlines():
        l.append(int(i))

f.close()
print('ordenado crescente')
tempo_inicial = time.time()

in_sort(l)

print("%.10f segundos" % (time.time() - tempo_inicial))

# semiOrdenado

l = []
with open('semiOrdenado' + str(tamanhoVetor) + '.txt', 'r') as f:
    for i in f.readlines():
        l.append(int(i))

f.close()
print('Semi Ordenado')
tempo_inicial = time.time()

in_sort(l)

print("%.10f segundos" % (time.time() - tempo_inicial))

l = []
with open('aleatorio' + str(tamanhoVetor) + '.txt', 'r') as f:
    for i in f.readlines():
        l.append(int(i))

f.close()
print('Aleatório')
tempo_inicial = time.time()

in_sort(l)

print("%.10f segundos" % (time.time() - tempo_inicial))

l = []
with open('repetido' + str(tamanhoVetor) + '.txt', 'r') as f:
    for i in f.readlines():
        l.append(int(i))

f.close()
print('Aleatório com muitos valores repetidos')
tempo_inicial = time.time()

in_sort(l)

print("%.10f segundos" % (time.time() - tempo_inicial))

l = []
with open('reverso' + str(tamanhoVetor) + '.txt', 'r') as f:
    for i in f.readlines():
        l.append(int(i))

f.close()
print('ordenado descrescente')
tempo_inicial = time.time()

in_sort(l)

print("%.10f segundos" % (time.time() - tempo_inicial))
