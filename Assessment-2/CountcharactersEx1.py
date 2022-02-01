#Using Regex Method
import  re

string=input(" ")
  
# Creating separate lists using 
# the re.findall() method.
uppercase = re.findall(r"[A-Z]", string)
lowercase = re.findall(r"[a-z]", string)
numbers = re.findall(r"[0-9]", string)
special = re.findall(r"[, .!?]", string)
space = re.findall(r"[ ]", string)
  
print("No. of uppercase characters =", len(uppercase))
print("No. of lowercase characters =", len(lowercase))
print("No. of numerical characters =", len(numbers))
print("No. of special characters =", len(special))
print("No. of white space characters =", len(space))




# Using basic Method
str=input(" ")#take input from the user
upper, lower, num, special, space=0,0,0,0,0;#variable declaration and initilization
for i in range(len(str)):
  if(str[i]>='A' and str[i]<='Z'):#check upper case letters
     upper+=1
  elif(str[i]>='a' and str[i]<='z'):#check lower case letter
     lower+=1
  elif(str[i]>='0' and str[i]<='9'):#check numeric value
      num+=1
  elif(str[i]==" "):
     space+=1 
  else:
      special+=1
print("No.of uppercase characters =",upper)
print("No.of lowercase characters =",lower)
print("No.of numberical characters =",num)
print("No.of special characters =",special)
print("No.of white space characters =",space)
