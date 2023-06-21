x=[]
flag=False
m=int(input("How many no.s do you want to enter?"))
print("Enter",m,"Values")
for i in range(0,m):
    a=int(input())
    x.append(a)
no=int(input("Enter a value to be searched for"))
for i in range(0,m):
    if(x[i]==no):
        flag=True
        break
if(flag==True):    
        print("It exists at index ",i," in the list")
else:
        print("Does not exist")


