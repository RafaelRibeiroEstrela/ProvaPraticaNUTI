

from tkcalendar import * 
from tkinter import *
from conexao_db import conection_db



class tela_4:

    def __init__(self):

        
        # Construção da tela
        self.principal = Tk ()
        self.principal.geometry ('1024x768')
        self.principal.resizable (False, False)
        self.principal.title ('Companhia Voo')

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

        self.ct6 = Frame (pady=10)
        self.ct6.pack ()         
                
        self.label1 = Label(self.ct1, pady=20, padx=50, relief='groove', bg='gray72')
        self.label1['text'] = 'Agendar Voo'
        self.label1['font'] = ('Arial', 12)
        self.label1.pack()

        self.calendar = Calendar(self.ct2)
        self.calendar.pack(side = LEFT)

        self.date = self.calendar.get_date()

        self.espaco1 = Label(self.ct2)
        self.espaco1['text'] = '  '
        self.espaco1.pack(side = LEFT)

        self.pegar_data = Button(self.ct2)
        self.pegar_data['text'] = 'ADD'
        self.pegar_data['command'] = self.select_date
        self.pegar_data.pack(side = LEFT)

        self.label1_listbox = Label(self.ct3)
        self.label1_listbox['text'] = 'Avião'
        self.label1_listbox.grid(row=0, column=0)

        self.lista1 = Listbox(self.ct3, width=15, height=5)
        self.lista1.grid(row=1, column=0)

        self.botao1 = Button(self.ct3)
        self.botao1['text'] = 'ADD'
        self.botao1['command'] = lambda: self.select(1)
        self.botao1.grid(row=2, column=0)   

        self.label2_listbox = Label(self.ct3)
        self.label2_listbox['text'] = 'Cidade Origem'
        self.label2_listbox.grid(row=0, column=1)

        self.lista2 = Listbox(self.ct3, width=20, height=5)
        self.lista2.grid(row=1, column=1)

        self.botao2 = Button(self.ct3)
        self.botao2['text'] = 'ADD'
        self.botao2['command'] = lambda: self.select(2)
        self.botao2.grid(row=2, column=1)

        self.label3_listbox = Label(self.ct3)
        self.label3_listbox['text'] = 'Cidade Destino'
        self.label3_listbox.grid(row=0, column=2)

        self.lista3 = Listbox(self.ct3, width=20, height=5)
        self.lista3.grid(row=1, column=2)

        self.botao3 = Button(self.ct3)
        self.botao3['text'] = 'ADD'
        self.botao3['command'] = lambda: self.select(3)
        self.botao3.grid(row=2, column=2)

        self.label4_listbox = Label(self.ct3)
        self.label4_listbox['text'] = 'Horário'
        self.label4_listbox.grid(row=0, column=3)

        self.lista4 = Listbox(self.ct3, width=20, height=5)
        self.lista4.grid(row=1, column=3)

        self.botao4 = Button(self.ct3)
        self.botao4['text'] = 'ADD'
        self.botao4['command'] = lambda: self.select(4)
        self.botao4.grid(row=2, column=3)

        self.label5_listbox = Label(self.ct3)
        self.label5_listbox['text'] = 'Duração'
        self.label5_listbox.grid(row=0, column=4)

        self.lista5 = Listbox(self.ct3, width=10, height=5)
        self.lista5.grid(row=1, column=4)

        self.botao5 = Button(self.ct3)
        self.botao5['text'] = 'ADD'
        self.botao5['command'] = lambda: self.select(5)
        self.botao5.grid(row=2, column=4)

        #Estabelecendo conexao com o SQLite
        self.conn = conection_db().return_conn()
        self.cursor = self.conn.cursor()

        lista = []

        self.cursor.execute ("""SELECT nome FROM aviao;""")
        lista.append(self.cursor.fetchall())

        self.cursor.execute ("""SELECT nome FROM cidade;""")
        lista.append(self.cursor.fetchall())


        #Adicionando elementos nos objetos da tela
        for i in range(len(lista)):

            for j in range(len(lista[i])):

                for k in range(len(lista[i][j])):

                    if (i == 0):

                        self.lista1.insert(END, lista[i][j][k])

                    if (i == 1):

                        self.lista2.insert(END, lista[i][j][k])
                        self.lista3.insert(END, lista[i][j][k])

        for i in range(24):

            if (i < 10):

                self.lista4.insert(END, '0'+str(i)+'h')

            else:

                self.lista4.insert(END, str(i)+'h')

            if (i > 0):

                self.lista5.insert(END, str(i) + 'h')

        self.lista5.insert(END, '24h')

        self.label15 = Label(self.ct4)
        self.label15['text'] = 'Data :'
        self.label15.grid(row=0, column=0)

        self.label15_resp = Label(self.ct4)
        self.label15_resp['text'] = ''
        self.label15_resp.grid(row=0, column=1)    

        self.label2 = Label(self.ct4)
        self.label2['text'] = 'Avião: '
        self.label2.grid(row=1, column=0)

        self.label2_resp = Label(self.ct4)
        self.label2_resp['text'] = ''
        self.label2_resp.grid(row=1, column=1)

        self.label3 = Label (self.ct4)
        self.label3['text'] = 'Cidade Origem: '
        self.label3.grid(row=2, column=0)

        self.label3_resp = Label(self.ct4)
        self.label3_resp['text'] = ''
        self.label3_resp.grid(row=2, column=1)

        self.label4 = Label (self.ct4)
        self.label4['text'] = 'Cidade Destino: '
        self.label4.grid(row=3, column=0)

        self.label4_resp = Label(self.ct4)
        self.label4_resp['text'] = ''
        self.label4_resp.grid(row=3, column=1)

        self.label5 = Label (self.ct4)
        self.label5['text'] = 'Horário: '
        self.label5.grid(row=4, column=0)

        self.label5_resp = Label(self.ct4)
        self.label5_resp['text'] = ''
        self.label5_resp.grid(row=4, column=1)

        self.label6 = Label (self.ct4)
        self.label6['text'] = 'Duração: '
        self.label6.grid(row=5, column=0)

        self.label6_resp = Label(self.ct4)
        self.label6_resp['text'] = ''
        self.label6_resp.grid(row=5, column=1)

        self.botao_confirmar = Button(self.ct5)
        self.botao_confirmar['text'] = 'Confirmar'
        self.botao_confirmar['command'] = self.confirmar
        self.botao_confirmar.pack()

        self.status = Label(self.ct6)
        self.status['text'] = 'Status: '
        self.status.pack(side = LEFT)

        self.mensagem = Label(self.ct6)
        self.mensagem.pack(side = LEFT)

        self.voltar = Button(self.principal, width=10, height=2)
        self.voltar['text'] = 'Voltar'
        self.voltar['command'] = self.chamar_tela2
        self.voltar.place(x=100,y=600)

        self.informativo = Label(self.principal)
        self.informativo['text'] = """Tutorial: Você deve selecionar uma data e clicar no botão ADD. 
        Deve-se fazer o mesmo com as outras informações
        e após concluir, clicar no botão CONFIRMAR"""
        self.informativo.place(x=650,y=100)

        self.bug = Label(self.principal)
        self.bug['text'] = """Existe um erro ao agendar um voo\n em um intervalo de datas, ou seja, entre dois voos já agendados.\n Não foi corrigido a tempo"""
        self.bug.place(x=0,y=0)

        self.principal.mainloop()


    def chamar_tela2(self):
    
        self.principal.destroy()
        self.conn.close()    
        import tela2
        tela2.tela_2()



    def confirmar(self):

        #Verifica se todos os campos foram preenchidos
        if (self.label15_resp['text'] == '' or self.label2_resp['text'] == '' or self.label3_resp['text'] == '' 
            or self.label4_resp['text'] == '' or self.label5_resp['text'] == '' or self.label6_resp['text'] == ''):

            self.mensagem['text'] = 'Erro > Todos os campos devem ser preenchidos'

            return self.mensagem['text']

        #Verifica se a cidade de origem é diferente da cidade de destino
        if (self.label3_resp['text'] == self.label4_resp['text']):

            self.mensagem['text'] = 'Erro > A cidade de destino deve ser diferente da cidade de origem.'

            return self.mensagem['text']

        
