# import module of mysql connector
import mysql.connector

# create a connection with mysql database server
connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "sunbeam",
    password = "password",
    database = "iotdb"
)

# create a query
emid = int(input("Enter emid : "))
name = input("Enter name : ")
dep = input("Enter department :")
email = input("Enter email : ")
salary = int(input("Enter salary : "))
doj = input("Enter date of joining : ")

query = f"insert into employee values({emid}, '{name}', '{dep}', '{email}', '{salary}', '{doj}');"

# create a cursor to execute the query
cursor = connection.cursor()

# execute query using cursor
cursor.execute(query)

# after execution of query commit your changes
connection.commit()

# close the cursor
cursor.close()

#close the connection with mysql server 
connection.close()