
import mysql.connector
import json

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
 database="films"
)

mycursor = mydb.cursor()

class create_dict(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value

mydict = create_dict()
select_movie = """SELECT * FROM movies"""
cursor=mydb.cursor()

cursor.execute(select_movie)
result = cursor.fetchall()

for row in result:
	mydict.add(row[0],({"Year_of_release":row[1],"Genre":row[2], "Awards_won":row[3], "Lead_actor":row[4], "Lead_actress":row[5]}))
    

stud_json = json.dumps(mydict, indent=2, sort_keys=True)

#To view output in Json format
print(stud_json)

with open('movies_data.json', 'w') as f:
	f.write(stud_json)