#-----------------------------------------------------------------------------------------------------------------------


        self.cursor.execute("""SELECT * FROM voo""")
        lista0 = self.cursor.fetchall()

        #Verifica se o banco de dados está vazio
        if (lista0 == []):

            temp = ''

            for i in range(len(self.label5_resp['text'])):

                if (self.label5_resp['text'][i] != 'h'):

                    temp += self.label5_resp['text'][i]

            self.label5_resp['text'] = temp

            temp = ''

            for i in range(len(self.label6_resp['text'])):
        
                if (self.label6_resp['text'] != 'h'):

                    temp += self.label6_resp['text']

            self.cursor.execute("""INSERT INTO voo VALUES (
                               (SELECT MAX(id)+1 FROM voo),
                               (SELECT id FROM aviao WHERE nome = ?),
                               (SELECT id FROM cidade WHERE nome = ?),
                               (SELECT id FROM cidade WHERE nome = ?),
                               ?,
                               ?,
                               ?);""", (self.label2_resp['text'], self.label3_resp['text'], self.label4_resp['text'], self.label15_resp['text'], 
                                   self.label5_resp['text']+':00:00', self.label6_resp['text']+':00:00'))

            self.conn.commit()

            self.mensagem['text'] = 'Sucesso: O voo foi agendado'

            return self.mensagem['text']


