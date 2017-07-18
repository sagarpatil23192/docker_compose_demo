#!/usr/bin/python

import MySQLdb
import time

time.sleep(20)

# Open database connection
db = MySQLdb.connect("db","root","root","domo_mom_db")

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "INSERT INTO directory (email, phone_number) values ('sagar@gmail.com', '9595504298')"
try:
   # Execute the SQL command
   cursor.execute(sql)
except:
   print "Error: unable to fecth data"

# disconnect from server
db.close()
