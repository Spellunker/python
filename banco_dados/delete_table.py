from db import new_connection
from mysql.connector.errors import ProgrammingError

right_delete = """
    DROP TABLE IF EXISTS emails
"""

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(right_delete)
    except ProgrammingError as e:
        print(f"Error: {e.msg}")
