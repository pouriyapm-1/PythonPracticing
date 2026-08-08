# Sets  (Unordered, Unchangeable, Unindexed but we can add and remove items)
newSet = {"Orange", "Grey", "White"}
print(newSet)
print(type(newSet))
print(len(newSet))
# We can also use set constructor to create sets: set()
# .add() to add items     .update() to add items from another iterable
newSet.add("Blue")
list1 = ["mother", "brother"]
newSet.update(list1)
print(newSet)
# .remove() & .discard() to remove items.    .pop() will remove a random item.
# .clear() & del
# There are several ways to join two or more sets in Python.
# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)
# u can use | instead of .union() and .update()        and use & for .intersection()

# The .intersection_update() method will also keep ONLY the duplicates,but it will change the original set instead of returning a new set.
# .difference() will return a new set that will contain only the items from the first set that are not present in the other set.
# .difference_update() ...
# The .symmetric_difference() method will keep only the elements that are NOT present in both sets.
# .symmetric_difference_update() ...

# frozenset is an immutable version of a set.
# Like sets, it contains unique, unordered, unchangeable elements.
# Unlike sets, elements cannot be added or removed from a frozenset.


# Dictionaries
# ordered*, changeable and do not allow duplicates.
mydict = {"name":"reza",
          "age" : "20",
          "favcolor" : "blue"}
print(mydict)
x = mydict["age"] # or use the method: mydict.get("age")
print(x)

# .keys() method will return a list of all the keys in the dictionary.
print(mydict.keys())

# .values() method will return a list of all the values in the dictionary.
print(mydict.values())

# .items() method will return each item in a dictionary, as tuples in a list.
print(mydict.items())

if "favcolor" in mydict:
  print("Yes! favcolor is in the dictionary")

# changing and adding items (2 ways)
mydict["favcolor"] = "red"
mydict.update({"phone number": 94324})
print(mydict)

# .pop() method removes the item with the specified key name: mydict.pop("model")
# .popitem() method removes the last inserted item
# remove items: del mydict["model"]    delete the dictionary: del mydict
# mydict.clear()

for x in mydict:
  print(x)           # returns all the keys
# for x in mydict.keys():           # another way
#   print(x)

for x in mydict:
  print(mydict[x])   # returns all the values
# for x, y in mydict.items():       # another way
#   print(x, y)
 
# to copy a dictionary (2 ways)

# .copy()                     
# dict1 = mydict.copy()

# .dict()
# dict1 = dict(mydict)

# Nested dictionaries: A dictionary can contain dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child1"]["name"])
