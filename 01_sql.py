import sqlite3
"""
with sqlite3.connect("new.db") as conn:
	c = conn.cursor()
	c.execute("CREATE TABLE Population(City TEXT, State TEXT, Population TEXT)")
"""
with sqlite3.connect("cars.db") as conn:
	c = conn.cursor()
	c.execute("CREATE TABLE Inventory(Make TEXT, Model TEXT, Quantity INT)")
