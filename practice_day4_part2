# while exercises

# اعداد ۱ تا ۱۰ رو چاپ کن
i = 1
while i <= 10:
  print(i)
  i += 1

# اعداد زوج بین ۱ تا ۲۰ رو چاپ کن
a = 1
while a <= 20:
  if a % 2 == 0:
    print(a)
  a += 1

# از ۱۰ تا ۱ رو با while چاپ کن و آخرش بنویس: Blast off! 🚀
b = 10
while b >= 1:
  print(b)
  b -= 1
print("Blast off!")

#مجموع اعداد ۱ تا ۱۰۰ رو حساب کن و در نهایت 5050 رو چاپ کن.
z = 1
total = 0
while z <= 100:
  total = total + z
  z += 1
print(total)  

#یک عدد از کاربر بگیر و جدول ضرب ۱ تا 100 اون عدد رو چاپ کن
k = int(input("enter a number: "))
n = 1
mazrab = 1
while n <= 10:
  mazrab = k * n
  print(mazrab)
  n += 1

#از کاربر عدد بگیر و تا وقتی عدد مثبت وارد می‌کنه، اعداد رو با هم جمع کن. 
# وقتی 0 یا عدد منفی وارد شد، حلقه متوقف بشه و مجموع چاپ بشه.
total = 0
x = int(input("enter a number: "))
while x > 0:
  total = total + x
  x = int(input("enter another number:"))
print("sum is: ", total)

# یک عدد مخفی تعیین کن. بعد با حلقه وایل، از کاربر عدد بگیر تا درست حدس بزنه
# below the number: too low ,  above the number: too high

secret = 54
x = int(input("Enter your guess number: "))
while x:
  if x > secret:
    print("Too high! try again.")
  elif x < secret:
    print("Too low! try again.")
  else:
    print("yesss! Currect.")
    break
  x = int(input("Enter your guess number again: "))

  # پسورد درست رو داخل برنامه تعیین کن
  #از کاربر پسورد بگیر و تا وقتی اشتباهه، دوباره درخواست کن. وقتی درست وارد کرد بگو آفرین
password = "py12345"
x = input("guess the password: ")
while x:
  if x == password:
    print("Access granted!")
    break
  else:
    x = input("wrong passwod, guess the password again: ")

# برنامه‌ای بنویس که از کاربر یک عدد صحیح مثبت بگیره و با استفاده از حلقه وایل حساب کنه چند رقم داره.
x = int(input("Enter a number: "))
count = 0
while x > 0:
  count += 1
  x = x // 10
print("number of digits:", count)

# برنامه‌ای بنویس که یک عدد صحیح مثبت از کاربر بگیره و با استفاده از ، عدد رو برعکس کنه.
x = int(input("Enter a number: "))
latest_digit = 0
new_num = 0
while x > 0:
  latest_digit = x % 10
  x = x // 10
  new_num = new_num * 10 + latest_digit
print(new_num)
