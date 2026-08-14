# Functions exercises

# تابعی که 3 تا عدد دریافت کند و میانگین آنها را برگرداند
def calculate_average(a,b,c):
  return (a+b+c) / 3
print(calculate_average(10,20,30))

# تابعی که یک اسم دریافت کند و خوش آمد گویی کند. مقدار پیش فرض هم داشته باشد
def greet(name = "Guest"):
    return "Hello, " + name + "!"

print(greet("Ali"))
print(greet())

# تابعی بنویس که سه آرگومان
# name age grade 
# داشته باشد. تابع باید اطلاعات دانش‌آموز را چاپ کند.
# تابع را طوری صدا بزن که ترتیب آرگومان‌ها مهم نباشد
def student_info(name,age,grade):
   print("Name:",name)
   print("Age:",age)
   print("Grade:" ,grade)
student_info(grade = "11th",name = "reza",age = 24)

# تابعی بنویس که بتواند هر تعداد عددی که به آن می‌دهیم دریافت کند و مجموع همه‌ی آن‌ها را برگرداند.
def sum_numbers(*numbers):
   total = 0
   for i in numbers:
      total += i
   return(total)
print(sum_numbers(1,6,7,8,9,4))

# تابعی بنویس که بتواند هر تعداد اطلاعات با نام دلخواه دریافت کند و هر کلید و مقدار را در یک خط چاپ کند.
def person_info(**info):
    for key, value in info.items():
        print(key, ":", value)
person_info(name = "Ali", age = "22", city = "Tehran", job = "Programmer")

# کدی بنویس که یک متغیر به نام x با مقدار 10 در global scope داشته باشد.
# سپس تابعی به نام test تعریف کن که داخل آن یک متغیر محلی x با مقدار 20 داشته باشد و مقدار x را چاپ کند.
# بعد از اجرای تابع، مقدار x خارج از تابع را هم چاپ کن.
x = 10
def test():
   x = 20
   print(x)

print(x)
test()

# یک تابع لمبدا بنویس که دو عدد دریافت کند و حاصل‌ضرب آن‌ها را برگرداند.
lambdafunc = lambda x,y: x*y
print(lambdafunc(6,7))

# یک تابع لمبدا بنویس که یک عدد دریافت کند و مشخص کند آیا آن عدد زوج است یا نه.
#تابع را با عدد 8 اجرا کن.
if_even = lambda n: n % 2 == 0

#تابعی به نام فاکتوریل بنویس که با استفاده از تابع بازگشتی، فاکتوریل یک عدد را محاسبه کند.
# تابع را با عدد 5 اجرا کن و نتیجه را چاپ کن.
def factorial(x):
   if x <= 1:
      return 1
   else:
      return x * factorial(x-1)

# تابعی به نام sum_to_n بنویس که با استفاده از recursion مجموع اعداد 1 تا n را محاسبه کند.
def sum_to_n(z):
   if z == 1:
      return 1
   else:
      return z + sum_to_n(z-1)

print(sum_to_n(4))

# تابعی به نام countdown بنویس که یک عدد دریافت کند و با استفاده از recursion اعداد را از آن عدد تا 1 چاپ کند.
def countdown(n):
   if n == 1:
      return 1
   else:
      print(n)
      return countdown(n-1)
print(countdown(22))

#تابعی به نام power بنویس که دو عدد base و exponent دریافت کند و با استفاده از recursion مقدار توان را محاسبه کند.
def power(base,exponent):
   if exponent == 1:
      return base
   else:
      return power(base, exponent-1) * base
print(power(2,4))

#تابعی به نام find_minimum بنویس که هر تعداد عدد دریافت کند و کوچک‌ترین عدد را برگرداند.
def find_minimum(*numbers):
   smallest = numbers[0]
   for i in numbers:
      if i < smallest:
         smallest = i
   return smallest
print(find_minimum(6, 4, 1, 7))

# یک decorator به نام uppercase بنویس که خروجی یک تابع را به حروف بزرگ تبدیل کند.
# سپس آن را روی تابعی به نام greet اعمال کن که رشته‌ی "hello world" را برمی‌گرداند.
def uppercase(func):
   def inner():
      return func().upper()
   return inner

@uppercase
def greet():
   return "hello world"
  
print(greet())

#یک decorator به نام double_result بنویس که نتیجه‌ی یک تابع را دو برابر کند.
# سپس آن را روی تابعی به نام add اعمال کن که دو عدد دریافت کرده و مجموعشان را برمی‌گرداند.

def double_result(func):
   def inner(a,b):
      return func(a,b) * 2
   return inner

@double_result
def add(a,b):
   return a + b

print(add(5,6))

# یک generator به نام count_up_to بنویس که یک عدد n دریافت کند و اعداد ۱ تا n را یکی‌یکی تولید کند.

def count_up_to(n):
   count = 1
   while count <= n:
      yield count
      count += 1

for i in count_up_to(5):
   print(i)

# یک generator به نام even_numbers بنویس که یک عدد n دریافت کند و تمام اعداد زوج از ۲ تا n را یکی‌یکی تولید کند.
def even_numbers(n):
   start = 2
   while start <= n:
      yield start
      start += 2

for num in even_numbers(14):
   print(num)

# یک generator به نام multiples_of_three بنویس که یک عدد n دریافت کند و مضرب‌های ۳ را از 3 تا n یکی‌یکی تولید کند.
def multiples_of_three(n):
   counter = 3
   while counter <= n:
      yield counter
      counter += 1
      if counter % 3 == 0:
         yield counter

# تابعی به نام calculate_average بنویس که هر تعداد عدد دریافت کند و میانگین آن‌ها را برگرداند.
def calculate_average(*numbers):
   total = 0
   for i in numbers:
      total += i
   return total / len(numbers)

print(calculate_average(10, 20, 30, 40))