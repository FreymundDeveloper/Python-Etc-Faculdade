def v(vp, de, c=0):
    if de > 0:
        vp = vp * 0.03 + vp

        while c < de:
            vp = vp * 0.001 + vp
            c += 1
    else:
        return vp

    return vp


c=1
tt=0
vp = 9
while vp != 0:
    vp = float(input('Digite o valor da prestação:'))
    c +=1
    if vp != 0:
        de = int(input('Digite os dia de atraso:'))

        print('Valor de %.2f devera se pago.' % v(vp, de, c=0))
        tt = tt + v(vp, de, c=0)
    else:
        print('Foram feitas %.f execusões e o valor total é de R$ %.2f' % (c,tt))
