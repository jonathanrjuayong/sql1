"""
Homework
"""

import sqlite3

with sqlite3.connect("cars.db") as conn:
	c = conn.cursor()
	
	sql = {"Focus count:":"SELECT count(Model) FROM Orders WHERE Model = 'Focus' ",
	       "Fiesta count:":"SELECT count(Model) FROM Orders WHERE Model = 'Fiesta' ",
	       "Explorer count:":"SELECT count(Model) FROM Orders WHERE Model = 'Explorer' ",
	       "Civic count:":"SELECT count(Model) FROM Orders WHERE Model = 'Civic' ",
	       "Accord count:":"SELECT count(Model) FROM Orders WHERE Model = 'Accord' ",}
	
	c.execute("""SELECT Inventory.Model, Inventory.Make, Inventory.Quantity
	             FROM Inventory""")
	             
	for r in c.fetchall():
		print(r[0],r[1],r[2])
		for keys, values in sql.items():
			c.execute(values)
			results = c.fetchall()
			print(keys[results] + ":", results[0])
			
	
	
		
			
		
		
