def addsum(n):
    sum=0
    while(n>0):
        sum=sum+n%10
        n=n//10
    return(sum)    


#main()
num=int(input("Enter a number"))
sum=0
no=num

while(no>1):
    for i in range(2,no+1):
        if(no%i==0):
            sum=sum+addsum(i)
            break
    no=no//i
if(addsum(num)==sum):
    print("Smith number")
else:
    print("Not a smith number")
