x=[]
sz=int(input("How many no do you want to input?"))
print("Enter",sz,"values")
for i in range(0,sz):
    a=int(input())
    x.append(a)
print("The list is",x)
p=0
for i in range(0,sz):
    flag=0
    p=p+1
    for j in range(0,sz-i-1):
        if(x[j]>x[j+1]):
            x[j],x[j+1]=x[j+1],x[j]
            flag=1
    if(flag==0):
        break
    print("\n After",(i+1),"pass, the list is,",x)
print("Total pass is",p)
print("The sorted list is",x)
    
