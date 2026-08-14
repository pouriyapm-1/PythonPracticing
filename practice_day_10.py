# Ranges
# range(start,stop,step)
# x = range(10) --> 0-9
# we can convert ranges to lists to display them : list(range(2,10,3))
# Extract a subsequence from a range:
r = range(10)
print(r[2])
print(r[:3])
# Ranges support membership testing with the in operator.
r = range(0, 10, 2)
print(6 in r) # True
print(7 in r) # False
# we can use len() on ranges
print(len(r))

# Python Arrays
# Python does not have built-in support for Arrays, but Python Lists can be used instead.
# ... like lists

# Iterators
# An iterator is an object that contains a countable number of values.
# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
# All these objects and strings have a iter() method which is used to get an iterator
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# The for loop actually creates an iterator object and executes the next() method for each loop.
# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
# The __next__() method also allows you to do operations, and must return the next item in the sequence.
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

# Stop after 20 iterations:

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration



# Modules: A file containing a set of functions you want to include in your application.
# To create a module just save the code you want in a file with the file extension .py:
# Save this code in a file named mymodule.py
def greeting(name):
  print("Hello, " + name)

# Use the module you created:
import mymodule

mymodule.greeting("Jonathan")

# a module also can contain variables
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

# use it
import mymodule

a = mymodule.person1["age"]
print(a)

# Rename module by the as keyword دادن یک نام مستعار به ماژول
import mymodule as mx

a = mx.person1["age"]
print(a)

#There are several built-in modules in Python, which you can import whenever you like.
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
# List all the defined names belonging to the platform module:

import platform

x = dir(platform)
print(x)

# You can choose to import only parts from a module,
# by using the from keyword.

# Import only the person1 dictionary from the module:

from mymodule import person1

print (person1["age"])

# When importing using the from keyword, do not use the module 
# name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]



# Python Datetime
# datetime is a module
# Import the datetime module and display the current date:

import datetime

x = datetime.datetime.now()
print(x)

# create a date by datetime()
# The datetime() class requires three parameters to create a date: year, month, day.

import datetime
x = datetime.datetime(2020,11,18)
print(x)

#The datetime() class also takes parameters for time and
# timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).

# strftime()   : a method for formatting date objects into readable strings.
# takes one parameter
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

# all the legal format codes: Datetime page in w3schools.com



# Math
# Built-in Math Functions
# min() and max()  : can be used to find the lowest or highest value in an iterable:
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

# abs() pow(x, y) توان و قدر مطلق

# math module: import math
# math.sqrt() ریشه یک عدد
import math
x = math.sqrt(81)
print(x)

# math.ceil() & math.floor() 
# گرد کردن عدد به عدد صحیح بعدی یا قبلی

print(math.ceil(1.4))    # 2
print(math.floor(1.4))   # 1

# math.pi عدد پی
print(math.pi)

# and other methods in math module...