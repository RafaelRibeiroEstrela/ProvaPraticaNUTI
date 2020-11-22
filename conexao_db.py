

import sqlite3

class conection_db:

	def __init__(self):

		self.conn = sqlite3.connect ('companhia_aerea.db')

	def return_conn(self):

		conn = self.conn

		return conn


conection_db()
