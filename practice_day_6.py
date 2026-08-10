# Functions
# A function is a block of code which only runs when it is called.
# A function can return data as a result.
# A function helps avoiding code repetition.
def my_function():
  print("Hello from a function")

my_function()

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

def get_greeting():
  return "Hello from a function"

print(get_greeting())

# If a function doesn't have a return statement, it returns None by default.
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument

# By default, a function must be called with the correct number of arguments.
# If your function expects 2 arguments, you must call it with exactly 2 arguments.

# You can assign default values to parameters. If the function is called without an argument, it uses the default value:
def my_function(name = "friend"): # "friend" is the default value
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

# Keyword arguments
# You can send arguments with the key = value syntax.
# This way, with keyword arguments, the order of the arguments does not matter.
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")

# You can mix positional and keyword arguments in a function call.
# However, positional arguments must come before keyword arguments:

def pet_info(animal,name,age):
  print("i have a ", animal, "his name is ",name, "he is ",age, "years old.")

pet_info("cat", age="4", name="tuffle")

# You can send any data type as an argument to a function (string, number, list, dictionary, etc.).

def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

# You can specify that a function can have ONLY positional arguments.
# To specify positional-only arguments, add , / after the arguments:

def my_function(name, /):
  print("Hello", name)

my_function("Emil")

# To specify that a function can have only keyword arguments, add *, before the arguments:
def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")

# Combining Positional-Only and Keyword-Only
# You can combine both argument types in the same function.
# Arguments before / are positional-only, and arguments after * are keyword-only:

def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)

# Arbitrary Arguments - *args
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# The *args parameter allows a function to accept any number of positional arguments.
# Inside the function, args becomes a tuple containing all the passed arguments:

def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")

# You can combine regular parameters with *args.
# Regular parameters must come before *args:
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")

# یک تابع که جمع هر تعداد مقدار ورودی را محاسبه می کند
def sum_calculate(*numbers):
  total = 0
  for i in numbers:
    total += i
  return total

print("total addition:",sum_calculate(10,20,60,20))

# یک تابع که بین هر تعداد عدد وارد شده، ماکزیمم را پیدا می کند
def max_finder(*numbers):
  maximum = numbers[0]
  for i in numbers:
    if i > maximum:
      maximum = i
  return maximum
print(max_finder(4,7,8,23,42))

# Arbitrary Keyword Arguments - **kwargs
# If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.
# This way, the function will receive a dictionary of arguments and can access the items accordingly:
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# You can combine regular parameters with **kwargs.
# Regular parameters must come before **kwargs

# You can use both *args and **kwargs in the same function.

# The order must be:
#   regular parameters
#   *args
#   **kwargs

# Unpacking Lists with *
# Using * to unpack a list into arguments:

def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)

# If you operate with the same variable name inside and outside of a function,
# Python will treat them as two separate variables, one available
# in the global scope (outside the function) and one available in the local scope (inside the function):
x = 300

def myfunc():
  x = 200
  print(x)

myfunc() # prints 200
print(x) # prints 300

# If you use the global keyword, the variable belongs to the global scope:
def myfunc():
  global x
  x = 300

myfunc()

print(x)

# Also, use the global keyword if you want to make a change to a global variable inside a function.
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)

#The nonlocal keyword is used to work with variables inside nested functions.
# The nonlocal keyword makes the variable belong to the outer function.

def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

#Python follows the LEGB rule when looking up variable names, and searches for them in this order:

# Local - Inside the current function
# Enclosing - Inside enclosing functions (from inner to outer)
# Global - At the top level of the module
# Built-in - In Python's built-in namespace

# Decorators
#یعنی یک تابع رو می‌گیری و بدون تغییر دادن کد خودش، رفتارش رو با یک تابع دیگه تغییر/گسترش میدی.
# Decorators let you add extra behavior to a function, without changing the function's code.
# A decorator is a function that takes another function as input and returns a new function.
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())
