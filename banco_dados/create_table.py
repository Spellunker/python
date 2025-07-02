from mysql.connector.errors import ProgrammingError
from db import new_connection

contact_table = """
    CREATE TABLE IF NOT EXISTS contacts (
        name VARCHAR(50),
        tel VARCHAR(40)
        )
"""

emails_table = """
    CREATE TABLE IF NOT EXISTS emails(
        id INT AUTO_INCREMENT PRIMARY KEY,
        owner VARCHAR(50)
    )
"""

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(contact_table)
        cursor.execute(emails_table)
    except ProgrammingError as e:
        print(f"Error: {e.msg}")
