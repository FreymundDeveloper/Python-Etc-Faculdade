from tkinter import *


class Janela(Tk):
    __Lb_vista = None
    __Lb_prazo = None
    __Lb_difer = None
    __Lb_fogao = None
    __Lb_gela = None
    __Lb_teve = None
    __Et_vista_fogao = None
    __Et_vista_gela = None
    __Et_vista_teve = None
    __Et_prazo_fogao = None
    __Et_prazo_gela = None
    __Et_prazo_teve = None
    __Et_difer_fogao = None
    __Et_difer_gela = None
    __Et_difer_teve = None
    __Bt_Calc = None

    def __init__(self, Str='Janela'):
        super().__init__()
        super().title(Str)
        self.geometry('%sx%s+%s+%s' % ('580', '200', '0', '0'))
        self.configure(bg='orange')
        self.inicialize()

    def init_text(self):
        self.__Lb_fogao.configure(text='Fogão')
        self.__Lb_gela.configure(text='Geladeira')
        self.__Lb_teve.configure(text='Televisor')

    def action_Diferenca_Fogao(self):
        n1 = float(self.__Et_vista_fogao.get())
        n2 = float(self.__Et_prazo_fogao.get())
        total = n2 - n1
        self.__Et_difer_fogao.delete(0, END)
        self.__Et_difer_fogao.insert(END, '%.1f' % total)

    def action_Diferenca_Gela(self):
        n1 = float(self.__Et_vista_gela.get())
        n2 = float(self.__Et_prazo_gela.get())
        total = n2 - n1
        self.__Et_difer_gela.delete(0, END)
        self.__Et_difer_gela.insert(END, '%.1f' % total)

    def action_Diferenca_Teve(self):
        n1 = float(self.__Et_vista_teve.get())
        n2 = float(self.__Et_prazo_teve.get())
        total = n2 - n1
        self.__Et_difer_teve.delete(0, END)
        self.__Et_difer_teve.insert(END, '%.1f' % total)

    def action_exit(self):
        self.destroy()
        sys.exit(0)

    def action_Bt_Calc(self):
        self.action_Diferenca_Fogao()
        self.action_Diferenca_Gela()
        self.action_Diferenca_Teve()

    def inicialize(self):
        self.__Lb_vista = Label(self, text="A Vista", bg='Yellow', width=18)
        self.__Lb_prazo = Label(self, text="A Prazo 12X", bg='Yellow', width=18)

        self.init_text()

        self.__Et_vista_gela = Entry(self, width=22)
        self.__Et_vista_gela = Entry(self, width=22)
        self.__Et_vista_teve = Entry(self, width=22)
        self.__Et_prazo_gela = Entry(self, width=22)
        self.__Et_prazo_gela = Entry(self, width=22)
        self.__Et_prazo_teve = Entry(self, width=22)
        self.__Et_difer_gela = Entry(self, width=22)
        self.__Et_difer_gela = Entry(self, width=22)
        self.__Et_difer_teve = Entry(self, width=22)

        self.__Lb_difer = Label(self, text="Diferença", bg='Yellow', width=15)

        self.__Et_vista_fogao.grid(row=1, column=1, sticky=NW, padx=4, pady=4)
        self.__Et_vista_gela.grid(row=2, column=1, sticky=NW, padx=4, pady=4)
        self.__Et_vista_teve.grid(row=3, column=1, sticky=NW, padx=4, pady=4)
        self.__Et_prazo_fogao.grid(row=1, column=2, sticky=NW, padx=4, pady=4)
        self.__Et_prazo_gela.grid(row=2, column=2, sticky=NW, padx=4, pady=4)
        self.__Et_prazo_teve.grid(row=3, column=2, sticky=NW, padx=4, pady=4)
        self.__Et_difer_fogao.grid(row=1, column=3, sticky=NW, padx=4, pady=4)
        self.__Et_difer_gela.grid(row=2, column=3, sticky=NW, padx=4, pady=4)
        self.__Et_difer_teve.grid(row=3, column=3, sticky=NW, padx=4, pady=4)


Jan1 = Janela('Compras Eletrodomésticos')
Jan1.mainloop()

# ESSA MERDA TA INCOMPLETA E QUE SE FODA
