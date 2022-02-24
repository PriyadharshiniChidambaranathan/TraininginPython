import pandas as pd
#read the csv file
df=pd.read_csv(r'/content/drive/MyDrive/nba.csv')

#display 1st 5 rows
res1=df.head(n=5)
print (res1)


#dimension of desired data
df_shape = df.shape
print (df_shape)

#type of column datatype
print(df.dtypes)
