# this is a comment
print("hi bro." , end = " ")
print("printing on the same line")

print(557)
print(557+3)

"""
this is
a multiline
comment
"""

x = 5
y = 7
z = "Alex"
print(x)
print(y)
print(z)

x = int(8)
y = str(5)
z= float(3.5)
print(x)
print(y)
print(z)

print(type(x))

myName = "pooria"
firstPlayer, secondPlayer, Thirdplayer = "ali","reza", 55
print(firstPlayer)
print(secondPlayer)
print(Thirdplayer)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# use a variable inside a function and make it global
def myfunc():
  global x
  x = "fantastic"

myfunc()

myList = ["ali", "reza", "mmd"]
myTuple = (1, 3 ,5)

# convert number types to each other
x = 5
a = float(x) # 5.0
b = str(x) # "5"

y = 7.6
a = int(y) # 7
b = float(y) # 7.6
