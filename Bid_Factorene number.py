x=int(input("Enter a number"))
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
    print("Special no.")
else:
    print("Not a special no.")
