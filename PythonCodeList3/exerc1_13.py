num = int(input('Digite um numero:'))

if num == 0 and 1 or num < 0:
    print('N é um numero primo')

elif num == 2:
    print('É um numero primo')

elif num % 2 == 0:
    print('Não é um numero primo')

else:

    n=2
    v=True

    while n < num:

        rsp=num % n

        if rsp == 0:
            v=False

        if n==2:
            n=n+1
        else:
            n=n+2

    if not v:
        print('Não é primo')
    else:
        print('Primo')
