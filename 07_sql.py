"""
Create a new table
"""

import sqlite3

with sqlite3.connect("new.db") as conn:
	c = conn.cursor()
	
	#create new table
	#c.execute("CREATE TABLE Regions (City TEXT, Region TEXT)")
	
	#data values
	cities = (
	    ('New York City', 'Northeast'),
	    ('San Francisco', 'West'),
	    ('Chicago', 'Midwest'),
	    ('Houston', 'South'),
	    ('Phoenix', 'West'),
	    ('Boston', 'Northeast'),
	    ('Los Angeles', 'West'),
	    ('Houston', 'South'),
	    ('Philadelphia', 'Northeast'),
	    ('San Antonio', 'South'),
	    ('San Diego', 'West'),
	    ('Dallas', 'South'),
	    ('San Jose', 'West'),
	    ('Jacksonville', 'South'),
	    ('Indianapolis', 'Midwest'),
	    ('Austin', 'South'),
	    ('Detroit', 'Midwest')
	)
	
	#insert data into table
	#c.executemany("INSERT INTO Regions VALUES (?,?)",cities)
	
	c.execute("SELECT * FROM Regions ORDER BY region ASC")
	for r in c.fetchall():
		print(r[0],r[1])
	
