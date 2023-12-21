cf=float(input('digite o valor dos custos de fabrica: '))

imp=cf/100*45
dist=(cf-imp)/100*28
rsp=cf+imp+dist

print('O valor total desse carro é de R$', rsp)
