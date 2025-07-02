from db import new_connection

sql = "SELECT * FROM contacts WHERE name like %s"

with new_connection() as connection:
    name = input("Contact to Find: ")
    args = (f"%{name}%", )
    cursor = connection.cursor()
    cursor.execute(sql, args)

    for x in cursor:
        print(x)
