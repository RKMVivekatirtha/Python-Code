#HAPPY NUMBER

def addsum(x):
    c=x
    sum=0
    while(c>0):
        a=c%10
        sum=sum+(a*a)
        c=c//10
    return(sum)
    

#main
x=int(input("Enter a no."))
a=x
while(a>0):
    a=addsum(x)
    print("Result is ",a)
    x=a
    if(a<10):
        break
print("a= ",a)
if(a==1):
    print("Happy Number")
else:
    print("Not a Happy number")
