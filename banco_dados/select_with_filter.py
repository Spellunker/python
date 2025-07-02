from db import new_connection

sql = "SELECT * FROM contacts WHERE tel = '98765-4321'"

with new_connection() as connection:
    cursor = connection.cursor()
    cursor.execute(sql)
    
    for x in cursor:
        print(x)
