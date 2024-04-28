# ASSIGNMENT XI - CIS 206 - phil may'r

import sqlite3

def create_table():
	cursor.execute("CREATE TABLE IF NOT EXISTS colors(color TEXT, red REAL, green REAL, blue REAL, alpha REAL)")

def feed_data():
	data = [('Blue', 50.3, 75.6, 113.3, 1.0),
		('Purple', 75.6, 50.4, 113.3, 1.0),
		('Bronze', 113.3, 75.6, 50.4, 1.0),
		('Amaranth', 113.3, 50.4, 75.6, 1.0),
		('Chlorophyll', 50.4, 113.3, 75.6, 1.0),
		('Olive', 75.6, 113.3, 50.4, 1.0)]
			
	cursor.executemany("INSERT INTO colors VALUES (?, ?, ?, ?, ?)", data)
	
def list_rows_and_columns():
	cursor.execute("SELECT * FROM colors")
	for row in cursor.fetchall():
		print(row)
		
def print_row(row):
	cursor.execute("SELECT * FROM colors WHERE color=" + row)
	for row in cursor.fetchall():
		print(row)
		
def list_column(column):
	cursor.execute("SELECT " + column + " FROM colors")
	for row in cursor.fetchall():
		print(row[0])
		
def sum_column(column):
	cursor.execute("SELECT SUM(" + column + ") FROM colors")
	print(cursor.fetchone()[0])
	
def count_rows():
	cursor.execute("SELECT * FROM colors")
	count = len(cursor.fetchall())
	print(count)

def show_rows_and_columns():
	cursor.execute("SELECT * FROM colors")
	print(cursor.fetchall())
	

connection = sqlite3.connect("colors.db")
cursor = connection.cursor()

create_table()
feed_data()

list_rows_and_columns()
print()
print_row("'Blue'")
print()
list_column("color")
print()
sum_column("red")
print()
sum_column("green")
print()
sum_column("blue")
print()
count_rows()
print()
show_rows_and_columns()
print()

connection.commit()
cursor.close()
connection.close()
