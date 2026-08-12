# Recursion : Recursion is when a function calls itself.
# Every recursive function must have two parts:
# A base case - A condition that stops the recursion
# A recursive case - The function calling itself with a modified argument

# a simple recursive function:
def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n-1)

countdown(8)    

# Fibonacci sequence
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))

# calculate the sum of all elements in a list
mylist = [5,7,9,4,13]
def sum_list(numbers):
  if len(numbers) == 0:
    return 0
  else:
    return numbers[0] + sum_list(numbers[1:])
print(sum_list(mylist))

# Find the maximum value in a list:
mylistt = [4,7,8,11]
def max_list(numbers):
  if len(numbers) == 1:
    return numbers[0]
  else:
    max_of_rest = max_list(numbers[1:])
    if max_of_rest > numbers[0]:
      return max_of_rest
    else:
      return numbers[0]

print(max_list(mylistt))

# Generators
# Generators are functions that can pause and resume their execution.
# When a generator function is called, it returns a generator object, which is an iterator.
# The code inside the function is not executed yet, it is only compiled. The function only executes when you iterate over the generator.
# Generators allow you to iterate over data without storing the entire dataset in memory.
# Instead of using return, generators use the yield keyword.
def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)

def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)

# You can manually iterate through a generator using the next() function:
def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))

# Similar to list comprehensions, you can create generators using generator expressions with parentheses instead of square brackets:
# List comprehension vs generator expression:

# List comprehension - creates a list
list_comp = [x * x for x in range(5)]
print(list_comp)

# Generator expression - creates a generator
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))

# Generate 100 Fibonacci numbers:
def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

# Get first 100 Fibonacci numbers
gen = fibonacci()
for _ in range(100):
  print(next(gen))

# Generator Methods
# The .send() method allows you to send a value to the generator
def echo_generator():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen) # Prime the generator
gen.send("Hello")
gen.send("World")

# The .close() method stops the generator:
def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close()

# try: یه کد
# finally: این بخش در پایان اجرا میشه