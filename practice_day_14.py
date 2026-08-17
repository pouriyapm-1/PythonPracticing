# Polymorphism چندریختی
# methods/functions/operators with the same name that can be executed on many objects or classes.

# functions example: len() function can be used on different objects
# on strings
x = "Hello World!"
print(len(x))

# on tuples
mytuple = ("apple", "banana", "cherry")
print(len(mytuple))

# on dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict))

# Polymorphism is often used in Class methods,
# where we can have multiple classes with the same method name.
# For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()

# If we use the example above and make a parent class called Vehicle, and make Car, Boat, Plane child classes of Vehicle, the child classes inherits the Vehicle methods, but can override them:
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()

# Child classes inherits the properties and methods from the parent class.
# In the example above you can see that the Car class is empty, but it inherits brand, model, and move() from Vehicle.
# The Boat and Plane classes also inherit brand, model, and move() from Vehicle, but they both override the move() method.
# Because of polymorphism we can execute the same method for all classes.


# Encapsulation
# Encapsulation is about protecting data inside a class.
# It means keeping data (properties) and methods together in a class, while controlling how the data can be accessed from outside the class.
# This prevents accidental changes to your data and hides the internal details of how your class works.

# Private properties: you can make properties private by
# using a double underscore __ prefix:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Private property

p1 = Person("Emil", 25)
print(p1.name)
print(p1.__age) # This will cause an error

# Private properties cannot be accessed directly from outside the class.
# To access a private property, you can create a getter method:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

p1 = Person("Tobias", 25)
print(p1.get_age())

#To modify a private property, you can create a setter method.
#The setter method can also validate the value before setting it:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age
  def get_age(self):
    return self.__age
  def set_age(self, age): # <---
    if age > 0:
      self.__age = age
    else:
      print("Age most be a positive number.")

p1 = Person("Joey", 22)
print(p1.get_age())
p1.set_age(26) # <---
print(p1.get_age())

# Encapsulation provides several benefits:

# Data Protection: Prevents accidental modification of data
# Validation: You can validate data before setting it
# Flexibility: Internal implementation can change without affecting external code
# Control: You have full control over how data is accessed and modified

class Student:
  def __init__(self, name):
    self.name = name
    self.__grade = 0

  def set_grade(self, grade):
    if 0 <= grade <= 100:
      self.__grade = grade
    else:
      print("Grade must be between 0 and 100")

  def get_grade(self):
    return self.__grade

  def get_status(self):
    if self.__grade >= 60:
      return "Passed"
    else:
      return "Failed"

student = Student("Emil")
student.set_grade(85)
print(student.get_grade())
print(student.get_status())

# Protected Properties
# Python also has a convention for protected properties using a single underscore _ prefix:

class Person:
  def __init__(self, name, salary):
    self.name = name
    self._salary = salary # Protected property

p1 = Person("Linus", 50000)
print(p1.name)
print(p1._salary) # Can access, but shouldn't
# A single underscore _ is just a convention. It tells other programmers that the property is intended for internal use, but Python doesn't enforce this restriction.

# protected & private کنار هم
class Animal:
    def __init__(self):
        self.name = "Rex"       # public
        self._age = 5           # protected
        self.__secret = "..."   # private

# Private methods:  use __ again
class Calculator:
  def __init__(self):
    self.result = 0

  def __validate(self, num):
    if not isinstance(num, (int, float)):
      return False
    return True

  def add(self, num):
    if self.__validate(num):
      self.result += num
    else:
      print("Invalid number")

calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)
# calc.__validate(5) # This would cause an error چون یک متد پرایوت هست
# Private Method در واقع
# متدی است که برای استفاده داخلی کلاس ساخته شده و معمولاً نباید مستقیماً از بیرون کلاس صدا زده شود.

# Name Mangling دستکاری نام
# Name mangling is how Python implements private properties and methods.
# When you use double underscores __, Python automatically renames it internally by adding _ClassName in front.
# For example, __age becomes _Person__age.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

p1 = Person("Emil", 30)
print(p1._Person__age) # Not recommended!
# اگرچه میشه به پرایوت ها اینطوری دسترسی پیدا کرد؛
# ولی پیشنهاد نمیشه چون هدف کپسوله سازی رو نقض میکنه

# Code Challenge: (solved)
class ScoreBoard:
  def __init__(self, score):
    self.__score = score
  
  def get_score(self):
    return self.__score

s1 = ScoreBoard(0)
print(s1.get_score())

# Inner Classes
# An inner class is a class defined inside another class. The inner class can access the properties and methods of the outer class.
# Inner classes are useful for grouping classes that are only used in one place, making your code more organized.
class Outer:
  def __init__(self):
    self.name = "Outer Class"

  class Inner:
    def __init__(self):
      self.name = "Inner Class"

    def display(self):
      print("This is the inner class")

outer = Outer()
print(outer.name)

# To access the inner class, create an object of the outer class, and then create an object of the inner class:
class Outer:
  def __init__(self):
    self.name = "Outer"

  class Inner:
    def __init__(self):
      self.name = "Inner"

    def display(self):
      print("Hello from inner class")

outer = Outer()
inner = outer.Inner()
inner.display()

# Accessing Outer Class from Inner Class
# Inner classes in Python do not automatically have access to the outer class instance.
# If you want the inner class to access the outer class, you need to pass the outer class instance as a parameter:
class Outer:
  def __init__(self):
    self.name = "Emil"

  class Inner:
    def __init__(self, outer):
      self.outer = outer

    def display(self):
      print(f"Outer class name: {self.outer.name}")

outer = Outer()
inner = outer.Inner(outer)
inner.display()

# ساختارش:
# Outer CLASS
#     │
#     └── Inner CLASS


# outer OBJECT
#     │
#     └── name = "Emil"


# inner OBJECT
#     │
#     └── outer ───────→ outer OBJECT
#                          │
#                          └── name = "Emil"

# Inner classes are useful for creating helper classes that are only used within the context of the outer class:
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
    self.engine = self.Engine()

  class Engine:
    def __init__(self):
      self.status = "Off"

    def start(self):
      self.status = "Running"
      print("Engine started")

    def stop(self):
      self.status = "Off"
      print("Engine stopped")

  def drive(self):
    if self.engine.status == "Running":
      print(f"Driving the {self.brand} {self.model}")
    else:
      print("Start the engine first!")

car = Car("Toyota", "Corolla")
car.drive()
car.engine.start()
car.drive()

# Multiple Inner Classes
# A class can have multiple inner classes:
class Computer:
  def __init__(self):
    self.cpu = self.CPU()
    self.ram = self.RAM()

  class CPU:
    def process(self):
      print("Processing data...")

  class RAM:
    def store(self):
      print("Storing data...")

computer = Computer()
computer.cpu.process()
computer.ram.store()