year=int(input("enter year:"))
if year%400 == 0:
  print("leap year")
elif year% 4==0:
  print("yes! leap year")
elif year%100==0:
  print("yes!leap year")
else:
  print("not a leap year")

  
  ------------------
  #output:
 #      enter year:1999
#       not a leap year
