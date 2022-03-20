num=int(input("enter the number:"))
for i in range(2,num):
  if num % i==0:
    print("non prime num")
    break
  else:
    print("Prime number")
    break


-----------------------
#output:
#       enter the number:11
#       Prime number
