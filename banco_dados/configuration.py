from mysql.connector import connect

connection = connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="neves@123",
    auth_plugin='mysql_native_password'
)

print(connection)
