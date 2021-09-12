op=1
me=0
ma=0

while 0 < op < 140:
    op=float(input('Digite um valor:'))

    if 21 > op > 0:
        me=me+1
    elif 50 < op < 140:
        ma=ma+1

print('Quantidade menor que 21= %.f;\nQuantidade maior que 50= %.f .' % (me, ma))
