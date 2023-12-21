import math

raiz=float(input('Digite um numero: '))

if raiz<0:
    rsp=raiz*raiz
    print('Seu numero é:', rsp)
else:
    print("%4.2f" % math.sqrt(raiz))
