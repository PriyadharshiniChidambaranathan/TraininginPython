dict = {}
while True:
  user=input("Do you want Add/Modify Dictionary or Exit:")
  if user=='Add':
    key=input("Enter the key to add:")
    value=input("Enter the value to add:")
    dict[key]=value
    print(dict)
    continue
  elif user=='Modify':
    key=input("Enter the key to modify:")
    value=input("Enter the value to modify:")
    dict.update({key.value})
    print(dict)
    continue
  else: user_input=='Exit'
  break
    
