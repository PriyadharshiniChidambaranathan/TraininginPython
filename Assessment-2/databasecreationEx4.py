
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
 database="FILMS"
)

mycursor = mydb.cursor()

#TO CREATE DB
#mycursor.execute("CREATE DATABASE FILMS")

#TO CREATE TABLE
mycursor.execute("CREATE TABLE movies (Movie_name VARCHAR(255), Year_of_release VARCHAR(255), Genre VARCHAR(255), Awards_Won VARCHAR(255), Lead_Actor VARCHAR(255), Lead_Actress VARCHAR(255))")
#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

#to show table created
#mycursor.execute("SHOW TABLE")
#for x in mycursor:
# print(x)





