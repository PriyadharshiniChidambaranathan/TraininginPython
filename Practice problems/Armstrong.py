val=int(input("Enter val:" ))
num=val
res=0
while(num>0):
  rem=num%10
  res=res+(rem**3)
  num=num//10
print(res)
if(res==val):
  print("{} is an armstrong number".format(val))
else:
  print("not")
  
  
  
  ------------------------------------------------
  #output:
  #     Enter val:153
  #     153
  #     153 is an armstrong number
