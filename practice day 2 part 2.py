list1 = ["mouse", "keyboard", "headphones", "desk"]
# add: insert append extend 
# remove: remove pop del clear

newlist = [x for x in list1 if x != "desk"]
print(newlist)

# Sort alphanumerically
list1.sort()
print(list1)
# list1.sort(reverse = True)  سورت کردن از زیاد به کم Descending

# Customize Sort Function
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key= myfunc)
print(thislist)

# By default the sort() method is case sensitive
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist.reverse() # reverse the order

mylist = thislist.copy()  # copy the list. other ways:
# mylist = list(thislist), mylist = thislist[:]

# Join lists ways
# .extend()    list3 = list1 + list2

# .count()    list.count(3)  میشماره که چنتا 3 داره لیست

#Tuples  (unchangeable, u cannot add or remove items)

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#To create a tuple with only one item, you have to add a comma after the item,
# otherwise Python will not recognize it as a tuple.

myTuple = ("rain",)
print(type(myTuple))
print(myTuple[0]) #indexing is the same as the lists

#Once a tuple is created, you cannot change its values. 
#Tuples are unchangeable, or immutable as it also is called.
#But there is a workaround.
#You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# unpacking tuples way 1
# fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)

# using asterisks ---------------------------------------

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, yellow, *red) = fruits
# print(green)
# print(yellow)
# print(red)

# Join tuples
# tuple3 = tuple2 +_tuple1

# Tuple Methods .count() .index()