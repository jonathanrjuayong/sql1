"""
Searching for data
"""

import sqlite3

with sqlite3.connect("new.db") as conn:
	c = conn.cursor()
	c.execute("SELECT FirstName, LastName FROM Employees")
	
	rows = c.fetchall()
	for r in rows:
		print(r[0],r[1])
