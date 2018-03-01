"""
SQL Example Application
"""

import sqlite3
import random

with sqlite3.connect("newnum.db") as conn:
	c = conn.cursor()
	
	rand_num = ()
	
	for num in range(1,100):
		random_int = random.randint(1,100)
		rand_num.append(random_int)
	
	data = rand_num
	print(data)
	
	#c.execute("""CREATE TABLE Integers(Integers INT)""")
	#c.execute("""INSERT INTO Integers VALUES(?), data""")
	
