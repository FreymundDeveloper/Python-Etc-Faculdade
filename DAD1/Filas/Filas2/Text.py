base = 2

valor = (int(input('Digite um valor inteiro >1: ')))
while valor != 1:
    if valor % base == 0:
        new.setV(base)
        valor = valor / base

    else:
        base += 1