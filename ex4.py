def computepay(h , r) :
    if h<=40:
        pay=h*r 
        return pay
    elif h>=40:
        payy=(40*r)+(h-40)*15.75
        return payy
    
hrs=float(input("Enter the hours"))
rate=float(input("Enter the pay"))


x=computepay(hrs,rate)
print("Pay" , x  )