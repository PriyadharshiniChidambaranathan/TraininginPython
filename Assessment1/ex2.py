
num=[]
for val in range(2000,3200):
    if (val%7==0) and (val%5!=0):
        num.append(str(val))
print (','.join(num))