#------------------------------------------------------------------------------------------------------------------------------------------------------

        self.cursor.execute("""SELECT a.nome, c.nome, v.data, v.horario, v.duracao, v.horario+v.duracao
                               FROM voo v
                               JOIN aviao a ON (v.id_aviao = a.id)
                               JOIN cidade c ON (v.id_cidade_destino = c.id)
                               WHERE a.nome = ?
                               ORDER BY v.data DESC""", (self.label2_resp['text'],))


        lista1 = self.cursor.fetchall()

        print (lista1)

        cont_tempo = ''
        cont_data = ''
        index = 0

        for i in range(len(lista1)):

            if (lista1[i][2] > cont_data):

                cont_data = lista1[i][2]

                if (lista1[i][3] > cont_tempo):

                    cont_tempo = lista1[i][3]
                    index = i


        if (lista1[index][1] != self.label3_resp['text']):

            self.mensagem['text'] = 'Erro > O avião não estará na cidade de origem selecionada'

            return self.mensagem['text']


        elif (lista1[0][2] > self.label15_resp['text']):

            self.mensagem['text'] = 'Erro > O avião não estará na data selecionada'


        elif (lista1[0][2] == self.label15_resp['text']):

            temp = ''

            for i in range(len(self.label5_resp['text'])):

                if (self.label5_resp['text'][i] != 'h'):

                    temp += self.label5_resp['text'][i]

            for i in range(len(lista1)):

                #Verificamos todos os horarios+duração de voos para saber se o avião estará antes do horario selecionado
                if (lista1[i][5] >= int(temp)):

                    self.mensagem['text'] = 'Erro > O avião estará na cidade após o horário selecionado'

                    return self.mensagem['text']



        self.cursor.execute("""SELECT 'True'
                               FROM voo v
                               JOIN aviao a ON (v.id_aviao = a.id)
                               JOIN cidade c ON (v.id_cidade_origem = c.id)
                               WHERE v.data = ? AND a.nome = ? AND c.nome = ?""", (self.label15_resp['text'], self.label2_resp['text'], self.label3_resp['text']))

        lista2 = self.cursor.fetchall()

        if (lista2 != []):

            self.mensagem['text'] = 'Erro > Já existe um voo agendado da cidade de origem selecionada'

            return self.mensagem['text']


        temp1 = ''
        temp2 = ''                
        for i in range(len(self.label5_resp['text'])):

            if (self.label5_resp['text'][i] != 'h'):

                temp1 += self.label5_resp['text'][i]

        for i in range(len(self.label6_resp['text'])):

            if (self.label6_resp['text'][i] != 'h'):

                temp2 += self.label6_resp['text'][i]

        if (int(temp2) < 10):

            temp2 = '0'+temp2
                   

        #Caso não tenha feito nenhum return das funções, todas as condições foram satisfeitas para se fazer o agendamento do voo
        self.cursor.execute("""INSERT INTO voo VALUES (
                          (SELECT MAX(id)+1 FROM voo),
                          (SELECT id FROM aviao WHERE nome = ?),
                          (SELECT id FROM cidade WHERE nome = ?),
                          (SELECT id FROM cidade WHERE nome = ?),
                          ?,
                          ?,
                          ?);""", (self.label2_resp['text'], self.label3_resp['text'], self.label4_resp['text'], self.label15_resp['text'], 
                                   temp1+':00:00', temp2+':00:00'))

        self.conn.commit()

        self.label15_resp['text'] = ''
        self.label2_resp['text'] = ''
        self.label3_resp['text'] = ''
        self.label4_resp['text'] = ''
        self.label5_resp['text'] = ''
        self.label6_resp['text'] = '' 

        self.mensagem['text'] = 'Sucesso: O voo foi agendado'

        return self.mensagem['text']                     


    def select_date(self):
        
        #Tratando a data: A data fornecida pelo TKinter é bem esquisito. É feito um tratamento da data para o padrão do banco
        x = self.calendar.get_date()

        dia = mes = ano = ''
        i = 0
        while (True):

            if (x[i] == '/'):

                i += 1

                break

            else:
            
                mes += x[i]

            i += 1

        while (True):

            if (x[i] == '/'):

                break

            else:
            
                dia += x[i]

            i += 1

        if (len(dia) == 1):

            dia = '0'+dia

        if (len(mes) == 1):

            mes = '0'+mes


        ano = '20' + x[-2] + x[-1]

        self.label15_resp['text'] = ano+'-'+mes+'-'+dia

    def select(self, x):

        #Função que pega o item selecionado nas listas e joga no Label de informações
        if (x == 1):

            self.label2_resp['text'] = self.lista1.get(ANCHOR)
        
        if (x == 2):

            self.label3_resp['text'] = self.lista2.get(ANCHOR)

        if (x == 3):
        
            self.label4_resp['text'] = self.lista3.get(ANCHOR)

        if (x == 4):

            self.label5_resp['text'] = self.lista4.get(ANCHOR)

        if (x == 5):
        
            self.label6_resp['text'] = self.lista5.get(ANCHOR)        



#tela_4()