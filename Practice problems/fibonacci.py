val1=int(input("Enter 1st val:" ))
val2=int(input("Enter 2nd val:" ))
num=int(input("Enter range:" ))
print(val1,val2,end=" ")
while(num-2):
  sum=val1+val2
  val1=val2
  val2=sum
  num-=1
  print(sum, end=" ")
  
  
  -----------------------------------------------------------
 # o/p:
 #   Enter 1st val:0
 #   Enter 2nd val:1
 #   Enter range:10
 #   0 1 1 2 3 5 8 13 21 34 
