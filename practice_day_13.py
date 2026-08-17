# OOP (Object-Oriented Programming)
# Define a class:
class MyClass:
  x = 5

# Create an object:
p1 = MyClass()
print(p1.x)

# Delete an object:
del p1

# Multiple Objects
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

# Each object is independent and has its own copy of the class properties.

# class definitions cannot be empty (use pass if you want)
class Person:
  pass

# All classes have a built-in method called __init__(), which is always executed when the class is being initiated.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

# Using __init__() makes it easier to create objects with initial values:
# With __init__(), you can set initial values when creating the object:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 28)

print(p1.name)
print(p1.age)

# You can also set default values for parameters in the __init__() method:
class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)

# The __init__() method can have as many parameters as you need:
class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)

# فرمول ساده‌ای که فعلاً یادت بمونه:
# object.method()

class Dog:
  def __init__(self, name, age):
    self.name() = name
    self.age() = age
  def bark(self):              # یک متد
    print(self.name + "says Woof!")

d1 = Dog("Buddy", 3)    # یک شی

d1.bark()

# self parameter
# The self parameter is a reference to the current instance of the class.
# It is used to access properties and methods that belong to the class.
# The self parameter must be the first parameter of any method in the class.

#It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any method in the class:
class Person:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age

  def greet(abc):
    print("Hello, my name is " + abc.name)

p1 = Person("Emil", 36)
p1.greet()

#  While you can use a different name, it is strongly recommended to use self

# Access multiple properties using self:

class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()


class Person:
  def __init__(self, name, favcolor, favfood):
    self.name = name
    self.favcolor = favcolor
    self.favfood = favfood

  def message(self):
    print(f"Hooray! now we know {self.name} loves {self.favfood} and their favorite color is {self.favcolor}")

p1 = Person("reza","blue","pizza")
p1.message()

# u can call one method from another method using self:
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return "Hello, " + self.name

  def welcome(self):
    message = self.greet()
    print(message + "! Welcome to our website.")

p1 = Person("Tobias")
p1.welcome()

# Class Properties
# Properties are variables that belong to a class. They store data for each object created from the class.
class Person:
  def __init__(self, name, age):
    self.name = name  # <--- properties
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

# You can access object properties using dot notation:
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand)   # <--- access object properties using .
print(car1.model)

# You can modify the value of properties on objects:
# Change the age property:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Tobias", 25)
print(p1.age)

p1.age = 26 # <--- change the age property
print(p1.age)  # prints 26

# You can delete properties from objects using the del keyword
# Delete the age property:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 30)

del p1.age

print(p1.name) # This works
# print(p1.age) # This would cause an error (bcs it's deleted)

# Class Properties vs Object Properties
# Properties defined inside __init__() belong to each object (instance properties).
# Properties defined outside methods belong to the class itself (class properties) and are shared by all objects:
# Class property vs instance property:

class Person:
  species = "Human" # Class property

  def __init__(self, name):
    self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.species) # Human
print(p2.species) # Human

# When you modify a class property, it affects all objects:
# Change a class property:

class Person:
  lastname = ""

  def __init__(self, name):
    self.name = name

p1 = Person("Linus")
p2 = Person("Emil")

Person.lastname = "Refsnes"

print(p1.lastname) # Refsnes
print(p2.lastname) # Refsnes

# You can add new properties to existing objects:
class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Tobias")

p1.age = 25 # <--- adding new properties to object
p1.city = "Oslo" # <--- 

print(p1.name)
print(p1.age)
print(p1.city)

# * Adding properties this way only adds them to that specific object, not to all objects of the class.

# Code challenge so far:
class Student:
  def __init__(self, name, grade):
    self.name = name
    self.grade = grade
s1 = Student("Anna","A")
print(s1.grade) # prints A
s1.grade = "B"
print(s1.grade) # prints B


# Class Methods
# Methods are functions that belong to a class. They define the behavior of objects created from the class.

# Create a method in a class:
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil")
p1.greet()

# نکته: All methods must have self as the first parameter.

# Methods can accept parameters just like regular functions:
class Calculator:
  def add(self, a, b): # <---
    return a + b

  def multiply(self, a, b): # <---
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))

# Methods can access and modify object properties using self:
# A method that accesses object properties:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_info(self):
    return f"{self.name} is {self.age} years old" # <---

p1 = Person("Tobias", 28)
print(p1.get_info())

# Methods can modify the properties of an object:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1 # <---
    print(f"Happy birthday! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()

# __str__()   : a special method that controls what is returned when the object is printed:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):    # <---
    return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1)

# A class can have multiple methods that work together:
class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()

# You can delete methods from a class using the del keyword:
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello!")

p1 = Person("Emil")

del Person.greet

p1.greet() # This will cause an error

# w3schools code challenge
class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  def area(self):
    return self.width * self.height
r1 = Rectangle(5,3)
print(r1.area())

# Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# Creating a child class : To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:
# Example:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):  # Now the Student class has the same properties and methods as the Person class.
  pass

x = Student("Mike","Olsen")
x.printname()

# Add the __init__() Function
# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

# super() # این هم باعث میشه کلاس فرزند، تمام متد ها و ویژگیهای والد رو به ارث ببره
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

# add properties
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)

# add methods
# add a method called welcome
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.
# اگه نام متد، مشابه نام یکی از توابع کلاس والد باشد، ارث بری متد والد لغو می شود
# Code Challenge: (Solved)
class Animal:
  def __init__(self, name):
    self.name = name
  def speak(self):
    print(self.name)

class Dog(Animal):
  pass

d1 = Dog("Rex")  
d1.speak()