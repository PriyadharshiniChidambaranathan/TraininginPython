
t = int(input("Testcase: ")) 
out=0 
sum=[]
row=[]
col=[]
for i in range (1,t+1):
    N = int(input("Size:"))
    input_matrix = []
    #to get matrix
    
    for i in range(N):
        raw_input = input().split(" ")
        input_matrix.append([int(s) for s in raw_input])
        
        
    #to find output for sum_of_diagonals and rows repeated
    
    sum_of_diagonals=0
    row_repeated=0
    column_repeated=0
    for i in range(N):
      sum_of_diagonals+=input_matrix[i][i]
      row_duplicate = set(input_matrix[i])      
      if len(row_duplicate) != N:
        row_repeated += 1
    
    
    # to find repeated elements in column
    
    for i in range(N):
       col_dup = set()
       for j in range(N):
           col_dup.add(input_matrix[j][i])
       if len(col_dup) != N:
           column_repeated += 1             
    
   
    sum.append(sum_of_diagonals)
    col.append(column_repeated)
    row.append(row_repeated)


for i in range(1,t+1):
  out=1+i
  print("Case #{}: {} {} {}".format(i, sum[i-1],row[i-1],col[i-1]))
