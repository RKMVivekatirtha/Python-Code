class car():
  def __init__(self,comp,yr):
    self.comp=comp
    self.yr=yr
  def display(self):
    print("Name of the company is: ",self.comp)
    print("Year of manufacturing is: ",self.yr)

a=input("Enter company's name: ")
b=input("Enter yr of manufacturing")
x=car(a,b)
x.display()

#Calculate the area of an area
class area():
  def __init__(self,len,br):
    self.len=len
    self.br=br
    self.ar=self.len*self.br
  def display(self):
    print("Area is: ",self.ar)

a=int(input("Enter length: "))
b=int(input("Enter breath: "))
x =area(a,b)
x.display()

#Calculate a number is automorphic or not
class AutoMorphic():
  def __init__(self,num):
    self.num = num

  def check (self):
    self.sq = self.num**2
    self.ln = len(str(self.num))
    self.div = 10**self.ln


    if self.sq%self.div == self.num:
      print(self.num, "It is an Automorphic number")
    else:
      print(self.num, "It not an Automorphic number")

num = int(input("Enter a number: "))
res = AutoMorphic(num)
res.check()