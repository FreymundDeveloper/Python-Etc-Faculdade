sm = float(input('Digite o valor do seu saldo:'))


def resp():
    print('Vc tem um saldo de R$ %.2f com direito a um credito de R$ %.2f' % (sm, rsp))


if 0 > sm <= 500:
    rsp=0
elif 500 > sm <= 1000:
    rsp=sm-(sm*0.3)
elif 1000 > sm <= 3000:
    rsp=sm-(sm*0.4)
elif sm>3000:
    rsp=sm-(sm*0.5)

resp()
