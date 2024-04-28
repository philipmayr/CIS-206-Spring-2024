# ASSIGNMENT XII - CIS 206 - phil may'r

import sqlite3

def add_column():
	cursor.execute("ALTER TABLE colors ADD COLUMN esp TEXT")

def add_rows():
	data = [('Blue', 'Azul')
		    ('Purple', 'Púrpura'),
			('Bronze', 'Bronce'),
			('Amaranth', 'Amaranto'),
			('Chlorophyll', 'Clorofila'),
			('Olive', 'Oliva')]
	cursor.executemany("UPDATE colors SET esp = ? WHERE color = ?", data)
	

connection = sqlite3.connect("colors.db")
cursor = connection.cursor()

connection.commit()
cursor.close()
connection.close()

