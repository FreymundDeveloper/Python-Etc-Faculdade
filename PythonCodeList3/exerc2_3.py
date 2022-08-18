num=int(input('Digite quantos valores vc quer digitar:'))

maior=-9999999999999.9
menor=99999999999999.9
n=0
nn=0

while n<num:
    nn=float(input('Digite um numero:'))

    if nn > maior:
        maior=nn

    if nn < menor:
        menor=nn

    n=n+1

print('maior: %.f ;\n menor: %.f' % (maior, menor))
