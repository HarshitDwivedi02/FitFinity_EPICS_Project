import pandas as pd
import mysql.connector

 # Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="yoga_diet") 

# Read the Excel file into a pandas dataframe
df = pd.read_csv('C:\\Users\\ASUS\\Desktop\\FitFinity_EPICS_Project\\DATABASE 2 - Sheet1.csv')

# Replace NaN values with None
df = df.where(pd.notnull(df), None)

# Insert dataframe records into SQL table
cursor = mydb.cursor() 
for index, row in df.iterrows():
    values = tuple(row)
    placeholders = ', '.join('?' * len(values))
    query = f"INSERT INTO  VALUES ({placeholders})"
    cursor.execute(query, values)
mydb.commit()

# Close the database connection
mydb.close()
