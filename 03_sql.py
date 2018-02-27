"""
Importing data from CSV file
"""

import sqlite3
import csv
import os

csv_path = r"C:\Users\Jonathan\Documents\MEGA\RealPython\book2-exercises-master\sql"
csv_file = os.path.join(csv_path,"employees.csv")

# import data from csv file then insert it into new table: employees
with sqlite3.connect("new.db") as conn:
	try:
		c = conn.cursor()
		file_reader = csv.reader(open(csv_file,"rU"))
		#c.execute("CREATE TABLE Employees(FirstName TEXT, LastName TEXT)")
		c.executemany("INSERT INTO Employee(FirstName,LastName) VALUES(?,?)",file_reader)
	except sqlite3.OperationalError:
		print("Oops! Something went wrong. Please try again...")
		
