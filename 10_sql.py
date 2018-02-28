"""
SQL Functions
"""
"""
|---------------|-----------------------------------------|
|   Function:   |                 Result:                 |
|---------------|-----------------------------------------|
|    AVG()      | Returns the average value from a group  |
|    COUNT()    | Returns the number of rows from a group |
|    MAX()      | Returns the largest value from a group  |
|    MIN()      | Returns the smallest value from a group |
|    SUM()      | Returns the sum of a group of values    |
|---------------|-----------------------------------------|
"""
import sqlite3

with sqlite3.connect("new.db") as conn:
	c = conn.cursor()
	
	#create dictionary of SQL queries with funcion
	sql = {"average":"SELECT avg(Population) FROM Population",
	       "maximum":"SELECT max(Population) FROM Population",
	       "minimum":"SELECT min(Population) FROM Population",
	       "sum":"SELECT sum(Population) FROM Population",
	       "count":"SELECT count(City) FROM Population",}
	
	#loop over dictionary of queries
	for keys,values in sql.items():
		
		#run sql:
		c.execute(values)
		
		#fetchone() retrieves one record from the query
		result = c.fetchone()
		
		#output the result to the screen
		print(keys + ":", result[0])
		
