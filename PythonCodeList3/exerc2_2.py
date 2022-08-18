c=0
num=0
p=0
n=0

while c < 10:
    num=float(input('Digite um numero:'))

    if num > 0:
        p=p+num
    else:
        n=n+1

    c += 1

print('Soma dos positivos: %.f ;\n N de negativo: %.f .' % (p, n))
