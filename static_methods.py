# Object Oriented Programming in Python: Static Methods

class Math:

  @staticmethod
  def add5(x):
    return x + 5
  
  @staticmethod
  def pr():
    print("ran")
  
print(Math.add5(3))
Math.pr()