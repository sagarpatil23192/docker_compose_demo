#!/usr/bin/python

import MySQLdb
import time

time.sleep(10)

# Open database connection
db = MySQLdb.connect("db","root","root","domo_mom_db")

# prepare a cursor object using cursor() method
cursor = db.cursor()

tweets = open("keywords.txt", "w")

sql = "SELECT * FROM directory"
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      fname = row[1]
      print>>tweets, fname
      # Now print fetched result
      print "fname=%s" % \
             (fname)
except:
   print "Error: unable to fecth data"

# disconnect from server
db.close()

