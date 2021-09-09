from tkinter import *


class Janela(Tk):
    __Lb_Nome = None
    __Lb_Telefone = None
    __Lb_Email = None
    __Lb_Endereco = None
    __Et_Nome = None
    __Et_Telefone = None
    __Et_Email = None
    __Et_Endereco = None

    def __init__(self, Str="Janela", x1="0", y1="0", dx="640", dy="480", cor="lightgray"):
        super().__init__()
        super().title(Str)
        super().geometry("%sx%s+%s+%s" % (dx, dy, x1, y1))
        self.configure(bg=cor)
        self.inicialize()

    def inicialize(self):
        self.__Lb_Nome = Label(self, text='Nome:', bg='Yellow', width=9, anchor=E)
        self.__Lb_Nome.place(x=3, y=2)
        self.__Et_Nome = Entry(self, width=50)
        self.__Et_Nome.place(x=75, y=2)

        self.__Lb_Telefone = Label(self, text='Telefone:', bg='Yellow', width=9, anchor=E)
        self.__Lb_Telefone.place(x=3, y=27)
        self.__Et_Telefone = Entry(self, width=50)
        self.__Et_Telefone.place(x=75, y=27)

        self.__Lb_Email = Label(self, text='Email:', bg='Yellow', width=9, anchor=E)
        self.__Lb_Email.place(x=3, y=52)
        self.__Et_Email = Entry(self, width=50)
        self.__Et_Email.place(x=75, y=52)

        self.__Lb_Endereco = Label(self, text='Endereco:', bg='Yellow', width=9, anchor=E)
        self.__Lb_Endereco.place(x=3, y=77)
        self.__Et_Endereco = Entry(self, width=50)
        self.__Et_Endereco.place(x=75, y=77)


Jan1 = Janela("Minha janela Tkinter", "400", "200", "390", "100", "orange")

Jan1.mainloop()
