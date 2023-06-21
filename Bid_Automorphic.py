x=int(input("Enter a value"))
dgtcnt=0
b=x
while(b>0):
    dgtcnt=dgtcnt+1
    b=b//10
y=pow(x,2)
a=pow(10,dgtcnt)
if(y%a==x):
    print("Automorphic")
else:
    print("Non automorphic")
