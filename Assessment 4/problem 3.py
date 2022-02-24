
import pandas as pd

#read the csv file
df=pd.read_csv(r'/content/drive/MyDrive/nba.csv')

#display 1st 5 rows
res1=df.head(n=5)
print ("\nTop 5 rows: \n",res1)


#dimension of desired data
df_shape = df.shape
print ("\nDimension:",df_shape)

#type of column datatype
typ=df.dtypes
print("\nColumn Datatypes:\n",typ)

#display statistics of data
res_statis=df.describe()
print("\nStatistics :\n",res_statis)


#display median on dataframe
reult_median=df.median()
print("\n\nMedian on dataframe:  \n",suii)

#median on age column
mde_res=df['Age'].median()
print("\nMedian of Age :", mde_res)

