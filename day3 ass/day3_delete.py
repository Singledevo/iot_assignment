import dbconn

def delete_employee(emid):
    # get connection
    conn = dbconn.get_connection()

    # form a query
    query = f"delete from employee where emid = %s;"
    val = (emid, )

    # create a cursor
    cursor = conn.cursor()

    # execute the query
    cursor.execute(query, val)

    # commit the changes
    conn.commit()

    # close cursor as well as connection
    cursor.close()
    conn.close()