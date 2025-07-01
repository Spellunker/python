from mysql.connector.errors import ProgrammingError
from db import new_connection

sql = "INSERT INTO contacts (name, tel) VALUES (%s, %s)"
args = ("Arnaldo", "98765-4321")

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(sql, args)
        connection.commit()
    except ProgrammingError as e:
        print(f"Error: {e.msg}")
    else:
        print("1 register inserted, ID: ", cursor.lastrowid)
