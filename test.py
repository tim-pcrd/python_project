import mysql.connector
from mysql.connector import (connection)

db = connection.MySQLConnection(user='sql11491613', password='eWFcPv5Ndt',
                                 host='35.157.16.43',
                                 database='sql11491613')

mycursor = db.cursor()
db_name= "sql11491613"

users=mycursor.execute("SHOW columns FROM roles;")
for x in mycursor:
    print(x)

users=mycursor.execute("SELECT * FROM users;")
for x in mycursor:
    print(x)

roles = mycursor.execute("SELECT * FROM roles;")
for x in mycursor:
    print(x)


mycursor.close()

db.close()