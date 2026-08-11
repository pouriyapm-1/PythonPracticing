# Decoration 
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunc():
  return "hello world! i'm here."

print(myfunc())

# Functions with arguments can also be decorated:
def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))
# --------------------------------
def changecase(func):
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))

# Multiple Decorators
# You can use multiple decorators on one function.
# This is done by placing the decorator calls on top of each other.
# Decorators are called in the reverse order, starting with the one closest to the function. 

# Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes.
# Normally, a function's name can be returned with the __name__ attribute
# But, when a function is decorated, the metadata of the original function is lost.
# To fix this, Python has a built-in function called functools.wraps that can be used to preserve the original function's name and docstring.

import functools

def changecase(func):
  @functools.wraps(func)
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

# Lambda Functions
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# lambda arguments : expression
x = lambda a : a + 10
print(x(5))
# کاربرد تابع لمبدا
def myfunc(n):
  return lambda a: a * n

mydoubler = myfunc(2)
print(mydoubler(6))

# Lambda with Built-in Functions
# Lambda functions are commonly used with built-in functions like map(), filter(), and sorted().

# The map() function applies a function to every item in an iterable:
mynumbers = [5, 6, 8, 9]
doubled = list(map(lambda x: x*2, mynumbers))
print(doubled)

# Using Lambda with filter()
# The filter() function creates a list of items for which a function returns True:
# Filter out odd numbers from a list:
numbers = [1,2,3,5,6,9,12]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

# Using Lambda with sorted()
# The sorted() function can use a lambda as a key for custom sorting:

# Sort a list of tuples by the second element:
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key = lambda x: x[1])
print(sorted_students)