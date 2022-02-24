
import requests 
import json


api_url = "https://jsonplaceholder.typicode.com/todos/10"

data = {'userId':1,'id':10,'Address and pincode':'try_01', 'completed':'true'}
response=requests.put(api_url,json=data)


print(response.text)
response.status_code
