pc=float(input('Qual o preço de custo do produto: '))
ac=float(input('De quantos porcento sera o acrecimo ao custo: '))
vv=float(input('Qual o  valor de venda desse produto: '))

pt=(pc/100*ac)+pc

print('O preço de desse produto é de R$ %.2f e o seu valor de venda é de R$ %.2f' % (pt, vv))
