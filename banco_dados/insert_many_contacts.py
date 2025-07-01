from mysql.connector.errors import ProgrammingError
from db import new_connection

sql = "INSERT INTO contacts (name, tel) VALUES (%s, %s)"
args = (
    ("Ana", "88765-4321"),
    ("Bia", "97765-4321"),
    ("Luca", "96765-4321"),
    ("Lu", "98765-4321"),
    ("Gui", "98764-4321"),
    ("Beca", "98763-4321"),
    ("Pedro", "98762-4321"),
    )

with new_connection()  as connection:
    try:
        cursor = connection.cursor()
        cursor.executemany(sql, args)
        connection.commit()
    except ProgrammingError as e:
        print(f"Error: {e.msg}")
    else:
        print(f"{cursor.rowcount} registers inserted")
