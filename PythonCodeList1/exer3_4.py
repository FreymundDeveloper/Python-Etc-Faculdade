p=float(input('Digite o valor que é depositado mensalmete:'))
j=float(input('digite a taxa de juros mensais:'))
n=int(input('digite o numero de meses que a aplicaçao sera feita: '))

s=(1+j)*((1+j)**n-1)/j*p
vt=p*n+s

print('O valor total obtido é R$ %.2f , ou seja ouve um lucro de R$ %.2f' % (vt, s))
