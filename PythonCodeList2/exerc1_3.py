num1=float(input('Digite um numero:'))
num2=float(input('Digite um numero:'))

num=num1+num2

if num>20:
    num=num+8
    print('Seu numero é:', num)
elif num<=20:
    num=num-5
    print('Seu numero é:', num)
