


import sqlite3

conn = sqlite3.connect ('companhia_aerea.db')

cursor = conn.cursor()

try:
       
    cursor.execute ("""CREATE TABLE cidade (
        id INTEGER NOT NULL,
        nome VARCHAR (50) NOT NULL,
        CONSTRAINT cidade_id_pk PRIMARY KEY(id));""")

    cursor.execute ("""CREATE TABLE aviao (
        id INTEGER NOT NULL,
        nome VARCHAR (50) NOT NULL,
        CONSTRAINT aivao_id_pk PRIMARY KEY(id));""")

    cursor.execute ("""CREATE TABLE voo (
        id INTEGER NOT NULL,
        id_aviao INTEGER NOT NULL,
        id_cidade_origem INTEGER NOT NULL,
        id_cidade_destino INTEGER NOT NULL,
        data DATE NOT NULL,
        horario TIME NOT NULL,
        duracao TIME,
        CONSTRAINT voo_id_pk PRIMARY KEY(id),
        CONSTRAINT voo_id_aviao_fk FOREIGN KEY(id_aviao) REFERENCES aviao(id),
        CONSTRAINT voo_id_cidade_origem_fk FOREIGN KEY(id_cidade_origem) REFERENCES cidade(id),
        CONSTRAINT voo_id_cidade_destino_fk FOREIGN KEY(id_cidade_destino) REFERENCES cidade(id));""")
    
    cursor.execute ("""INSERT INTO cidade VALUES
        (1, 'Cuiabá'),
        (2, 'Campo Grande'),
        (3, 'Goiânia'),
        (4, 'Brasília');""")

    cursor.execute ("""INSERT INTO aviao VALUES
        (1, 'Airbus A320'),
        (2, 'Boeing 767');""")

    cursor.execute ("""INSERT INTO voo VALUES
        (1, 1, 1, 2, '2020-11-01', '10:00:00', '02:00:00'),
        (2, 1, 2, 3, '2020-11-01', '14:00:00', '04:00:00'),
        (3, 1, 3, 1, '2020-11-03', '20:00:00', '03:00:00'),
        (4, 1, 1, 3, '2020-11-04', '07:00:00', '03:00:00'),
        (5, 2, 2, 4, '2020-11-01', '10:00:00', '01:00:00'),
        (6, 2, 4, 1, '2020-11-01', '17:00:00', '01:00:00');""")

    conn.commit()

    print ('Sucesso')
except:
    print ('Erro')

conn.close()






