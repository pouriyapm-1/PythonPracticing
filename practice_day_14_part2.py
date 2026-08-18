# Inner Classes Exercises

# attribute
# یعنی یک ویژگی یا داده که مربوط به شیء یا کلاس است
class Car:
    def __init__(self):
        self.brand = "BMW" # <--- 
        self.color = "Black" # <--- attributes
        self.speed = 200 # <---
# در اینجا برند، کالر و اسپید اتریبیوت های آبجکت فعلی هستن
# Attribute ویژگی‌ایه که object داره؛ بعضی attributeها مقدارشون از کاربر/پارامتر میاد و بعضی‌ها مقدار اولیه یا ثابت خودشون رو داخل کلاس دارن.

# دسترسی از کلاس بیرونی به کلاس درونی
class Outer:
  def __init__(self):
    self.name = "Outer"

  class Inner:
    def __init__(self):
      self.name = "Inner"
    def hellofrominner(self):
      print("Hello from inner class :D")
outer = Outer()
inner = outer.Inner()
inner.hellofrominner()

#دسترسی از کلاس درونی به کلاس بیرونی
class Outer:
  def __init__(self):
    self.name = "Emilia"

  class Inner:
    def __init__(self, outer):
      self.outer = outer
    def greet(self):
      print(f"Hello and welcome {self.outer.name}")
outer = Outer()
inner = outer.Inner(outer)
inner.greet()

class BankAccount:
  def __init__(self, owner):
    self.owner = owner

  class Card:
    def __init__(self, bankAccount):
      self.bankAccount = bankAccount
    def show_owner(self):
      print("owner name: ", self.bankAccount.owner)
bankAccount = BankAccount("Pouriya")
card = bankAccount.Card(bankAccount)
card.show_owner()

class Restaurant:
  def __init__(self, name):
    self.name = name

  class Order:
    def __init__(self, restaurant):
      self.restaurant = restaurant
    def show_restaurant(self):
      print("Restaurant Name: ", self.restaurant.name)
PizzaHouse = Restaurant("Akbari")
order_obj = PizzaHouse.Order(PizzaHouse)
order_obj.show_restaurant()

class Library:
  def __init__(self, name):
    self.name = name

  class Book:
    def __init__(self, title, library):
      self.title = title
      self.library = library
    def show_info(self):
      print("Book Title: " + self.title)
      print("Library Name: " + self.library.name)
# Central Library, Python Basics
Library_obj = Library("Central Library")
Book_obj = Library_obj.Book("Python Basics", Library_obj)
Book_obj.show_info()

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  class Engine:
    def __init__(self,car,engine_type):
      self.car = car
      self.engine_type = engine_type
    def show_car_info(self):
      print("brand: ", self.car.brand)
      print("model: ", self.car.model)

#Brand: BMW Model: M4 Engine: V6 and execute show_car_info
# engine = Car.Engine("V5")
car_object = Car("BMW","M4")
engine_object = car_object.Engine(car_object, "V6")
engine_object.show_car_info()


# Class Methods
@classmethod
def show_user_count(cls):
    print(cls.user_count)

# cls represents User class.
# without @classmethod decorator, it will be a regular method.
# cls: همون نقشی رو برای کلاس داره که سلف برای آبجکت داشت
# مثالش:
class User:
    user_count = 0

    @classmethod
    def show_count(cls):
        print(cls.user_count)

# class attribute
# متعلق به کلاس هست و بین تمام آبجکت ها مشترکه
class User:
  counter = 0 # <--

# we can call class methods without creating object
User.show_count()

# Class Methods Exercises:
class User:
  user_count = 0
  def __init__(self ,name, age):
    self.name = name
    self.age = age
    User.user_count += 1
  @classmethod
  def show_user_count(cls):
    print("Total users: ", cls.user_count)
new_user = User("Ali", 20)
new_user = User("Reza", 25)
new_user = User("Sara", 22)
User.show_user_count()


class Product:
  product_count = 0
  def __init__(self, name, price):
    self.name = name
    self.price = price
    Product.product_count += 1
  @classmethod
  def show_product_count(cls):
    print("Total products:", cls.product_count)

Product("cake", 20)
Product("shampoo", 70)
Product("lollipop", 10)
Product.show_product_count()


class Company():
  country = "Iran"
  def __init__(self, name):
    self.name = name
  @classmethod
  def change_country(cls, new_country):
    cls.country = new_country

company1 = Company("Apple")
company2 = Company("Google")
print(company1.country)
print(company2.country)
Company.change_country("Germany")
print(company1.country)
print(company2.country)

# Alternative Constructor: یک راه دوم برای ساختن آبجکت از یه کلاس
# بیشتر برای تبدیل فرمت‌های مختلف داده به آبجکت استفاده میشه.
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split(",")
        return cls(name, int(age))

# تمرین ازش
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  @classmethod
  def from_string(cls, data):
    name,age = data.split(",")
    return cls(name, int(age))

person = Person.from_string("Pouriya,21")
print(person.name)
print(person.age)