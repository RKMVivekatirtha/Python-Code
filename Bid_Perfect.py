x=int(input("Enter a value"))
sum=0
for i in range(1,x):
    if(x%i==0):
        sum=sum+i
if(sum==x):
    print("Perfect")
else:
    print("Non perfect")
