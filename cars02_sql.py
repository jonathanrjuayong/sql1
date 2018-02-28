"""
Homework
"""

import sqlite3

#add another table called "orders"

with sqlite3.connect("cars.db") as conn:
	c = conn.cursor()
	
	#data values:
	orders = (
	        ("Ford","Focus","2018-02-13"),
	        ("Ford","Focus","2018-02-14"),
	        ("Ford","Focus","2018-02-15"),
	        ("Ford","Fiesta","2018-02-12"),
	        ("Ford","Fiesta","2018-02-10"),
	        ("Ford","Fiesta","2018-02-11"),
	        ("Ford","Explorer","2018-02-03"),
	        ("Ford","Explorer","2018-02-05"),
	        ("Ford","Explorer","2018-02-02"),
	        ("Honda","Civic","2018-01-03"),
	        ("Honda","Civic","2018-01-23"),
	        ("Honda","Civic","2018-01-09"),
	        ("Honda","Accord","2018-01-13"),
	        ("Honda","Accord","2018-01-19"),
	        ("Honda","Accord","2018-01-24"),
	)
	
	#create table then input data
	#c.execute("""CREATE TABLE Orders (Make TEXT, Model TEXT, OrderDate TEXT)""")
	#c.executemany("""INSERT INTO Orders VALUES(?,?,?)""", orders)
	
	#Select data from two tables: Inventory & Orders
	c.execute("""SELECT Inventory.Make, Inventory.Model, Inventory.Quantity, Orders.OrderDate
	             FROM Inventory, Orders
	             WHERE Inventory.Model = Orders.Model""")
	
	for r in c.fetchall():
		print("Make:",r[0])
		print("Model:",r[1])
		print("Quantity:",r[2])
		print("Order Date:",r[3])
		print()
	
	
