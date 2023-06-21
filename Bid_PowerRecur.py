def power(x,n):
    if(n==1):
        return(x)
    else:
        return(x*power(x,(n-1)))

#main
x=int(input("enter base and power"))
y=int(input())
a=power(x,y)
print("Result is ",a)
               
