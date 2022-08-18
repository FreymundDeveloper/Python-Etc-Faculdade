def soma(n):
    if n == 0:
        return n
    else:
        return n + soma(n - 1)


n = int(input('Digite um valor para a soma sucessiva: '))
print('Resultado: ', soma(n))
