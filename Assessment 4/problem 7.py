
import requests 


api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {'userId':'10','title':'macaroni', 'completed':'false'}
response=requests.post(api_url, json=todo)
response.json()
print(response.text)
response.status_code
