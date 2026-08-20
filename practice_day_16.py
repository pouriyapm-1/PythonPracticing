# File Handling

# open(filename, mode)
# modes: 
# "r"  Read
# "a"  Append
# "w"  Write
# "x"  Create
# how the file handled : "t" or "b" (text mode or binary mode)

f = open("testfile.txt")
# f = open("demofile.txt", "rt") مثل بالایی هست
# چون مقادیر r,t دیفالت هستند

# اگر توی همون فولدر نباشه: مسیرشو باید مشخص کنیم
# f = open("C:\\...")

print(f.read())

# You can also use the with statement when opening a file:
# Then you do not have to worry about closing your files, the with statement takes care of that.
with open("testfile.txt") as f:
  print(f.read())

# It is a good practice to always close the file when you are done with it.
# (if u're not using with statement)
f = open("testfile.txt")
print(f.readline())
f.close()

with open("testfile.txt") as f:
  print(f.read(5))  # <--- how many characters u want to return

with open("testfile.txt") as f:
  print(f.readline()) # <--- read one line
  # f.readlines() همه خط هارو میخونه و میندازه شون توی یه لیست

with open("testfile.txt") as f:
  print(f.readline())
  print(f.readline())  # <--- read the first two lines

# Loop through the file line by line:
with open("testfile.txt") as f:
  for x in f:
    print(x)

# Write to an existing file
# "a"    Append - will append to the end of the file
# "w"    Write - will overwrite any existing content

with open("testfile.txt", "a") as f:
  f.write("Now the file has more content!")
# open and read the file:
with open("testfile.txt") as f:
  print(f.read())

with open("testfile.txt", "w") as f:
  f.write("This is a whole new content!")

with open("testfile.txt"):
  print(f.read())

# writelines() نوشتن چند رشته در فایل
# lines = ["Apple\n", "Banana\n", "Orange\n"]
# file.writelines(lines)  \n رو خودت باید بذاری

# create a new file:  use "x"
open("testfile2.txt", "x")

# To delete a file, you must import the OS module, and run its os.remove() function:
import os
os.remove("testfile2.txt")

# Check if File exists before remove:
import os
if os.path.exists("testfile2.txt"):
  os.remove("testfile2.txt")
else:
  print("The file does not exist")

# To delete an entire folder, use the os.rmdir() method:
# (You can only remove empty folders.)
import os
os.rmdir("myfolder")


# File Handling Exercises
with open("students.txt", "w") as f:
  f.write("ali\nmmd\nreza\nakbar\nemad")
with open("students.txt", "r") as f:
  print(f.read())

with open("students.txt", "r") as f:
  for i in f:
    print(i.strip()) 


count = 0
with open("students.txt", "r") as f:
  for i in f:
    count += 1
print(count)


with open("numbers.txt", "w") as numbersfile:
  for x in range(1,11):
    numbersfile.write(str(x))
    numbersfile.write("\n")

with open("numbers.txt", "r") as numbersfile:
  print(numbersfile.read())

with open("numbers.txt", "a") as numbersfile:
  numbersfile.write("11\n12\n13\n14\n15")


with open("scores.txt", "w") as scoresfile:
  scoresfile.write("Ali,18\nReza,15\nSara,20\nMina,12")

with open("scores.txt", "r") as scoresfile:
    for line in scoresfile:
        name, score = line.strip().split(",")
        score = int(score)

        if score >= 18:
            print(name, score)
            with open("passed.txt", "a") as passed:
              passed.write(f"{name},{score}\n")