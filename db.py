import pandas as pd
import numpy as np
import mysql.connector 

data = pd.read_csv('DATABASE 2 - Sheet1.csv')
print (data.head())


#CONNECTING THE MYSQL TO PYTHON 
from mysql.connector import *


connection = mysql.connector.connect(user='root', password='123456')
if (connection.is_connected()):
     print("Connection Successfull!!!")
else:
     print("Not connected")

#ESTABLISHING A CURSOR TO WORK WITH THE CONNECTION

cursor = connection.cursor()





#CREATING A DATABASE AND USING IT


# cursor.execute("CREATE DATABASE {}".format('survey_reports'))

# cursor.execute("USE {}".format('yoga_diet'))


# from sqlalchemy import create_engine

# engine = create_engine('mysql://root:123456@localhost/yoga_diet')

# data.to_sql('health_output', con=engine)
cursor.execute("SELECT * FROM health_output WHERE Health_Problems = 'Back Pain'")
cursor.fetchall()





