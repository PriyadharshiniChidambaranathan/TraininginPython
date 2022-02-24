import requests 
import pandas

#to print data of 7 rows
df=pd.read_json(r'https://jsonplaceholder.typicode.com/todos')
res1=df.head(n=7)
print ("\nTop 7 rows: \n",res1)
