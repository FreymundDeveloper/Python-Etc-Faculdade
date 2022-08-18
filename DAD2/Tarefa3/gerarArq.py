import random

tamanhoVetor = 100  # Alterar e gerar todos os vetores
primoRepeticao = 13  # utilizar 3 (três) quando gerar o vetor com 10 posições

# Ordenado
with open('ordenado' + str(tamanhoVetor) + '.txt', 'w') as f:
    for i in range(tamanhoVetor):
        f.write(str(i) + '\n')
f.close()  # lembrem de SEMPRE fechar o arquivo!

# Ordenado inverso
with open('reverso' + str(tamanhoVetor) + '.txt', 'w') as f:
    for i in reversed(range(tamanhoVetor)):
        f.write(str(i) + '\n')
f.close()

# Aleatorio
with open('aleatorio' + str(tamanhoVetor) + '.txt', 'w') as f:
    for i in range(tamanhoVetor):
        f.write(str(random.randint(0, (tamanhoVetor * 2))) + '\n')
f.close()

# Aleatorio com muitos valores repetidos
with open('repetido' + str(tamanhoVetor) + '.txt', 'w') as f:
    for i in range(tamanhoVetor):
        f.write(str(random.randint(0, (tamanhoVetor / 5))) + '\n')
f.close()

# Semi Ordenado
with open('semiOrdenado' + str(tamanhoVetor) + '.txt', 'w') as f:
    for i in range(tamanhoVetor):
        if (i % primoRepeticao == 0):
            f.write(str(i * 3) + '\n')
        else:
            f.write(str(i) + '\n')
f.close()

# impressão
l = []
with open('ordenado' + str(tamanhoVetor) + '.txt', 'r') as f:
    for i in f.readlines():
        l.append(int(i))

f.close()
print('ordenado crescente')
print(l)

l = []
with open('reverso' + str(tamanhoVetor) + '.txt', 'r') as f:
    for i in f.readlines():
        l.append(int(i))

f.close()
print('ordenado descrescente')
print(l)

l = []
with open('aleatorio' + str(tamanhoVetor) + '.txt', 'r') as f:
    for i in f.readlines():
        l.append(int(i))

f.close()
print('Aleatório')
print(l)

l = []
with open('repetido' + str(tamanhoVetor) + '.txt', 'r') as f:
    for i in f.readlines():
        l.append(int(i))

f.close()
print('Aleatório com muitos valores repetidos')
print(l)

# semiOrdenado

l = []
with open('semiOrdenado' + str(tamanhoVetor) + '.txt', 'r') as f:
    for i in f.readlines():
        l.append(int(i))

f.close()
print('Semi Ordenado')
print(l)

# Após entender o algoritmo, responda:

# Por que é importante ter nomes sugestivos nas variáveis?
# O nome utilizado tanto pro algoritmo quanto para variáveis te induziram ao erro na análise? Por que?
# Se fossem nomes mais sugestivos teria facilitado a compreensão?
