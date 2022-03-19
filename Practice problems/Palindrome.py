def palindrome(num):
  pal=num[::-1]
  if pal==num:
    print("yes")
  else:
    print("no")

#num=input("value:")
#palindrome(num)
palindrome(input("value:"))
