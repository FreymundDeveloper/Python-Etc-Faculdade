from tkinter import *


class Janela(Tk):
    __form = None
    __calc = None
    __resultado = None

    def __init__(self, Str='Calculadora para Estatisticas', x1="0", y1="0", dx="800", dy="600"):
        super().__init__()
        super().title(Str)
        super().geometry("%sx%s+%s+%s" % (dx, dy, x1, y1))
        self.inicialize()

    def inicialize(self):
        self.__form = Entry(self, width=20)

        self.__calc = Button(self, text='Calcule')

        self.__resultado = Label(self, text='Resultado', fg='blue')

        self.__form.grid(row=0, column=0, padx=350, pady=0)
        self.__calc.grid(row=1, column=0, padx=350, pady=0)
        self.__resultado.grid(row=2, column=0, padx=350, pady=0)


instancia = Janela()

instancia.mainloop()
