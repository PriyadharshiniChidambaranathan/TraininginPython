import mysql.connector

mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="films"
)

mycursor=mydb.cursor()

sql =" INSERT INTO movies (Movie_name, Year_of_release, Genre, Awards_Won, Lead_Actor, Lead_Actress) VALUES (%s, %s, %s, %s, %s, %s)"
val =[ ("JaiBeem", "2021", "Supese", "Flimfare", "Suriya", "lijo"),( "Doctor", "2021", "Comedy", "fifa", "SK", "Anjana")]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")



