from db import new_connection

sql = "SELECT name, id FROM contacts ORDER BY name DESC"

with new_connection() as connection:
    cursor = connection.cursor()
    cursor.execute(sql)

    print("\n".join(str(registro) for registro in cursor))
