import math
import statistics
import numpy as np
import scipy.stats



import pandas as pd
df=pd.read_csv(r'/content/drive/MyDrive/nba.csv')
#display 1st 5 rows
res1=df.head(n=5)
  #print (res1)


#dimension of desired data
df_shape = df.shape
   #print (df_shape)

#type of column datatype
print(df.dtypes)

#median of age
mad=df[Age]
df = pd.read_csv("sample_file.csv")
median= statistics.median(df[mad])
print(median)
