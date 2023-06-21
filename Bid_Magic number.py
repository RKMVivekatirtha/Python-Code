def addsum(n):
    sum=0
    while(n>0):
        sum=sum+n%10
        n=n//10
    return(sum)

x=int(input("Enter a no"))
c=x
while(c>9):
    a=addsum(c)
    c=a
if(c==1):
    print("Happy number")
else:
    print("Invalid")
