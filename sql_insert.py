"""
SQL Example Application
"""

import sqlite3
import random

with sqlite3.connect("newnum.db") as conn:
	c = conn.cursor()
	
	rand_num = []
	
	for num in range(1,101):
		list = []
		random_int = random.randint(1,100)
		list.append(random_int)
		rand_num.append(tuple(list))
	
	print(rand_num)
	
	#c.execute("""CREATE TABLE Integers(Integers INT)""")
	c.executemany("""INSERT INTO Integers VALUES(?)""",rand_num)
	
	
