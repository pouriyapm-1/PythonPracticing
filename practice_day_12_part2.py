# PIP
# PIP is a package manager for Python packages, or modules if you like.
# A package contains all the files you need for a module.
# Modules are Python code libraries you can include in your project.

# install packages: in Terminal --> pip install ...
# source: https://pypi.org/
import camelcase
c = camelcase.CamelCase()
txt = "hello world"

print(c.hump(txt))

# Unistall a package: pip unistall ...
# list all the packages installed on your system: pip list

# Try...Except
# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.
try:
  print(x)
except:
  print("An exception occurred")

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

# In this example, the try block does not generate any error:
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# To throw (or raise) an exception, use the raise keyword.
# Example
# Raise an error and stop the program if x is lower than 0:
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

#You can define what kind of error to raise, and the text to print to the user.
# Raise a TypeError if x is not an integer:

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")

# چندتا Error مهم که خوبه بشناسی:
# ValueError → مقدار نامعتبر
# TypeError → نوع داده اشتباه
# ZeroDivisionError → تقسیم بر صفر
# IndexError → index خارج از محدوده
# KeyError → key وجود نداره
# FileNotFoundError → فایل پیدا نشده
# NameError → متغیر تعریف نشده

# None
# None is a special constant in Python that represents the absence of a value.
# Its data type is NoneType, and None is the only instance of a NoneType object.

# Variables can be assigned None to indicate "no value" or "not set".
x = None
print(x)
print(type(x))

# Use the identity operator is for comparisons with None:
# نمیگیم x == None
# میگیم x is None
result = None
if result is None:
  print("No result yet")
else:
  print("Result is ready")

# None evaluates to False in a boolean context.  # از نظر بولین بخوایم بگیم، نان فالس هست

# User Input ...


# Virtual Environment

# python -m venv venv → ساخت محیط مجازی
# .\venv\Scripts\Activate.ps1 → فعال کردنش
# (venv) اول Terminal → یعنی الان داخل محیط مجازی هستی
# deactivate → خارج شدن از محیط

#ین دوتا رو یادت باشه:

# فعال کردن:
# .\venv\Scripts\Activate.ps1

# غیرفعال کردن:
# deactivate