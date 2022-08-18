class Tv:
    ligada = None
    canal = None
    cmin = None
    cmax = None

    def __init__(self, canal, ligada):
        self.canal = canal
        self.ligada = ligada
        self.cmin = 0
        self.cmax = 100


tv = Tv(1, True)
print(tv.canal)
print(tv.ligada)
