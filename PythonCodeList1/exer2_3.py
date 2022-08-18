v=float(input('Digite o valor do produto: '))
t=int(input('Digite a quantidade de dias de atraso: '))
vt=float(input('Qual é o valor da taxa em relação ao valor do produto (digitar em porcentagem):'))

tx=v/100*vt
p=v+(v*(tx/100)*t)

print(' valor da prestação é:%.f' % p)
