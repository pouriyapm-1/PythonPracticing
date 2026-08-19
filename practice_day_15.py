# Classes Inheritance
class Animal:  # <--- Parent
  def speak(self):
    print("animal sound")

class Dog(Animal): # <--- Child
  pass
dog = Dog()
dog.speak()

# child can use parent's methods and attributes
# child can have its own methods
# child can override methods : از همین مثال بالایی مثال میزنم
class Animal:
  def speak(self):
    print("animal sound")

class Dog(Animal):
  def speak(self):
    print("Woof!")

dog = Dog()
dog.speak() # prints Woof!

# child can have its own __init__
# .super()   متد پرنت رو اجرا کن
# super().speak() یا super().__init__    مثلا

# isinstance(dog, Dog)   is dog an object of Dog?
# issubclass(Dog, Animal)  # آیا داگ از انیمال ارث بری میکند؟

# Exercises
class Animal:
  def __init__(self, name):
    self.name = name
  def speak(self):
    print(self.name)

class Dog(Animal):
  pass

d1 = Dog("Rex")
d1.speak()
#نکته تمرین: داگ خودش نه اینیت داره و نه اسپیک. هردو رو به ارث برده

class Animal:
  def __init__(self, name):
    self.name = name
  def speak(self):
    print("Animal is speaking")

class Dog(Animal):
  def __init__(self, name, breed):
    super().__init__(name)
    self.breed = breed
  def info(self):
    print(self.name)
    print(self.breed)

d1 = Dog("Rex", "German Shepherd")
d1.info()
d1.speak()

# فلسفه تابع سوپر
# از قابلیت/منطق کلاس والد استفاده کن، به‌جای اینکه دوباره خودت آن را بنویسی.

class Vehicle:
  def __init__(self, brand):
    self.brand = brand
  def move(self):
    print("Vehicle is moving")

class Car(Vehicle):
  def move(self):
    print("Car is driving")
    
v1 = Vehicle("Generic")
c1 = Car("BMW")
v1.move()
c1.move()


class Employee:
  def work(self):
    print("Employee is working")

class Developer(Employee):
  def work(self):
    print("Developer is coding")

class Designer(Employee):
  def work(self):
    print("Designer is designing")

e = Employee()
developer1 = Developer()
designer1 = Designer()

e.work()
developer1.work()
designer1.work()


class BankAccount:
  def __init__(self, owner, balance):
    self.owner = owner
    self.balance = balance
  def info(self):
    print(self.owner)
    print(self.balance)

class SavingsAccount(BankAccount):
  def __init__(self, owner, balance, interest_rate):
    super().__init__(owner, balance)
    self.interest_rate = interest_rate
  def info(self):
    print(self.owner)
    print(self.balance)
    print(self.interest_rate)

account = SavingsAccount("Pouriya", 5000, 0.18)
account.info()


class Notification:
  def __init__(self, recipient):
    self.recipient = recipient
  def send(self):
    print("Sending notification")

class EmailNotification(Notification):
  def __init__(self, recipient):
    super().__init__(recipient)
  def send(self):
    print(f"Sending email to {self.recipient}")

class SMSNotification(Notification):
  def __init__(self, recipient):
    super().__init__(recipient)
  def send(self):
    print(f"Sending SMS to {self.recipient}")

email = EmailNotification("user@gmail.com")
sms = SMSNotification("09120000000")

email.send()
sms.send()

# Polymorphism
# یک متد مشترک ولی رفتار متفاوت برای آبجکت های مختلف

class Guitar:
  def play(self):
    print("playing guitar")
class Piano:
  def play(self):
    print("playing piano")
class Drums:
  def play(self):
    print("playing drums")

g1 = Guitar()
p1 = Piano()
d1 = Drums()

g1.play()
p1.play()
d1.play()

instruments = [g1, p1, d1]
for i in instruments:
  i.play()



class Bank_Card_Payment:
  def __init__(self, card_number):
    self.card_number = card_number
  def pay(self):
    # ...
    print("Successful! Payment via bank card completed.")

class PayPal_Payment:
  def __init__(self, paypal_number):
    self.paypal_number = paypal_number
  def pay(self):
    # ...
    print("Successful! Payment via PayPal completed.")

class Cryptocurrency_Payment:
  def __init__(self, crypto_number):
    self.crypto_number = crypto_number
  def pay(self):
    # ...
    print("Successful! Payment via cryptocurrency completed.")
pay1 = Bank_Card_Payment("6037991722347346")
pay2 = PayPal_Payment("1416968")
pay3 = Cryptocurrency_Payment("54123415")

pay_list = [pay1, pay2, pay3]
for i in pay_list:
  i.pay()


class Vehicle:
  def __init__(self):
    pass
  def moving_style(self):
    print("Vehicle is moving!")

class Car(Vehicle):
  def moving_style(self):
    print("Driving on the road")
class Motorcycle(Vehicle):
  def moving_style(self):
    print("Riding on the road")
class Airplane(Vehicle):
  def moving_style(self):
    print("Flying in the sky")

c1 = Car()
m1 = Motorcycle()
a1 = Airplane()

vehicles = [c1, m1, a1]
for i in vehicles:
  i.moving_style()

# Encapsulation
# یعنی کنترل کردن دسترسی به داده ها و جزئیات داخلی یک آبجکت
# self.name       public
# self._name      protected این عضو داخلیه؛ بهتره از بیرون مستقیماً باهاش کار نکنی.
# self.__name     private پایتون از نیم منگلینگ استفاده میکنه و دسترسی مستقیمش از بیرون رو محدود میکنه