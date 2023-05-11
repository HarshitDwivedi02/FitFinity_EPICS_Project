import mysql.connector
# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="users_info") 

#Create cursor
cursor = mydb.cursor()
cursor.execute("USE {}".format('users_info'))
# Create a table to store user details
mydb.execute('''CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                gender TEXT NOT NULL,
                height REAL NOT NULL,
                weight REAL NOT NULL)''')