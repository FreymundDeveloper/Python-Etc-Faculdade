num1=float(input('Digite o valor do seu salario:'))
num2=float(input('Digite o valor da prestação:'))

ver=num1/100*30

if ver<num2:
    print('Linha de credito aprovado')
else:
    print('linha de credito negado')
