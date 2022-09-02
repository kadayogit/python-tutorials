
import mysql.connector
# import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="", database="pythondb")

if conn.is_connected():
    print("Connection success!")
else:
   print("Could not connected!")

#create database 
mycursor = conn.cursor()

# execute the database
mycursor.execute("SELECT * FROM users")
for selectQ in mycursor:
    print(selectQ)