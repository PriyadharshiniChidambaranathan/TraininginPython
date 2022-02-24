import requests

x = requests.delete('https://jsonplaceholder.typicode.com/todos/10')

#print the response text (the content of the requested file):
print(x.text)
response.status_code
