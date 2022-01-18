
k=input("Please input a key: ") 
v=input("Plesse input a value: ") 
d={k:v} 

#d={'A':1,'B':2,'C':3}
key=input("key = ")
if key in d.keys():
      print("Present,value =",end=" ")
      print(d[key])
else:
      print("Not present")
