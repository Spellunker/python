from db import new_connection

sql = "SELECT name, tel FROM contacts LIMIT 3 OFFSET 5"

with new_connection() as connection:
    cursor = connection.cursor()
    cursor.execute(sql)
    
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
