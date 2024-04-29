# ASSIGNMENT XI - CIS 206 - phil may'r

import sqlite3

def create_table(table, columns):
	cursor.execute("CREATE TABLE IF NOT EXISTS " + table + "(" + columns + ")")
	connection.commit()

def feed_data(table, data):
	cursor.executemany("INSERT INTO " + table + " VALUES (?, ?, ?, ?, ?)", data)
	connection.commit()
	
def list_rows_and_columns(table):
	cursor.execute("SELECT * FROM " + table)
	for row in cursor.fetchall():
		print(row)
		
def print_row(table, row):
	cursor.execute("SELECT * FROM " + table + " WHERE color = " + row)
	for row in cursor.fetchall():
		print(row)
		
def list_column(table, column):
	cursor.execute("SELECT " + column + " FROM " + table)
	for row in cursor.fetchall():
		print(row[0])
		
def sum_column(table, column):
	cursor.execute("SELECT SUM(" + column + ") FROM " + table)
	return cursor.fetchone()[0]
	
def count_rows(table):
	cursor.execute("SELECT * FROM " + table)
	count = len(cursor.fetchall())
	return count

def show_rows_and_columns(table):
	cursor.execute("SELECT * FROM " + table)
	print(cursor.fetchall())
	

table = 'colors'

connection = sqlite3.connect(table + ".db")
cursor = connection.cursor()

data = [('Blue', 50.3, 75.6, 113.3, 1.0),
	('Purple', 75.6, 50.4, 113.3, 1.0),
	('Bronze', 113.3, 75.6, 50.4, 1.0),
	('Amaranth', 113.3, 50.4, 75.6, 1.0),
	('Chlorophyll', 50.4, 113.3, 75.6, 1.0),
	('Olive', 75.6, 113.3, 50.4, 1.0)]

columns = 'color TEXT, red REAL, green REAL, blue REAL, alpha REAL'
create_table(table, columns)
feed_data(table, data)

list_rows_and_columns(table)
print_row(table, 'Blue')
print()
list_column(table, 'color')
print()
print(sum_column(table, 'red'))
print()
print(sum_column(table, 'green'))
print()
print(sum_column(table, 'blue'))
print()
print(count_rows(table))
print()
show_rows_and_columns(table)

cursor.close()
connection.close()
