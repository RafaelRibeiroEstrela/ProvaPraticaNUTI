

from tkinter import *

class tela_2:
    
    def __init__(self):
        
    	#Construção da tela
        self.principal = Tk ()
        self.principal.title ('Companhia Voo')
        self.principal.geometry ('1024x768')
        self.principal.resizable (False, False)

        self.ct1 = Frame (pady=50) 
        self.ct1.pack ()

        self.ct2 = Frame (pady=10)
        self.ct2.pack ()

        self.ct3 = Frame (pady=10)
        self.ct3.pack ()

        self.ct4 = Frame (pady=10)
        self.ct4.pack ()

        self.ct5 = Frame (pady=10)
        self.ct5.pack ()


        self.label1 = Label(self.ct1, pady=20, padx=50, relief='groove', bg='gray72')
        self.label1['text'] = 'MENU'
        self.label1['font'] = ('Arial', 12)
        self.label1.pack()  

        self.botao1 = Button(self.ct2, width=50, height=3)
        self.botao1['text'] = 'Voos Agendados'
        self.botao1['font'] = ('Arial', 12)
        self.botao1['command'] = self.chamar_tela3
        self.botao1.pack()

        self.botao2 = Button(self.ct3, width=50, height=3)
        self.botao2['text'] = 'Agendar Novo Voo'
        self.botao2['font'] = ('Arial', 12)
        self.botao2['command'] = self.chamar_tela4
        self.botao2.pack()

        self.botao3 = Button(self.ct4, width=50, height=3)
        self.botao3['text'] = 'Editar Voo (Não Implementado)'
        self.botao3['font'] = ('Arial', 12)
        self.botao3.pack()

        self.espaco1 = Label(self.ct5, height=5)
        self.espaco1['text'] = ''
        self.espaco1.pack(side = TOP)

        self.botao4 = Button(self.ct5, width=10, height=1)
        self.botao4['text'] = 'Fechar'
        self.botao4['font'] = ('Arial', 12)
        self.botao4['command'] = self.close
        self.botao4.pack()

        self.principal.mainloop ()

    def chamar_tela3(self):

    	self.principal.destroy()
    	import tela3
    	tela3.tela_3()

    def chamar_tela4(self):

   		self.principal.destroy()
   		import tela4
   		tela4.tela_4()


    def close(self):

    	self.principal.destroy()
    	
    	

#tela_2()