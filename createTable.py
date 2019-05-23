
import sqlite3


#connection to the sqlite database file. if database is opened succesfully, it returns a connection object
conn=sqlite3.connect('mydatabase.db')

#create a cursor which is used for python programming on database
c=conn.cursor()


#this is used to execute SQL statements
#if Students table doesn't exist create new one 
c.execute("CREATE TABLE if not exists Students(Name varchar(30),regNo int primary key,roll int)")
#c.execute("pragma table_info(student)")

print("database and table has created successfully")

#commit all the changes did in this transaction
conn.commit()

#close the connection
conn.close()
