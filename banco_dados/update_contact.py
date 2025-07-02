from mysql.connector.errors import ProgrammingError
from db import new_connection

sql = "UPDATE contacts \
    SET name = %s \
    WHERE id = %s"
args = ("Beto", 15)

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(sql, args)
        connection.commit()
    except ProgrammingError as e:
        print(f"Error: {e.msg}")
    else:
        print(f"{cursor.rowcount} register(s) updated.")
