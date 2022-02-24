import pandas
data ={'Name':['Jai','Prince','Gaurav','Anuj'],'Age':[27,24,22,32],'Qualification':['MSc','MA','MCA','Phd']}
data['Address']=['Delhi','Kanpur','Allahabad','Mumbai']
out_df=pandas.DataFrame(data)
print(out_df)
