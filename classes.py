# Object Oriented Programming in Python: Classes and Methods

class Dog:
  def __init__(self, name): # This method is always executed when a reference of the class is created
    self.name = name        # This attribute is stored permanently inside the class for each reference created
    print(name)

  def add_one(self, x):
    return x + 1

  def bark(self):
    print("bark")

d = Dog("Tim")              # Tim
d2 = Dog("Bill")            # Bill
d.bark()                    # bark
print(d.add_one(5))         # 6s
print(type(d))              # <class '__main__.Dog'>

