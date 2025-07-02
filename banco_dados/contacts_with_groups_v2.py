from collections import defaultdict
from mysql.connector.errors import ProgrammingError
from db import new_connection

sql = """
    SELECT
        grupos.description AS grupo,
        contacts.name AS name
    FROM contacts
    INNER JOIN grupos ON contacts.group_id = grupos.id
    ORDER BY grupo, name
"""

with new_connection() as connection:
    try:
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute(sql)
            contacts = cursor.fetchall()
        finally:
            cursor.close()
    except ProgrammingError as e:
        print(f"Error = {e.msg}")
    else:
        agrupados = defaultdict(list)
        for contact in contacts:
            agrupados[contact['grupo']].append(contact['name'])

        print(agrupados)
