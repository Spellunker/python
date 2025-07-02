from db import new_connection
from mysql.connector.errors import ProgrammingError

create_group_table = """
    CREATE TABLE IF NOT EXISTS grupos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        description VARCHAR(30)
    )
"""

alter_contact_table_1 = """
    ALTER TABLE contacts ADD group_id INT
"""

alter_contact_table_2 = """
    ALTER TABLE contacts ADD FOREIGN KEY (group_id)
    REFERENCES grupos(id)
"""

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(create_group_table)
        cursor.execute(alter_contact_table_1)
        cursor.execute(alter_contact_table_2)
    except ProgrammingError as e:
        print(f"Error: {e.msg}")
