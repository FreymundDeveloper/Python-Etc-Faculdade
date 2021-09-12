class TV:
    ndc=None
    v=None
    vm=None
    vmi=None

    def __init__(self, ndc, v, vm, vmi):
        self.ndc = ndc
        self.v = v
        self.vm = vm
        self.vmi = vmi

    def ifc(self, ndc):
        self.ndc = ndc

    def mvs(self):
        if self.v+1 <= self.vm:
            self.v += 1

    def mvb(self):
        if self.v-1 >= self.vmi:
            self.v -= 1


tv=TV(None, None, 60, 0)
tv.ndc = int(input('Informe o canal atual:'))
tv.v = int(input('Informe o volume atual:'))
c=0
while c != 3:
    c=int(input('1)Aumentar Vol:\n2)Abaixar Vol:\n3)Desligar TV:'))
    if c is 1:
        tv.mvs()
        print('Canal: %i \n Vol: %i' % (tv.ndc, tv.v))

    if c is 2:
        tv.mvb()
        print('Canal: %i \n Vol: %i' % (tv.ndc, tv.v))
