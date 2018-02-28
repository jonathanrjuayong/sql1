"""
Join data from multiple tables - cleanup
"""

import sqlite3

with sqlite3.connect("new.db") as conn:
	c = conn.cursor()
	
	#retrieve data
	c.execute("""SELECT Population.City, Population.Population, Regions.Region 
	             FROM Population, Regions 
	             WHERE Population.City = Regions.City""")
	
	for r in c.fetchall():
		print("City:",r[0])
		print("Population:",r[1])
		print("Region",r[2])
		print()
