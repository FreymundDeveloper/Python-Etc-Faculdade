km=float(input('Quantos KM vc vai percorrer:'))

if km>=200:
    rsp=km*0.45
    print('O valor do custo é igual a: ', rsp)
else:
    rsp=km*0.50
    print('O valor do custo é igual a:', rsp)
