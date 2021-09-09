def fatorial(n):
    if n > 0:
        return n * fatorial(n - 1)
    else:
        return 1


numero = int(input('Calcular o fatorial de: '))
print('O fatorial de', numero, 'é', fatorial(numero))