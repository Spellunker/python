from mysql.connector import connect

connection = connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="neves@123",
    auth_plugin='mysql_native_password'
)

cursor = connection.cursor()
# CREATE DATABASE IF NOT EXISTS schedule
cursor.execute("CREATE DATABASE schedule")
