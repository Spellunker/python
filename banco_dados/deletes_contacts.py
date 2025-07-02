from mysql.connector.errors import ProgrammingError
from db import new_connection

sql = "DELETE FROM contacts WHERE name = %s"
args = ("Arnaldo", )

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(sql, args)
        connection.commit()
    except ProgrammingError as e:
        print(f"Error: {e.msg}")
    else:
        print(f"{cursor.rowcount} record(s) deleted.")
