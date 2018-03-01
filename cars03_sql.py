"""
Homework
"""

import sqlite3
"""
with sqlite3.connect("cars.db") as conn:
	c = conn.cursor()
	
	sql = {"Focus count:":"SELECT count(Model) FROM Orders WHERE Model = 'Focus' ",
	       "Fiesta count:":"SELECT count(Model) FROM Orders WHERE Model = 'Fiesta' ",
	       "Explorer count:":"SELECT count(Model) FROM Orders WHERE Model = 'Explorer' ",
	       "Civic count:":"SELECT count(Model) FROM Orders WHERE Model = 'Civic' ",
	       "Accord count:":"SELECT count(Model) FROM Orders WHERE Model = 'Accord' ",}
	
	for keys, values in sql.items():
		c.execute(values)
		results = c.fetchone()
		print(keys , results[0])
"""
		
with sqlite3.connect("cars.db") as conn:
	c = conn.cursor()
	
	c.execute("""SELECT * FROM Inventory""")
	
	for r in c.fetchall():
		print(r[0],r[1], "\n","Quantity:", r[2])	
		c.execute("""SELECT count(OrderDate)
		             FROM Orders 
		             WHERE Make=? and Model=?""",(r[0],r[1]))
		order_count = c.fetchone()[0]
		print("Orders",order_count)	
		print()
