def si(ti, v):
    return (v/100)*ti+v


ti = float(input('Digite a taxa de impostos(%) sobre o produto:'))
v=float(input('Digite o valor do produto:'))

print('O novo valor é de R$', si(ti,v))
