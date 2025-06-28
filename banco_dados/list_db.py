from mysql.connector import connect

connection = connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="neves@123",
    auth_plugin='mysql_native_password'
)

cursor = connection.cursor()
cursor.execute("SHOW DATABASES")

for i, database in enumerate(cursor, start=1):
    print(f"Database {i}: {database[0]}")
