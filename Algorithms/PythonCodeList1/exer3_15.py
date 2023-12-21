cdt=float(input('Quanto custou essa apresentação: '))
cdi=float(input('Quanto custa um ingresso: '))

pc=cdt/cdi
lc=(cdt/100*23+cdt)/cdi

print('Para pagar os custos da apresentação é necessario vneder %.f ingressos e para obter um lucro de 23%% é'
      ' necessario vender %.f ingressos' % (pc, lc))
