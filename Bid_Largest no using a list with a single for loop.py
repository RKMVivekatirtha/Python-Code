x=[]
m=int(input("How many no.s do you want to enter?"))
print("Enter",m,"Values")
a=int(input())
x.append(a)
lg=x[0]
for i in range(1,m):
    a=int(input())
    x.append(a)
    if(x[i]>lg):
        lg=x[i]
    
print("Largest value is",lg)
