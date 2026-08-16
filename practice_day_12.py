# RegEx : A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.
import re   # a built-in module which can be used to work with Regular Expressions

# Search the string to see if it starts with "The" and ends with "Spain":
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

# RegEx Functions
# findall	  Returns a list containing all matches
# search	  Returns a Match object if there is a match anywhere in the string
# split	    Returns a list where the string has been split at each match
# sub	      Replaces one or many matches with a string

# Metacharacters
# Flags     
# Special Sequences
# Sets

# Metacharacters exercises: (Obsidian)

import re
text = "cat dog category cat scatter"
x = re.findall("cat", text)
print(x)

import re
text = "cat"
x = re.findall("c.t", text)
print(x)

import re
text = "cat"
x = re.findall("c.t", text)
print(x)

import re
text = "Hello World"
x = re.search("^Hello.*World$", text)
print(x)

import re
text = "a aa b aaa bb aaaa"
x = re.findall("a+", text)
print(x)

import re
text = "" 
x = re.findall("ba*", text)
print(x)

import re
text = "" 
x = re.findall("colou?r", text)
print(x)

import re
text = "" 
x = re.findall("^[0-9]{3}$", text)
print(x)

import re
text = "" 
x = re.findall("^[0-9]{3}$", text)
print(x)

import re
text = "I have a cat and a dog. My friend has a cat." 
x = re.findall("cat|dog", text)
print(x)

import re
text = "" 
x = re.findall("(I love cats)|(I love dogs)", text)  # or I love (cats|dogs)
print(x)

import re
text = "apples cars bananas apps cats ants"
x = re.findall("^a.*s$", text)
print(x)

# Special Sequences exercises: (Obsidian)

import re
text = "I have 2 apples, 15 bananas and 300 oranges."
x = re.findall("\d", text)
print(x)

import re
text = "Python 3.12 is great!"
x = re.findall("\D", text)
print(x)

import re
text = "Hello_world 123!"
x = re.findall("\w",text)
print(x)

import re
text = "Hello world\nHow are you?"
x = re.findall("\s",text)
print(x)

import re
text = "Hi there!"
x = re.findall("\S",text)
print(x)

import re
text = "cat category scatter catfish cat"
x = re.findall(r"\bcat\b",text)
print(x)

import re
text = "Python is very cool!"
x = re.findall("\w+",text)  # /w فقط کاراکتر هارو برمیگردونه
# /w+ جایی که کاراکترا پشت هم قرار گرفتن (کلمه) هارو پیدا میکنه
print(x)

import re
text = "I bought 25 apples, 3 bananas and 100 oranges."
x = re.findall("\d+",text)  
print(x)

# 9 and 10 تکراری
# RegEx Sets...

#RegEx Functions:

# findall()   The findall() function returns a list containing all matches.
# The list contains the matches in the order they are found.
# If no matches are found, an empty list is returned
#همه رو پیدا کن و به صورت list بده.

# search()   searches the string for a match, and returns a Match object if there is a match.
# If there is more than one match, only the first occurrence of the match will be returned
#اولین match رو پیدا کن.

# split()    returns a list where the string has been split at each match
# You can control the number of occurrences by specifying the maxsplit parameter:
# بر اساس Regex متن رو تکه‌تکه کن.
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)  # فقط در وایت اسپیس اول، اسپلیت می کند.
print(x)

# sub()    replaces the matches with the text of your choice
# Replace every white-space character with the number 9:
# پیدا کن و جایگزین کن.
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

# You can control the number of replacements by specifying the count parameter
# Replace the first 2 occurrences: # دوتای اولی که پیدا کردی رو جایگزین کن
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

# Match Object : is an object containing information about the search and the result.
# Note: If there is no match, the value None will be returned, instead of the Match Object.

# Match Object methods:
# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match

# group() → WHAT?  🎯
# string()  → WHERE? 📝
# span()   → WHERE EXACTLY? 📍