#1
"""for i in range(1,5):
    for j in range(1,4):
        print("*",end=" ")
    print()"""







#2
"""x=int(input("Enter a number"))
for i in range(1,x+1):
      for j in range(1,i+1):
          print("*",end=" ")
      print()"""
      
#OR
        
        
"""x=int(input("Enter a number"))
for i in range(1,x+1):
      print(i*"*")"""
    
        

#3
"""x=int(input("Enter a number"))
for i in range(1,x+1):
      for j in range(1,i+1):
          print(j,end=" ")
      print()"""




#4
"""x=int(input("Enter number of row"))
for i in range(1,x+1):
    for j in range(1,i+1):
        if(j%2==0):
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()"""






"""x=int(input("Enter number of row"))
for i in range(1,x+1):
    for j in range(1,i+1):
        print(j%2,end=" ")
    print()"""



#5
"""x=int(input("Enter a number"))
for i in range(1,x+1):
    c=x
    for j in range(1,i+1):
        print(c,end=" ")
        c=c-1
    print()"""



#6
"""x=int(input("Enter a number"))
for i in range(x,0,-1):
      for j in range(i,0,-1):
          print(j,end=" ")
      print()"""



#7
"""x=int(input("Enter a number"))
for i in range(x,0,-1):
    c=x
    for j in range(i,0,-1):
        print(c,end=" ")
        c=c-1
    print()"""





#8
"""x=int(input("Enter no of row"))
for i in range(x,0,-1):
    print(i*"*",end=" ")
    print()"""




#10
"""x=int(input("Enter no of row"))
c=1
for i in range(x,0,-1):
    x=c
    for j in range(i,0,-1):
        print(x,end=" ")
    c=c+1
    print()"""







#11
"""x=5
for i in range(1,x+1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()"""




#12
"""x=5
for i in range(1,x+1):
    for j in range(i,x+1):
        print(j,end=" ")
    print()"""
