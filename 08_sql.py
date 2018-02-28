"""
Join data from multiple tables
"""

import sqlite3

with sqlite3.connect("new.db") as conn:
	c = conn.cursor()
	
	#retrieve data
	c.execute("SELECT Population.City, Population.Population, Regions.Region FROM Population, Regions WHERE Population.City = Regions.City")
	
	for r in c.fetchall():
		print(r[0],r[1],r[2])
