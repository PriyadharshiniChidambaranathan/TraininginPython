#without recursion
def factorial(num):
  if num==0 or num==1:
    return num
  
  else:
    fact=1  
    while(num>0):
      fact=fact*num
      num-=1
      return fact

num=int(input("value:"))
ans=factorial(num)
print("Factorial of {} is {}".format(num,ans))


#recursion
def factorial(num):
  if num==0 or num==1:
    return num
 else:
  return 
