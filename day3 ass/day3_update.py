#import mysql connector
import mysql.connector


#function to create connector
def get_connection():
    return mysql.connector.connect(
        host ="localhost",
        port = 3306,
        user = "sunbeam",
        password = "password",
        database = "iotdb"
    )

def update_employee(empid, doj):
    #get connection
    conn = get_connection()

    #for a query
    query= f"update employee SET doj =%s where empid = %s;"
    val = (doj , empid)

    #create a cursor
    cursor = conn.cursor()

    #execute the query
    cursor.execute(query, val)

    #commit the changes
    conn.commit()

    #close cursor as well as connection
    cursor.close()
    conn.close()


update_employee(32 ,"1/1/1996")    