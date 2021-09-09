from tkinter import *


class Place(Frame):
    def __init__(self):
        top = Tk()
        top.title("place")
        top.geometry("250x200")

        # Label e primeira entrada
        label1 = Label(top, text="Nota 1")
        label1.place(x=10, y=10)
        entrada1 = Entry(top, bd=5)
        entrada1.place(x=60, y=10)

        # Label e segunda entrada
        label2 = Label(top, text="Nota 2")
        label2.place(x=10, y=50)
        entrada2 = Entry(top, bd=5)
        entrada2.place(x=60, y=50)

        # Label e terceira entrada
        label3 = Label(top, text="Média")
        label3.place(x=10, y=150)
        entrada3 = Entry(top, bd=5)
        entrada3.place(x=60, y=150)

        # Botão
        botao = Button(top, text="Calcular")
        botao.place(x=100, y=100)

        top.mainloop()


Place()