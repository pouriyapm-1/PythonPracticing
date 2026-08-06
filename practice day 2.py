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
