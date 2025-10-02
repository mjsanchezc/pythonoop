# Object Oriented Programming in Python: Classes and Methods

class Dog:
  def __init__(self, name, age): # This method is always executed when a reference of the class is created
    self.name = name        # This attribute is stored permanently inside the class for each reference created
    self.age = age
    print(name)

  def add_one(self, x):
    return x + 1

  def bark(self):
    print("bark")

  def get_name(self):
    return self.name
  
  def get_age(self):
    return self.age
  
  def set_name(self, name):
    self.name = name
    return self.name
  
  def set_age(self, age):
    self.age = age
    return self.age

d = Dog("Tim", 6)              # Tim
d2 = Dog("Bill", 2)            # Bill
d.bark()                       # bark
print(d.add_one(5))            # 6s
print(type(d))                 # <class '__main__.Dog'>

print(d.get_age())             # 6
print(d2.get_name())           # Bill

print(d.set_age(5))            # 5
print(d2.set_name("Max"))      # Max

