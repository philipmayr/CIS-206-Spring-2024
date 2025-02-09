# ASSIGNMENT XII - CIS 206 - phil may'r

import sqlite3

def add_column(table, column):
	cursor.execute("ALTER TABLE " + table + " ADD COLUMN " + column + " TEXT")
	connection.commit()

def update_row(table, column, where_column, row, value):
	cursor.execute("UPDATE " + table + " SET " + column + " = '" + value + "' WHERE " + where_column + " = '" + row + "'")
	connection.commit()

def update_column(table, column, value):
	cursor.execute("UPDATE " + table + " SET " + column + " = '" + value + "'")
	connection.commit()
	
def delete_row(table, column, row):
	cursor.execute("DELETE FROM " + table + " WHERE " + column + " = '" + row + "'")
	connection.commit()
	
def print_rows_and_columns(table):
	cursor.execute("SELECT * FROM " + table)
	print(cursor.fetchall())


table = 'colors'

connection = sqlite3.connect(table + ".db")
cursor = connection.cursor()

add_column(table, 'esp')
update_row(table, 'esp', 'color', 'Blue', 'Azul')
update_row(table, 'esp', 'color', 'Purple', 'Purpura')
update_row(table, 'esp', 'color', 'Bronze', 'Bronce')
update_row(table, 'esp', 'color', 'Amaranth', 'Amaranto')
update_row(table, 'esp', 'color', 'Chlorophyll', 'Clorofila')
update_row(table, 'esp', 'color', 'Olive', 'Oliva')
update_column(table, 'esp', '')
update_row(table, 'esp', 'color', 'Blue', 'Blao')
update_row(table, 'esp', 'color', 'Purple', 'Púrpura')
delete_row(table, 'color', 'Bronze')

print_rows_and_columns(table)

update_row(table, 'esp', 'color', 'Amaranth', 'Amaranto')
update_row(table, 'esp', 'color', 'Chlorophyll', 'Clorofila')
update_row(table, 'esp', 'color', 'Olive', 'Oliva')

cursor.close()
connection.close()
