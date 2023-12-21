qh=int(input('Quantos quartos tem esse hotel: '))
vq=float(input('Qual o valor de um quarto para o fim de semana: '))

vp=vq-(vq/100*25)
vt1=vp*qh
vt7=vp*(qh/100*70)
perd=(vq*qh)-vt1

print('Valor promocional da diária é de R$', vp)
print('Valor total a ser arrecadado caso a ocupação neste final de semana atinja 100% é de R$', vt1)
print('Valor total a ser arrecadado caso a ocupação neste final de semana atinja 70% é de R$', vt7)
print('Valor que o hotel deixará de arrecadar em virtude da promoção, caso a ocupação atinja 100% é de R$', perd)
