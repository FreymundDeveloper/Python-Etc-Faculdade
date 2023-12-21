vi=float(input('Digite o valor inicial da divida:'))
jm=float(input('Digite o valor dos juros mensais:'))
mpd=float(input('Quantos meses faltam para pagar a divida:'))

x=1
rsp=0

while x <= mpd:
    vi=vi/100*jm+vi
    rsp=rsp+vi
    x=x+1

print('O valor final a pagar é R$', rsp)
