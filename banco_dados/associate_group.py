from mysql.connector.errors import ProgrammingError
from db import new_connection

select_group = "SELECT id FROM grupos WHERE description = %s"
update_contact = "UPDATE contacts SET group_id = %s WHERE name = %s"

group_contact = {
    "Ana": "House",
    "Bia": "Work",
    "Luca": "House",
    "Lu": "House",
    "Gui": "Work",
    "Beca": "Work",
    "Pedro": "Work",
    "Beto": "House",
}

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        for contact, group in group_contact.items():
            cursor.execute(select_group, (group, ))
            group_id = cursor.fetchone()[0]
            cursor.execute(update_contact, (group_id, contact))
            connection.commit()
    except ProgrammingError as e:
        print(f"Error: {e.msg}")
    else:
        print("Contacts Associated.")

