def mult(a, b):
    if b == 1:
        return a * b

    elif b > 1:
        return a + mult(a, b - 1)


valorA = int(input('Digite um valor: '))
valorB = int(input('Digite um valor: '))
print('%i X %i = %i' % (valorA, valorB, mult(valorA, valorB)))
