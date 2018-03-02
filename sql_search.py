"""
SQL Example Application
"""

import sqlite3

with sqlite3.connect("newnum.db") as conn:
	c = conn.cursor()
	sql = {"avg":"SELECT avg(Integers) FROM Integers",
	       "max":"SELECT max(Integers) FROM Integers",
	       "min":"SELECT min(Integers) FROM Integers",
	       "sum":"SELECT sum(Integers) FROM Integers",}		
		
	while True:
		ans = str(input("What would you like to do?(avg, max, min, sum, exit)" )).lower()
		for keys, values in sql.items():
			if ans == keys:
				c.execute(values)
				print(keys + ":",c.fetchone()[0])
		print()
		if ans == "exit":
			print("Good bye!")
			break
				
				
		
