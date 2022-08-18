from tkinter import *


class Janela(Tk):  ## Questão 01
    __Lb_flamengo = None
    __Lb_vasco = None
    __Lb_torcida_total = None
    __Lb_pr = None
    __Lb_sc = None
    __Lb_rs = None
    __Et_flamengo_pr = None
    __Et_flamengo_sc = None
    __Et_flamengo_rs = None
    __Et_vasco_pr = None
    __Et_vasco_sc = None
    __Et_vasco_rs = None
    __Et_total_flamengo = None
    __Et_total_vasco = None
    __Bt_Calc = None

    def __init__(self, Str='Janela'):
        super().__init__()
        super().title(Str)
        self.configure(bg='orange')
        self.inicialize()

    def init_text(self):
        self.__Lb_pr = Label(self, text="Paraná", bg='Yellow', width=15)
        self.__Lb_sc = Label(self, text="Santa Catarina", bg='Yellow', width=15)
        self.__Lb_rs = Label(self, text="Rio Grande do Sul", bg='Yellow', width=15)

    def action_Total_Flamengo(self):
        n1 = float(self.__Et_flamengo_pr.get())
        n2 = float(self.__Et_flamengo_sc.get())
        n3 = float(self.__Et_flamengo_rs.get())
        total = n1 + n2 + n3
        self.__Et_total_flamengo.delete(0, END)
        self.__Et_total_flamengo.insert(END, '%.1f' % total)

    def action_Total_Vasco(self):
        n1 = float(self.__Et_vasco_pr.get())
        n2 = float(self.__Et_vasco_sc.get())
        n3 = float(self.__Et_vasco_rs.get())
        total = n1 + n2 + n3
        self.__Et_total_vasco.delete(0, END)
        self.__Et_total_vasco.insert(END, '%.1f' % total)

    def action_exit(self):
        sys.exit(0)

    def action_Bt_Calc(self):
        self.action_Total_Flamengo()
        self.action_Total_Vasco()

    def inicialize(self):
        self.__Lb_flamengo = Label(self, text="Flamengo", bg='Yellow', width=18)
        self.__Lb_vasco = Label(self, text="Vasco", bg='Yellow', width=18)

        self.init_text()

        self.__Et_flamengo_pr = Label(self, width=22)
        self.__Et_flamengo_sc = Label(self, width=22)
        self.__Et_flamengo_rs = Label(self, width=22)
        self.__Et_vasco_pr = Label(self, width=22)
        self.__Et_vasco_sc = Label(self, width=22)
        self.__Et_vasco_rs = Label(self, width=22)

        self.__Lb_torcida_total = Label(self, text="Torcida Total:", bg='Yellow', width=15)

        self.__Et_flamengo_pr = Entry(self, width=22)
        self.__Et_flamengo_sc = Entry(self, width=22)
        self.__Et_flamengo_rs = Entry(self, width=22)
        self.__Et_vasco_pr = Entry(self, width=22)
        self.__Et_vasco_sc = Entry(self, width=22)
        self.__Et_vasco_rs = Entry(self, width=22)

        self.__Bt_Calc = Button(self, text='Calcular', command=self.action_Bt_Calc)

        self.__Et_total_vasco = Entry(self, width=22, bg='grey')
        self.__Et_total_flamengo = Entry(self, width=22, bg='grey')

        self.__Lb_flamengo.grid(row=0, column=1, sticky=NW, padx=4, pady=4)
        self.__Lb_vasco.grid(row=0, column=2, sticky=NW, padx=4, pady=4)

        self.__Lb_pr.grid(row=1, column=0, sticky=NW, padx=4, pady=4)
        self.__Lb_sc.grid(row=2, column=0, sticky=NW, padx=4, pady=4)
        self.__Lb_rs.grid(row=3, column=0, sticky=NW, padx=4, pady=4)

        self.__Lb_torcida_total.grid(row=6, column=0, sticky=NW, padx=4, pady=4)

        self.__Et_flamengo_pr.grid(row=1, column=1, sticky=NW, padx=4, pady=4)
        self.__Et_flamengo_sc.grid(row=2, column=1, sticky=NW, padx=4, pady=4)
        self.__Et_flamengo_rs.grid(row=3, column=1, sticky=NW, padx=4, pady=4)
        self.__Et_vasco_pr.grid(row=1, column=2, sticky=NW, padx=4, pady=4)
        self.__Et_vasco_sc.grid(row=2, column=2, sticky=NW, padx=4, pady=4)
        self.__Et_vasco_rs.grid(row=3, column=2, sticky=NW, padx=4, pady=4)

        self.__Bt_Calc.grid(row=5, column=1, sticky=NW, padx=4, pady=4)

        self.__Et_total_flamengo.grid(row=6, column=1, sticky=NW, padx=4, pady=4)
        self.__Et_total_vasco.grid(row=6, column=2, sticky=NW, padx=4, pady=4)

        self.protocol("WM_DELETE_WINDOW", self.action_exit)
        self.init_text()


Jan1 = Janela("Torcidas de Futebol")
Jan1.mainloop()
