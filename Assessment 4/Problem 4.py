
import pandas as pd

#read the csv file
df=pd.read_csv(r'/content/drive/MyDrive/matches.csv')

#display 1st 5 rows
res1=df.head(n=5)
print ("\nTop 5 rows: \n",res1)


#mean on win_by_wickets column
mn_res=df['win_by_wickets'].mean()
print("\nMean of win_by_wickets :", mn_res,"\n")

# display column list using column method
print("Column List:\n",df.columns,"\n")


#SD of win by wickets data
sd_res=df['win_by_wickets'].std()
print("\nSD of win_by_wickets :", sd_res,"\n")


#dataframe by grouping city and winner
ci_wi =df.groupby(["city", "winner"])
for key,item in ci_wi:
  grp_city=ci_wi.get_group(key)
  print(grp_city,"\n")
#print("Groupby City and winner\n",ci_wi)

#Conditional probability 
total_matches=(df['city'].value_counts()['Mumbai'])
Mumbai=(df['winner'].value_counts()['Mumbai Indians'])
probility=Mumbai/total_matches
print(probility)



