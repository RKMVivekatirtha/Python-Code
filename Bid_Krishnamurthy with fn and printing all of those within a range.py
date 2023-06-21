#W.A._P. to print all Krishnamury nos within a given range    
    
    
    
"""def chkkrishnamurthy(x):
    c=x
    sum=0
    while(c>0):
        n=c%10
        pdt=1
        for i in range(1,n+1):
            pdt=pdt*i
        sum=sum+pdt
        c=c//10
    if(sum==x):
        return(True)
    else:
        return(False)
#main()
x=int(input("Enter a no."))
a=chkkrishnamurthy(x)
if(a==True):
    print("Krishnamurthy")
else:
    print("Not a Krishnamurthy")"""



def chkkrishnamurthy(x):
    c=x
    sum=0
    while(c>0):
        n=c%10
        pdt=1
        for i in range(1,n+1):
            pdt=pdt*i
        sum=sum+pdt
        c=c//10
    if(sum==x):
        return(True)
    else:
        return(False)
#main()
x=int(input("Enter two values"))
y=int(input())
lg=max(x,y)
sm=min(x,y)
for i in range(lg,sm-1,-1):
    a=chkkrishnamurthy(i)
    if(a==True):
        print(i,end="  ")
       























    
