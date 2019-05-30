#!/usr/bin/python3

import pymysql

db = pymysql.connect("localhost", "users", "users", "users")

cursor = db.cursor()

#cursor.execute("SELECT VERSION()")
#data = cursor.fetchone()
#print(data)

#database connection is working


#CREATE database table
#sql = """CREATE TABLE TestUsers (
#        name CHAR(20) NOT NULL, 
#        location CHAR(100), 
#        gender CHAR(1), 
#        age INTEGER)"""

#cursor.execute(sql)

#table created successfully


#INSERT in to database
#sql = """INSERT INTO TestUsers (name, location, gender, age)
#    VALUES('Test', 'US', 'M', 40)"""

#use try block... in case something goes wrong, the database rolls back to a valid state
#try:
#    cursor.execute(sql)
#    db.commit()
#except:
#    db.rollback()


#UPDATE database
update = """UPDATE TestUsers SET Age = 35 WHERE Name = 'Test'"""
try:
    cursor.execute(update)
    db.commit()
except:
    db.rollback()


#READ from database
sql = """SELECT * FROM TestUsers"""

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for x in results:
        name = x[0]
        location = x[1]
        gender = x[2]
        age = x[3]
        print("Name: ", name, " Location: ", location, " Gender: ", gender, " Age ", age)
except:
    print("Unable to get information from database")



#DELETE from database
delete = """DELETE FROM TestUsers WHERE NAME = 'Test'"""

try:
    cursor.execute(delete)
    db.commit()
except:
    db.rollback()

db.close()
