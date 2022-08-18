from tkinter import *


class PackDemo(Frame):
    def __init__(self):
        # Inicializando o frame
        Frame.__init__(self)
        self.master.title("Gerenciador pack")
        self.master.geometry("600x250")
        self.pack(expand=YES, fill=BOTH)

        # Botao que adiciona outros, no topo
        self.botao1 = Button(self, text="Adicionar Botão",
                             command=self.adicionarBotao)
        self.botao1.pack(side=TOP)

        # Botão 2, no fundo e preenche X e Y
        self.botao2 = Button(self,
                             text="expand = NO, fill = BOTH")
        self.botao2.pack(side=BOTTOM, fill=BOTH)

        # Botão3: na esquerda, fill só na horizontal
        self.botao3 = Button(self, text="expand = YES, fill = X")
        self.botao3.pack(side=LEFT, expand=YES, fill=X)

        # Botão4: na direita, fill só na vertical
        self.botao4 = Button(self, text="expand = YES, fill = Y")
        self.botao4.pack(side=RIGHT, expand=YES, fill=Y)

        mainloop()

    def adicionarBotao(self):
        Button(self, text="Botão novo").pack(pady=5)


PackDemo()