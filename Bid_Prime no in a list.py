def chkprime(x):
    for i in range(2,((x//2)+1)):
        if(x%i==0):
            return(0)
    return(1)

x=[]
sz=int(input("How many no do you want to input?"))
print("Enter",sz,"values")
for i in range(0,sz):
    a=int(input())
    x.append(a)
print("The list is",x)
fl=0
for i in range(0,sz):
    a=chkprime(x[i])
    if(a==1):
        print("Prime number is",x[i])
        fl=1
if(fl==0):    
        print("There is no prime number present in the list")
