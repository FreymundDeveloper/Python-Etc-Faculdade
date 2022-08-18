v=[15, 7, 27, 39]
x=0

p=int(input('Digite o valor que procura:'))

while x < len([v]):
    if v[x] is p:
        break
    x += 1

if v[x] is p:
    print('Achou')
else:
    print('N achou')
