from db import new_connection
from mysql.connector.errors import ProgrammingError

wrong_delete = """
    DROPY TABLE emails
"""

right_delete = """
    DROP TABLE IF EXISTS emails
"""

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(right_delete)
        cursor.execute(wrong_delete)
    except ProgrammingError as e:
        print(f"Error: {e.msg}")
