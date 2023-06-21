"""def chkprime(x):
    for i in range(2,(x//2+1)):
                   if(x%i==0):
                       return(0)
    return(1)
#main
a=int(input("Enter a no."))
x=chkprime(a)
if(x==0):
    print("Cmpst")
else:
    print("Prime")"""






def chkprime(x):
    for i in range(2,(x//2+1)):
        if(x%i==0):
            return(0)
    return(1)

x=int(input("enter two values"))
y=int(input())
lg=max(x,y)
sm=min(x,y)
count=0
print("Prime nos between ",x," and ",y," are")
for x in range(sm,lg+1):
    if(chkprime(x)==1):
        print(x,end="  ")
        count=1
if(count==0):
    print("not possible")
