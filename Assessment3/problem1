
t = int(input("Testcase: "))  
for i in range (1,t+1):
    N = int(input("Size:"))
    input_matrix = []
    #to get matrix
    for i in range(N):
        raw_input = input().split(" ")
        input_matrix.append([int(s) for s in raw_input])
        
        
    #to print input matrix
#    print("output")
#    for i in range(N):
#	    for j in range(N):
#		    print(input_matrix[i][j], end = " ")
#	    print()
    
    #to find output for sum_of_diagonals
    sum_of_diagonals=0
    row_repeated=0
    column_repeated=0
    for i in range(N):
      sum_of_diagonals+=input_matrix[i][i]
    
    # to find repeated elements in column
    for i in range(N):
       col_dup = set()
       for j in range(N):
           col_dup.add(input_matrix[j][i])
       if len(col_dup) != N:
           column_repeated += 1
           
    
    #to find repeated elements in row
    for i in range(N):
      row_duplicate = set(input_matrix[i])      
      if len(row_duplicate) != N:
        row_repeated += 1
        
    print("Case #{}: {} {} {}".format(i, sum_of_diagonals, row_repeated, column_repeated))
