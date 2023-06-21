'''l=int(input("Enter the starting number of the range"))
m=int(input("Enter the ending number of the range"))
for x in range(l,m+1):
    c=x
    count=0
    while(c>0):
        c=c//10
        count=count+1
    a=x
    sum=0
    while(a>0):
        b=a%10
        sum=sum+pow(b,count)
        a=a//10
    if(sum==x):
        print(x)'''
   




'''x=int(input("Enter two values"))
y=int(input())
lg=max(x,y)
sm=min(x,y)
for x in range(sm,lg+1):
    c=x
    count=0
    while(c>0):
        c=c//10
        count=count+1
    a=x
    sum=0
    while(a>0):
        b=a%10
        sum=sum+pow(b,count)
        a=a//10
    if(sum==x):
        print(x)'''
   
