# You can assign a multiline string to a variable by using three quotes
a = """hello i'm
pouriyapm, nice to meet
you"""
print(a)

# Access to charachters of a string
print(a[0])

# Loop through the strings
for x in "banana":
  print(x)

# Length of a string
b = "Apple"
print(len(b))

# to check if a word or charachter is present in a string or not
# (returns True or False)
txt = "The best things in life are free!"
print("life" in txt)
print("glow" not in txt)

# Slicing in strings
z = "Hello, World!"
print(z[2:6]) # llo,
print(z[:4]) # slices from the start
print(z[2:]) # slices to the end
print(z[-5:-2]) # starts from the end of string

# Methods
m = "Hello world, i'm here"
print(m.upper()) # .upper()
print(m.lower()) # .lower()
                 # .strip()    removes any whitespaces from start and end.
print(m.replace("o","x"))
print(m.split(",")) #splits the text with the specified sign

a = "Hello"
b = "World"
c = a + " " + b         
print(c)

# Combine strings and numbers (using f-string) / Formatting
age = 43
print(f"ali is {age} years old")

price = 50
print(f"the price is {price:.2f} dollars") #.2f یعنی با دو رقم اعشار
print(f"the price is {price * 4} dollars") # u can use operations in it

# Other methods for strings

# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning

# Booleans
print(10 > 8) #returns True
x = "Hello"
print(bool(x))
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.

num = 6

if num>5:
  print("WEEKEND!")
else:
  print("WORKDAY")

print(x)

#Operators
#   + - * ** / // %  (Arithmetic)
# = += -= *= **= /= //= %= :=  (Assignment)
# == != > < >= <=  (Comparison)
# and or not (Logical)
# is (if both variables point to the same object, True), is not (Identify)
# in, not in (uses to check if a value is in a sequence or not) (Membership)
# & | ^ ~ << >> (Bitwise)

# Lists
firstlist = ["ali","reza","nima"]
print(firstlist)

print(len(firstlist))  # use len() to determine list length

#List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# another way to create a list
k = ("blue", "pink", "red")
k = list(k)
print(list(k))

print(k[1:2]) # like the strings...
if "blue" in k:
  print("Yes, we have blue!")

# change a item in list
k[1] = "orange"
print(k[1])
# or we can change a range of items
# k[1,3]  = ["blueberry", "banana"]

# .insert( , ) to add a new item with specified place
k.insert(0,"brown")
print(k)

# .append() to add new items at the end of the list.
# To append elements from another list to the current list, use the .extend() method.

list1 = ["99","88","77"]
list1.append("66")
print(list1)

list2 = ["4", "5", "6"]
list1.extend(list2)
print(list1)
# With The extend() method, you can add any iterable object (tuples, sets, dictionaries etc.).

# .remove()
list1.remove("6")
print(list1)

# .pop() removes the specified index (if u don't specify, removes the last item)
list1.pop(0) 

#del removes the specified index
del list1[0]
# del list1       # deletes the list completely

list1.clear()     # empties the list

# Loop through a list with for
listt = [5, 7, 9, 11]
for x in listt:
  print(x)

for i in range(len(listt)):
  print(listt[i])  

# with while
z = 0
while z < len(listt):
  print(listt[z])
  z += 1

# list comprehension
# newlist = [expression for item in iterable if condition == True]

newlist = [x for x in range(10) if x < 5]
print(newlist)

newlist = [x.upper() for x in ...] # میشه expression رو دستکاری کرد
