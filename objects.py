# Object Oriented Programming in Python

def hello():
  print("hello")

x = 1
print(type(hello))      # <class 'function'>
print(type("hello"))    # <class 'str'>
print(type(x))          # <class 'int'>

# Common errors

y = 1
z = "hello"

# print(y + z)          # TypeError: unsupported operand type(s) for +: 'int' and 'str'

###

string = "hello"
x = 1

print(string.upper())   # "HELLO"
# print(x.upper())      # AttributeError: 'int' object has no attribute 'upper'
