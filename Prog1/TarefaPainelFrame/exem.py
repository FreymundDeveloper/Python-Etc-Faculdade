from tkinter import *


class Janela(Tk):
    def __init__(self, Str="Janela", x1="0", y1="0", dx="640", dy="480", cor="lightgray"):
        super().__init__()
        super().title(Str)
        super().geometry("%sx%s+%s+%s" % (dx, dy, x1, y1))
        # super(Janela, self).configure(bg=cor) ## Python 2

        # Comandos alternativos
        # self.title(Str)
        # self.geometry("%sx%s+%s+%s" % (dx, dy, x1, y1))
        self.configure(bg=cor)

        self.inicialize()

    def inicialize(self):
        Lb1 = Label(self, text="First Name")
        Lb2 = Label(self, text="Last Name")
        Lb3 = Label(self, text="Text área")

        Et1 = Entry(self, width=52)
        Et2 = Entry(self, width=52)

        Txt1 = Text(self, height=8, width=40)

        Bt1 = Button(self, text='Botão 1')
        Bt2 = Button(self, text='Botão 2')

        Cnv = Canvas(self, bd=0, bg="yellow", width=182, height=62)
        Cnv.create_oval(2, 2, 180, 60, fill="cyan")

        Lb1.grid(row=0, column=0, padx=2, pady=2)
        Lb2.grid(row=1, column=0, padx=2, pady=2)
        Lb3.grid(row=2, column=0, padx=2, pady=2)
        Et1.grid(row=0, column=1, columnspan=2, padx=2, pady=2)
        Et2.grid(row=1, column=1, columnspan=2, padx=2, pady=2)
        Txt1.grid(row=2, column=1, columnspan=2, padx=2, pady=2)
        Bt1.grid(row=3, column=1, sticky=E, padx=2, pady=2)
        Bt2.grid(row=3, column=2, sticky=W, padx=2, pady=2)

        Cnv.grid(row=4, column=1, columnspan=2, padx=2, pady=2)


########################################################################################################################

Jan1 = Janela("Minha janela", "400", "200", "500", "380", "orange")

Jan1.mainloop()
