

# Print the index of values in list whose sum is the given value:


li=[2,5,8,9]
val=11
for i in range(0,len(li)):
  sum=0
  for j in range(i+1,len(li)):
    #print("j:{}" .format(li[j]))
    sum=li[i]+li[j]
    #print(sum)
    if(sum==val):
      print("found")
      print("index of i:{} and index of j: {} " .format(i,j))
      break
    
    
    -------------------------------------------------------------------------------------------
    #                     Output:
    #                           found
    #                           index of i:0 and index of j: 3 
