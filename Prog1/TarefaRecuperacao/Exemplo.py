from tkinter import *

instancia = Tk()

instancia.title('Calculadora para Estatisticas')
instancia.geometry('800x600')
# instancia.wm_iconbitmap('icone.ico')

form = Entry(instancia)
form.pack()

calc = Button(instancia, text='Calcule')
calc.pack()

resultado = Label(instancia, text='Resultado', fg='blue')
resultado.pack()

instancia.mainloop()