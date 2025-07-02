from db import new_connection

sql = "SELECT * FROM contacts WHERE name like 'lu%'"

with new_connection() as connection:
    cursor = connection.cursor()
    cursor.execute(sql)

    for x in cursor:
        print(x)
