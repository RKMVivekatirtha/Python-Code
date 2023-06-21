x=int(input("Enter a number"))
y=x
fl=0
while(y>0):
   y=y%10
   if(y==0):
      fl=1
      break
   y=y//10 
if(fl==1):
    print(x,"is Duck no.")
else:
    print("Non duck no")

