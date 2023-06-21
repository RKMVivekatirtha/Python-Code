x=int(input("Enter a value"))
flag=0
i=2
while(i<=x//2):
    if(x%i==0):
        flag=1
        break
    i=i+1
if(flag==0):    
    print("Prime")
else:
    print("NonPrime")
        


