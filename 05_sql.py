"""
Updating and deleting
"""

import sqlite3

new_york = ("New York City","NY",8500000)


with sqlite3.connect("new.db") as conn:
	c = conn.cursor()
	c.execute("INSERT INTO Population VALUES(?,?,?)",new_york)
	c.execute("UPDATE Population SET Population = 9000000 WHERE City = 'New York City'")
	c.execute("DELETE FROM Population WHERE City = 'Boston'")
	print("\nNew Data\n")
	c.execute("SELECT * FROM Population")
	for rows in c.fetchall():
		print(rows[0],rows[1],rows[2])

"""
with sqlite3.connect("new.db") as conn:
	c = conn.cursor()
	c.execute("UPDATE Population SET City = 'New York City' WHERE City = 'NEW YORK CITY'")
	c.execute("SELECT * FROM Population")
	for rows in c.fetchall():
		print(rows[0],rows[1],rows[2])
"""
"""
with sqlite3.connect("new.db") as conn:
	c = conn.cursor()
	c.execute("DELETE FROM Population WHERE City = 'New York City'")
	c.execute("SELECT * FROM Population")
	for r in c.fetchall():
		print(r[0],r[1],r[2])
"""
