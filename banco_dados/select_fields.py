from db import new_connection

sql = "SELECT name, tel FROM contacts"

with new_connection() as connection:
    cursor = connection.cursor()
    cursor.execute(sql)
    
    for contact in cursor.fetchall():
        print("\t".join(str(field) for field in contact))
