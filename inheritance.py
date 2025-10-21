# Object Oriented Programming in Python: Inheritance

class Pet:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def show(self):
    print(f"I am {self.name} and I am {self.age} years old")

class Cat(Pet):
  def __init__(self, name, age, color):
    super().__init__(name, age)
    self.color = color

  def speak(self):
    print("Meow")

  def show(self):
    print(f"I am {self.name}, I am {self.age} years old, and I am {self.color}")

class Dog(Pet):
  def speak(self):
    print("Woof")

p = Pet("Tim", 1)
p.show()

c = Cat("Tony", 5, "Tabby White")
c.show()

d = Dog("Bisky", 3)
d.speak()