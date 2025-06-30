from db import new_connection

with new_connection() as connection:
    cursor = connection.cursor()
    cursor.execute("SHOW TABLES")

for i, table in enumerate(cursor, start=1):
    print(f"Database {i}: {table[0]}")
