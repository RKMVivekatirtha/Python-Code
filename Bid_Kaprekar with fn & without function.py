"""x=int(input("Enter a no."))
dgtcnt=0
a=x
while(a>0):
    dgtcnt=dgtcnt+1
    a=a//10
b=pow(10,dgtcnt)
sq=x*x
m=sq%b
n=sq//b
if(m+n==x):
    print("Kaprekar")
else:
    print("Not valid")"""

def chkkaprekar(x):
    dgtcnt=0
    a=x
    while(a>0):
        dgtcnt=dgtcnt+1
        a=a//10
    b=pow(10,dgtcnt)
    sq=x*x
    m=sq%b
    n=sq//b
    if((m+n)==x):
        return(True)
    else:
        return(False)

#main()
x=int(input("Enter a no."))
a=chkkaprekar(x)
if(a==True):
    print("Kaprekar")
else:
    print("Not a Kaprekar number")
