

from tkinter import *
from PIL import ImageTk, Image



class tela_1:
    
    def __init__(self):
        
    	#Construção da tela
        self.principal = Tk ()
        self.principal.title ('Companhia Voo')
        self.principal.geometry ('1024x768')
        #self.principal.iconbitmap('bitmap.jpg')
        self.principal.resizable (False, False)

        self.ct1 = Frame (pady=30) 
        self.ct1.pack ()

        self.ct2 = Frame (pady=10)
        self.ct2.pack ()

        self.ct3 = Frame (pady=30)
        self.ct3.pack ()

        self.ct4 = Frame (pady=10)
        self.ct4.pack ()

        self.label1 = Label(self.ct1, pady=20, padx=20, relief='groove', bg='gray72')
        self.label1['text'] = 'Companhia Aérea Teste'
        self.label1['font'] = 12
        self.label1.pack()

        self.img = ImageTk.PhotoImage (Image.open('download.jpg'))
        self.login_img = Label(self.ct2, relief='groove', image=self.img)
        self.login_img.pack ()

        self.email = Label (self.ct3, pady=10)
        self.email ["text"] = "User"
        self.email.grid (row=0, column=0)

        self.entrada_email = Entry (self.ct3)
        self.entrada_email ["width"] = 30
        self.entrada_email ["font"] = ("", "12")
        self.entrada_email.insert(0, 'Clique em autenticar')
        self.entrada_email.grid (row=0, column=1)

        self.senha = Label (self.ct3, pady=10)
        self.senha['text'] = 'Password'
        self.senha.grid (row=1, column=0)
        
        self.entrada_senha = Entry (self.ct3)
        self.entrada_senha ["show"] = '*'
        self.entrada_senha ["width"] = 30
        self.entrada_senha ["font"] = ("", "12")
        self.entrada_senha.insert(0, 'admin')
        self.entrada_senha.grid (row=1, column=1)

        self.autenticar = Button (self.ct4)
        self.autenticar ["text"] = "autenticar"
        self.autenticar ["font"] = ("Calibri", "9")
        self.autenticar ["width"] = 20
        self.autenticar ["command"] = self.chamar_pag
        self.autenticar.pack (side = LEFT)


        self.principal.mainloop ()

    def chamar_pag(self):


    	self.principal.destroy()
    	import tela2
    	tela2.tela_2()
    	
tela_1()
