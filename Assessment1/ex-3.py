# Factorial of a number using recursion

def factorial(num):
   if (num == 1) or (num==0):
       return num
   else:
       return num*factorial(num-1)

number = int(input("Enter a number: "))

# check if the number is negative
if number < 0:
   print("factorial does not exist for negative numbers")
else:
   print(factorial(number))
