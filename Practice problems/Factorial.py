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

-------------------------------------------------------------------------------------------------------------------------------------------------
#recursion  ALWAYS USE THIS METHOD IN PYTHON

def factorial(num):
  if num==0 or num==1:
    return num
 else:
  return num*factorial(num-1)

number = int(input("Enter a number: "))

# check if the number is negative
if number < 0:
   print("factorial does not exist for negative numbers")
else:
   print(factorial(number))
