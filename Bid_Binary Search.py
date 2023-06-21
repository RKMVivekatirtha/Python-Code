x=[]
flag=0
sz=int(input("How many no.s do you want to print?"))
print("Enter",sz,"values")
for i in range(0,sz):
    a=int(input())
    x.append(a)
print("The list is",x) 
beg=0
end=sz-1
no=int(input("Enter a value to be searched for"))
while(beg<=end):
    mid=(beg+end)//2
    if(x[mid]==no):
        flag=1
        break
    elif(x[mid]>no):
        end=mid-1
    else:
        beg=mid+1
if(flag==1):
    print("The no exists at the",mid,"index of the list")
else:
    print("The no does not exist in the list")
