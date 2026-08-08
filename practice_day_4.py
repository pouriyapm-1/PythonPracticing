# if elif else
x = 4
if x % 2 == 0:
  print("even number")
else: print("odd number")

n = 5
if n == 1:
  print("Current day of the week: Monday")
elif n == 2:
  print("Current day of the week: Tuesday")
elif n == 3:
  print("Current day of the week: Wednesday")
elif n == 4:
  print("Current day of the week: Thursday")
elif n == 5:
  print("Current day of the week: Friday")
elif n == 6:
  print("Current day of the week: Saturday")
elif n == 7:
  print("Current day of the week: Sunday")
else:
  print("The entered number is not showing a day of a week")

x = 16
y = 21
max_value = x if x>y else y
print("maximum:",max_value)

# pass statement: when you wanna if to be empty
a = 33
b = 200
if b > a:
  pass

# Match
# Instead of writing many if..else statements, you can use the match statement.
# The match statement selects one of many code blocks to be executed.

# _ for default case
day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")

# While loops
# break   continue   else
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

print("---------------------")