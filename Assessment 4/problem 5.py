import requests 
import pandas

#to read url
response = requests.get("https://jsonplaceholder.typicode.com/todos")

# To print http response code and response text
print("Return Code:",response.status_code,"\n")       
  #print(response.text)

#to print data of 5 rows
js=response.json()
print ("\nTop 7 rows: \n",js[0:5])
