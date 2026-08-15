# JSON
# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.
# Convert from JSON to Python: json.loads()
#              Python to json: json.dumps()

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

# Python:	JSON:
# dict	  Object
# list	  Array
# tuple	  Array
# str	    String
# int	    Number
# float	  Number
# True	  true
# False	  false
# None	  null

# Use the indent parameter to define the numbers of indents:
json.dumps(x, indent=4)

# Use the separators parameter to change the default separator:
# default value is (", ", ": ")
json.dumps(x, indent=4, separators=(". ", " = "))

#Use the sort_keys parameter to specify if the result should be sorted or not:
json.dumps(x, indent=4, sort_keys=True)

# json exercises
# یک دیکشنری پایتونی بساز و بعد تبدیلش کن به یک رشته جیسون
import json

person = {
  "name":"Ali",
  "age":22,
  "city":"Tehran"
}

x = json.dumps(person)
print(x)

# رشته جیسون زیر را به یک ساختار داده پایتون تبدیل کن و مقدار age را چاپ کن
import json
x = {"name": "Sara", "age": 25, "city": "Mashhad"}
y = json.loads(x)
print(y["age"])

# یک دیکشنری پایتون بساز که شامل اطلاعات یک کتاب باشد:
# آن را به JSON تبدیل کن و سپس دوباره به ساختار داده‌ی پایتون برگردان.
#در پایان مقدار title را چاپ کن.
import json

book_details = {
  "title" : 1984,
  "author" : "George Orwell",
  "year" : 1949
}

x = json.dumps(book_details)
y = json.loads(x)
print(y["title"])

# یک JSON string شامل اطلاعات زیر بساز:
# آن را به ساختار داده‌ی پایتون تبدیل کن و مقدار skills را چاپ کن.
import json
x = '{"name": "Reza", "age": 21, "skills": ["Python", "Git", "SQL"]}'

y = json.loads(x)
print(y["skills"])

# یک رشته جیسونی شامل اطلاعات زیر بساز
# آن را به ساختار داده‌ی پایتون تبدیل کن و مقدار city را چاپ کن.
import json

info = '{"name": "Ali", "age": 22, "address": { "city": "Tehran", "street": "Valiasr"} }'
y = json.loads(info)
print(y["address"]["city"])

# یک JSON string بساز که شامل اطلاعات دو دانش‌آموز باشد. هر دانش‌آموز باید name و age داشته باشد.
# سپس 
# آن را به ساختار داده‌ی پایتون تبدیل کن و نام دانش‌آموز دوم را چاپ کن.
import json

students = '{"student1":{"name":"ali","age":12},"student2":{"name":"reza","age":13}}'
x = json.loads(students)
print(x["student2"]["name"])

# یک JSON string بساز که شامل اطلاعات یک محصول باشد:
# سپس 
# آن را به ساختار داده‌ی پایتون تبدیل کن و قیمت محصول را چاپ کن.
import json
product_information = '''{
  "name": "earpods",
  "price": 300,
  "category": "gadjets",
  "in_stock": "yes"
}'''
x = json.loads(product_information)
print(x["price"])