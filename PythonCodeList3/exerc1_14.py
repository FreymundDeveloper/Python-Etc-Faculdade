n = int(input('Digite um numero:'))

if n <= 2:
    print('Não possui antecessors primos')

else:

    print(2)
    c=2

    while c<n:

        c2=2

        while c2 <= c:

            if c % c2 == 0 and c2 != 2:
                break

            elif c2 == 2:
                c2 = c2 + 1
            else:
                c2 = c2 + 2

        if c2 == c:
            print(c)

        c=c+1
