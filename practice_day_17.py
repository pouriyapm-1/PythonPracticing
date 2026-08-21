# Numpy : a python library (Numerical Python)
import numpy as np  # معمولا با همین نام مستعار استفاده میشه

# Numpy ndarray object
# The array object in NumPy is called ndarray.
# We can create a NumPy ndarray object by using the array() function

import numpy as np
arr = np.array([1,5,7,9])
print(arr)
print(type(arr)) # type : numpy.ndarray

# To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray:
arr = np.array((1, 2, 3, 4, 5)) # use a tuple to create array
print(arr)

# Dimensions in array: is one level of array depth (nested arrays).
# 0-D Arrays (Scalars): the elements in an array
# Each value in an array is a 0-D array.
arr = np.array(43)
print(arr)

# 1-D Arrays
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# 2-D Arrays: An array that has 1-D arrays as its elements
# NumPy has a whole sub module dedicated towards matrix operations called numpy.mat
arr = np.array([[1,2,3],[4,5,6]])
print(arr)

# 3-D Arrays: an array that has 2-D arrays(matrices) as its element
# These are often used to represent a 3rd order tensor. (تانسور مرتبه سوم)
arr = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr)

# Check Number of Dimensions
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
a = np.array(46)
b = np.array([1,5,7])
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[[2,3,6],[7,8,9]],[[2,3,6],[7,8,9]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# An array can have any number of dimensions.
# ndmin: When the array is created, you can define the number of dimensions by using the ndmin argument.
arr = np.array([1,2,3], ndmin = 6)
print(arr)
print(arr.ndim)

# -----------------------
# Array Indexing
# You can access an array element by referring to its index number.
# The indexes in NumPy arrays start with 0
arr = np.array([1, 2, 3, 4])
print(arr[0])
print(arr[2] + arr[3]) # جمع آرایه سوم و چهارم

# Access 2-D arrays
# Think of 2-D arrays like a table with rows and columns,
# where the dimension represents the row and the index represents the column.
arr = np.array([[2,4,6,8],[1,3,5,7]])
# عنصر ردیف اول ستون دوم را چاپ کن
print(arr[0,1])   # prints 4

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# 2nd row, 5th column
print("5th element on 2nd row:", arr[1,4])


# Access 3-D arrays
arr = np.array([[[1,2,3],[4,5,6]],[[12,13,14],[15,16,17]]])
# Access the third element of the second array of the first array:
print(arr[0,1,2])

# Use negative indexing to access an array from the end.
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[1,-1])   # prints last element of 2nd dimension


# Array Slicing
# [start:end:step] 

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])   # prints [2,3,4,5]

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[4:])    # prints [4,5,6,7]
print(arr[:3])    # prints [1,2,3]

# Negative Slicing
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-4:-1])  # [4,5,6]

# using step
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2]) # [2,4]

arr = np.array([1, 2, 3, 4, 5, 6, 7])
# همه عناصر یکی در میون
print(arr[::2])

# Slice 2-D arrays
# From the second element, slice elements from index 1 to index 4 (not included):
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# From both elements, return index 2:
print(arr[0:2, 2])   # prints [3,8]

# from both elements, slice index 1 to index 4
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])  # prints a 2-D array

# Data Types in NumPy
# NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.
# Below is a list of all data types in NumPy and the characters used to represent them.
# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

# Checking the Data Type of an Array:  dtype
ar = np.array([1,5,8,4])
print(ar.dtype)   #int64

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)  #U6

# array() function can take an optional argument : dtype
# it allows to define the data type of the array elements

# مثال: یه آرایه بساز با دیتا تایپ استرینگ
arr = np.array([1,2,3,4], dtype="S")
print(arr)
print(arr.dtype)

# For i, u, f, S and U we can define size as well.
# Create an array with data type 4 bytes integer:
arr = np.array([1, 2, 3, 4], dtype='i4')

# ValueError: In Python ValueError is raised when the type of passed argument to a function is unexpected/incorrect.
import numpy as np
# arr = np.array(['a', '2', '3'], dtype='i')  it causes error

# Convert data type on existing arrays
arr1 = np.array([1.1,2.6,3.7])
print(arr1.dtype)  #it's float
arr2 = arr1.astype("i")
print(arr2)         # prints [1,2,3]
print(arr2.dtype)   # int 
# or we can use it like this: arr2 = arr1.astype(int) یعنی کامل بنویسیم دیتا تایپ جدیدو
arr = np.array([1,0,5,6])
newarr = arr.astype(bool)
print(newarr) # True False True True
print(newarr.dtype) # bool

# Copy vs view
# The Difference Between Copy and View
# The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.
# copy owns its data and changes will not affect the original و برعکس
# view does not own the data and changes will affect the original و برعکس

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
print(x)
x[0] = 34
print(x)
print(arr)

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

# Check if Array Owns its Data
# Every NumPy array has the attribute base that returns None if the array owns the data.
# Otherwise, the base attribute refers to the original object.

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)

# The copy returns None.
# The view returns the original array.

# Array Shape
# The shape of an array is the number of elements in each dimension.
# arr.shape() : get a tuple that...
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)  # prints (2,4)
# means that the array has 2 dimensions, where the first dimension has 2 elements and the second has 4.

arr = np.array([1,2,3,4], ndmin=5)
print(arr)
print(arr.shape)  #prints (1,1,1,1,4)
# اعداد صحیح در هر اندیس، تعداد عناصر بُعد مربوطه را نشان می‌دهند
# for example 5th dimension has 4 elements


# Array Reshaping (changing the shape)
# By reshaping we can add or remove dimensions or change number of elements in each dimension.
# Convert the following 1-D array with 12 elements into a 2-D array.

# The outermost dimension will have 4 arrays, each with 3 elements:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4,3)
print(newarr)

# 1-D to 3-D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2,3,2)
print(newarr)

# Can We Reshape Into any Shape? No.
# Yes, as long as the elements required for reshaping are equal in both shapes.

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# newarr = arr.reshape(3, 3)
# print(newarr)   raises an error
# because 3 * 3 = 9 and we have 8 elements.

print(newarr.base)  # it returns view

# Unknown dimension
# You are allowed to have one "unknown" dimension.
# Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
# Pass -1 as the value, and NumPy will calculate this number for you.
# میتونی بجای فقط یکی از بعد ها 1- بذاری و پایتون خودش حساب میکنه (توی متد reshape)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2,2,-1)
print(newarr)

# Flattening array
# Flattening array means converting a multidimensional array into a 1D array.
# We can use reshape(-1) to do this.
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
newarr1 = arr1.reshape(-1)
print(newarr1)

# There are a lot of functions for changing the shapes of arrays and rearranging elements in numpy
# ولی فعلا لازم نداریمشون
