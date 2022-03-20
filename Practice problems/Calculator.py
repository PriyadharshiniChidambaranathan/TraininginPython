def add(a,b):
  return a+b

def sub(a,b):
  return a-b


def mul(a,b):
  return a*b

def div(a,b):
  return a/b

def sqr(a):
  return a**2

def si(p,n,r):
  return (p*n*r)/100

def ci(P,R,T):
  return P * pow((1 + R/100),T)

def sqroot(a):
  return a**0.5


print("Add val is {}".format(add(2,3)))  
print("Sqrt val is {}".format(sqroot(4)))  
print("Ci val is {}".format(ci(2,4,3)))  


-----------------------------------------------------


# output:
#       Add val is 5
#       Sqrt val is 2.0
#       Ci val is 2.249728
