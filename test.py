import mysql.connector
from mysql.connector import (connection)
from tabulate import tabulate

db = connection.MySQLConnection(user='sql11491613', password='eWFcPv5Ndt',
                                 host='35.157.16.43',
                                 database='sql11491613')

mycursor = db.cursor()
db_name= "sql11491613"

print("\n columns in user table:")
users=mycursor.execute("SHOW columns FROM users;")
for x in mycursor:
    print(x)

users=mycursor.execute("SHOW columns FROM roles;")
for x in mycursor:
    print(x)

print("\n all from users:")
users=mycursor.execute("SELECT * FROM users;")
for x in mycursor:
    print(x)

roles = mycursor.execute("SELECT * FROM roles;")
for x in mycursor:
    print(x)

# test=  mycursor.execute('update users set roleId = 2 where userID = 20')
# db.commit()
print("\n all from projects:")
projects=mycursor.execute("SELECT * FROM projects;")
for x in mycursor:
    print(x)

print("\n all from setups:")
setups=mycursor.execute("SELECT * FROM setups;")
for x in mycursor:
    print(x)

print("\n all from chains:")
chains=mycursor.execute("SELECT * FROM chains;")
for x in mycursor:
    print(x)


print("\n ALL tables from projects to gearunits:")
all=mycursor.execute("""SELECT projects.projectID, gearunits.gearunitName FROM projects
CROSS JOIN sessions
ON projects.projectID=sessions.projectID
CROSS JOIN setups
ON sessions.setupID=setups.setupID
CROSS JOIN setup_chain
ON setup_chain.setupID=setups.setupID
CROSS JOIN chains
ON setup_chain.chainID=chains.chainID
CROSS JOIN chain_gearunit
ON chains.chainID=chain_gearunit.chainID
CROSS JOIN gearunits
ON chain_gearunit.gearunitID=gearunits.gearunitID""")
for x in mycursor:
    print(x)
myresult = mycursor.fetchall()
print(tabulate(myresult, headers=['ProjectID', 'gearunit Name'], tablefmt='psql'))



mycursor.close()

db.close()