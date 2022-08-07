import mysql.connector

mydb = mysql.connector.connect(
    host="db",
    user="root",
    passwd="password123",
    database='my_websites',
    auth_plugin='mysql_native_password'
)

my_cursor = mydb.cursor()
#my_cursor.execute("DROP DATABASE my_websites")
#my_cursor.execute("CREATE DATABASE my_websites")
my_cursor.execute("CREATE TABLE sites (site_url varchar(255), site_colour varchar(255));")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)
