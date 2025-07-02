from mysql.connector.errors import ProgrammingError
from db import new_connection

sql = "SELECT * FROM contacts LIMIT 5"

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        contacts = cursor.fetchall()
    except ProgrammingError as e:
        print(f"Error: {e.msg}")
    else:
        for contact in contacts:
            print(f"{contact[2]:2d} - {contact[0]:10s} Telephone: \
                  {contact[1]}")
