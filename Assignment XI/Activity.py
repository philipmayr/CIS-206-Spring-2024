import sqlite3

connection = sqlite3.connect('colors.db')
cursor = connection.cursor()

def create_table():
	cursor.execute('CREATE TABLE IF NOT EXISTS colors(color TEXT, red REAL, green REAL, blue REAL, alpha REAL)')

def feed_data():
	cursor.execute("INSERT INTO colors VALUES('Blue', 50.3, 75.6, 113.3, 1.0)")
	cursor.execute("INSERT INTO colors VALUES('Purple', 75.6, 50.4, 113.3, 1.0)")
	cursor.execute("INSERT INTO colors VALUES('Bronze', 113.3, 75.6, 50.4, 1.0)")
	cursor.execute("INSERT INTO colors VALUES('Amaranth', 113.3, 50.4, 75.6, 1.0)")
	cursor.execute("INSERT INTO colors VALUES('Chlorophyll', 50.4, 113.3, 75.6, 1.0)")
	cursor.execute("INSERT INTO colors VALUES('Olive', 75.6, 113.3, 50.4, 1.0)")

	connection.commit()
	cursor.close()
	connection.close()

create_table()
feed_data()
