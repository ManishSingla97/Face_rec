import sqlite3



# this function is for checking whether the student is present in our  database or do we need to make a new entry
def checkDatabase(regNo,name, roll) :                                            
    connect = sqlite3.connect("mydatabase.db")                                  # connecting to the database
                                                                          # selecting the row of an id into consideration
    cur = connect.execute("SELECT * FROM Students WHERE regNo = ? ",(regNo,))
    isRecordExist = False

    for row in cur:                                                          # checking wheather the id exist or not
        isRecordExist = True

    # if row does exist , update the parameters otherwise create a new entrys
    if isRecordExist == True:  
        print("record is updated")                                                # updating name and roll no
        connect.execute("UPDATE Students SET Name = ? WHERE regNo = ?",(name, regNo))
        connect.execute("UPDATE Students SET roll = ? WHERE regNo = ?",(roll, regNo))
    else:
        print("record is entered")
        #params = (Id, Name, roll)                                               # insering a new student data
        connect.execute("INSERT INTO Students(Name, regNo, roll) VALUES(?, ?, ?)", (name,regNo,roll))
    connect.commit()                                                            # commiting into the database
    connect.close()
