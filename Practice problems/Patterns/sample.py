num=5
m=(2*num)-2
for i in range(0,num):
  for j in range(0,m):
    print(end="0 ")
  m-=1
  for j in range(0,i+1):
    print("*",end=" ")
  for j in range (0,i+1):
    print("L",end=" ")
  print(" ")
  
  
  
  ---------------------------------------------
  # output:
  #                   0 0 0 0 0 0 0 0 * L  
  #                   0 0 0 0 0 0 0 * * L L  
  #                   0 0 0 0 0 0 * * * L L L  
  #                   0 0 0 0 0 * * * * L L L L  
  #                   0 0 0 0 * * * * * L L L L L 
  #
  #
  #
