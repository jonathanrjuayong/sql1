"""
Homework
"""

import sqlite3

cars = (
("Ford","Focus",32),
("Ford","Fiesta",29),
("Ford","Explorer",34),
("Honda","Civic",41),
("Honda","Accord",22)
)

with sqlite3.connect("cars.db") as conn:
	c = conn.cursor()
	
	#insert new values to Inventory table
	#c.executemany("INSERT INTO Inventory VALUES(?,?,?)",cars)
	
	#update quantity
	#c.execute("UPDATE Inventory SET Quantity = 17 WHERE Model = 'Focus'")
	#c.execute("UPDATE Inventory SET Quantity = 37 WHERE Model = 'Civic'")
	
	#output Ford vehicles only
	c.execute("SELECT * FROM Inventory")
	for r in c.fetchall():
		if r[0] == "Ford":
			print(r[0],r[1],r[2])
