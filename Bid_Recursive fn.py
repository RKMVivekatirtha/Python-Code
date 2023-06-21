#1 Factorial
"""def factrecur(n):
    if(n==1):
        return(1)
    else:
        return(n*factrecur(n-1))


#main
n=int(input("Enter a no"))
x=factrecur(n)
print("Result is",x)"""




#2 HCF
"""def HCF(dvsr,dvdnt):
    a=dvdnt%dvsr
    if(a==0):
        return(dvsr)
    else:
        return(HCF(a,dvsr))



#main
x=int(input("Enter two numbers"))
y=int(input())
lg=max(x,y)
sm=min(x,y)
r=HCF(sm,lg)
print("HCF is ",r)"""



#3 x^n

#4 Fibonacci Series

#5 spcl no.(Not under recursive)
"""def chkspcl(n):
    pdt=1
    i=1
    while(pdt<n):
        pdt=(i*(i+1))
        i=i+1
    if(pdt==n):
        return(True)
    else:
        return(False)             

#main
x=int(input("Enter a no"))
a=chkspcl(x)
if(a==True):
    print("Special no")
else:
    print("NA")"""







  
    


































