#Types of sets
set1=set()#Empty set
set2={"Ram","Shyam"} #Set of string
set3={10,30,45,80,10} #Integer set
set4={10.2,20.5,30.7} #Set of real numbers
print("Set 1 = ",set1)
print("Set 2 = ",set2)
print("Set 3 = ",set3)
print("Set 4 = ",set4)
#Update function
set3={10,30,45,80,10} #Integer set
set4={25,35,80,30}
set3.update(set4)
print("First Set 3 = ",set3)
set3.update(set3)
print("Second Set 3 = ",set3)
#Implimentation of list in a set
list1=[10,20,30,40,50,"a","p"]
set5=set(list1)
print(set5)
#Implimentation of touple in a set
touple1=(10,20,30,40,50,"a","p",("g",30))
set6=set(touple1)
print(set6)
str1="teacher"
str2="cheater"
set7=set(str1)
set8=set(str2)
print(set7)
print(set8)
#Frozen set
set1={10,20,30,40}
xset1=frozenset() #Empty frozen set
xset2=frozenset(set1)
xset3=frozenset(list1)
print("xset1= ",xset1)
print("xset2= ",xset2)
print("xset3= ",xset3)
#Add and remove function
set1.add(100)
print(set1)
set1.remove(10)
print(set1)
#Union & Intersection
set1={10,20,30,40,50}
print(set1)
set2={10,12,40,45,23}
print(set2)
print("Union of sets: ",set1.union(set2))
print("Using logical 'or' doing the union: ",set1|set2)
print("Intersection os sets: ",set1.intersection(set2))
print("Using logical 'and' doing the intersection: ",set1&set2)
#Discard function and clear
set1.discard(30)
print(set1)
set1.discard(30) #No error if the number is not present in the set
print(set1)
set1.clear()
print("New set1 is: ",set1)
#Subset and superset
set1={10,20,30,40,50}
set2={7,10,25,70}
set3={20,30}
print(set3.issubset(set1))
print(set1.issuperset(set3))
#Intertion_update and Difference_Update
set1={10,20,30,40,50}
set2={7,10,25,70,50}
set1.intersection_update(set2)
print(set1)
set1={10,20,30,40,50}
set2={7,10,25,70,50}
set2.difference_update(set1)
print(set2)
# isdisjoint - checking the repetation of values in 2 sets
set1={10,20,30,40,50}
set2={7,10,25,70,50}
print(set2.isdisjoint(set1))
set1={10,20,30,40,50}
set2={7,25,70}
print(set2.isdisjoint(set1))
#Max, Min, Sum, Sort
set1={10,20,30,40,50,26,57,34}
print(max(set1))
print(min(set1))
print(sum(set1))
print(sorted(set1))
# Symmetric Difference - Present not in both, but print non-similer elements
set1={10,20,30,40,50}
set2={10,15,25,40,55}
print(set1.symmetric_difference(set2))