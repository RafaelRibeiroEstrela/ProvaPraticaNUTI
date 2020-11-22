

from tkinter import *
from conexao_db import conection_db

class tela_3:
    
    def __init__(self):
        

    	
    	#Construção da tela
    	self.principal = Tk ()
    	self.principal.title ('Companhia Voo')
    	self.principal.geometry ('1024x768')
    	self.principal.resizable (False, False)

    	self.ct1 = Frame (pady=30)
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
    	self.label1['text'] = 'Voos Agendados'
    	self.label1['font'] = ('Arial', 12)
    	self.label1.pack()

    	self.label1_listbox = Label(self.ct2)
    	self.label1_listbox['text'] = 'ID'
    	self.label1_listbox.grid(row=0, column=0)

    	self.label2_listbox = Label(self.ct2)
    	self.label2_listbox['text'] = 'Avião'
    	self.label2_listbox.grid(row=0, column=1)

    	self.label3_listbox = Label(self.ct2)
    	self.label3_listbox['text'] = 'Cidade Origem'
    	self.label3_listbox.grid(row=0, column=2)

    	self.label4_listbox = Label(self.ct2)
    	self.label4_listbox['text'] = 'Cidade Destino'
    	self.label4_listbox.grid(row=0, column=3)

    	self.label5_listbox = Label(self.ct2)
    	self.label5_listbox['text'] = 'Data'
    	self.label5_listbox.grid(row=0, column=4)

    	self.label6_listbox = Label(self.ct2)
    	self.label6_listbox['text'] = 'Horário'
    	self.label6_listbox.grid(row=0, column=5)

    	self.label7_listbox = Label(self.ct2)
    	self.label7_listbox['text'] = 'Duração'
    	self.label7_listbox.grid(row=0, column=6)

    	self.lista1 = Listbox(self.ct2, width=3, height=15)
    	self.lista1.grid(row=1, column=0)

    	self.lista2 = Listbox(self.ct2, width=15, height=15)
    	self.lista2.grid(row=1, column=1)

    	self.lista3 = Listbox(self.ct2, width=20, height=15)
    	self.lista3.grid(row=1, column=2)

    	self.lista4 = Listbox(self.ct2, width=20, height=15)
    	self.lista4.grid(row=1, column=3)

    	self.lista5 = Listbox(self.ct2, width=15, height=15)
    	self.lista5.grid(row=1, column=4)

    	self.lista6 = Listbox(self.ct2, width=15, height=15)
    	self.lista6.grid(row=1, column=5)

    	self.lista7 = Listbox(self.ct2, width=15, height=15)
    	self.lista7.grid(row=1, column=6)

    	self.bug = Label(self.principal)
    	self.bug['text'] = 'Existe um erro no sistema caso o banco de dados esteja vazio. Não foi corrigido a tempo'
    	self.bug.place(x=0,y=0)

    	#Estabelece conexão com o SQLite
    	self.conn = conection_db().return_conn()
    	self.cursor = self.conn.cursor()


    	#É feito um SELECT para mostrar todos os voos já agendados
    	
    	try:	

    		self.cursor.execute ("""SELECT v.id, a.nome, c1.nome, c2.nome, v.data, v.horario, v.duracao
						   		    FROM voo v
						   		    JOIN aviao a ON (v.id_aviao = a.id)
						   		    JOIN cidade c1 ON (v.id_cidade_origem = c1.id)
						   		    JOIN cidade c2 ON (v.id_cidade_destino = c2.id);""")

    		lista = self.cursor.fetchall()

    		for i in range(len(lista)):

	    		for j in range(len(lista[i])):

	    			if (j == 0):

	    				self.lista1.insert(END, lista[i][j])

	    			if (j == 1):

	    				self.lista2.insert(END, lista[i][j])

	    			if (j == 2):

	    				self.lista3.insert(END, lista[i][j])

	    			if (j == 3):

	    				self.lista4.insert(END, lista[i][j])

	    			if (j == 4):

	    				self.lista5.insert(END, lista[i][j])

	    			if (j == 5):
	    			
	    				self.lista6.insert(END, lista[i][j])

	    			if (j == 6):

	    				self.lista7.insert(END, lista[i][j])

	    	self.espaco1 = Label(self.ct3, height=2)
	    	self.espaco1['text'] = ''
	    	self.espaco1.pack(side = TOP)

	    	self.voltar = Button(self.ct5, width=10, height=1)
	    	self.voltar['text'] = 'Voltar'
	    	self.voltar['font'] = ('Arial', 12)
	    	self.voltar['command'] = self.chamar_tela2
	    	self.voltar.pack()    	


	    	self.principal.mainloop ()

    	except:    	

	    	self.espaco1 = Label(self.ct3, height=2)
	    	self.espaco1['text'] = ''
	    	self.espaco1.pack(side = TOP)

	    	self.voltar = Button(self.ct5, width=10, height=1)
	    	self.voltar['text'] = 'Voltar'
	    	self.voltar['font'] = ('Arial', 12)
	    	self.voltar['command'] = self.chamar_tela2
	    	self.voltar.pack()    	


	    	self.principal.mainloop ()
	    	

    def chamar_tela2(self):

    	self.principal.destroy()
    	self.conn.close()
    	import tela2
    	tela2.tela_2()

#tela_3()