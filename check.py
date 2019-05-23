
import sqlite3



#connection to the sqlite database file. if database is opened succesfully, it returns a connection object
conn=sqlite3.connect('mydatabase.db')

#create a cursor which is used for python programming on database
cur=conn.cursor()

#this is used to execute SQL statements
cur.execute("SELECT * FROM Students")

# fetch all the row in the table
rows=cur.fetchall()

print("table contents are given ---->")

# for loop to get  all the  row one by one
for row in rows:

	print(row)
conn.commit()
conn.close()
