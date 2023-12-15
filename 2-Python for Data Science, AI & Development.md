
## W1 ❉ Python Basics
📓**Say "Hello" to the world in Python**
```python

# Check the Python Version
sys # is a built-in module that contains many system-specific parameters and functions

import sys
print(sys.version)  # 3.11.7

━━━━━━━━━━━━
# Errors in Python
The error message tells you:
1- where the error occurred 
2- what kind of error it was (NameError,SyntaxError)


# if you spell print as frint  Python will display an error message
frint("hi") # NameError Traceback

```
📓 **Types of objects in Python**
```python 
# Python is an object-oriented language
# common object types: (strings - integers - floats)

type() # built-in function to know type of an expression

‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Integers ✥
 # Integers can be negative or positive numbers.

type(-1) # int
type(0)  # int

‗‗‗‗‗‗‗‗‗‗‗‗
✥ Floats ✥
# numbers with decimals can be negative or positive
type(1.0)  #float
type(-0.56) #float

‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Converting from one object type to a different object type ✥

# typecasting ➨ change the type of the object in Python

type(2) # int
type(float(2)) # float

# cast a float into an integer, we could potentially lose some information

int(1.1) # 1
_________________
# Converting from strings to integers or floats
# a string that contains a number within it

# Convert a string into an integer
int('1')# 1

# Convert the string "1.2" into a float
float('1.2') # 1.2
_________________
# Converting numbers to strings

# Convert an integer to a string
str(1) # '1'

# Convert a float to a string
str(1.2) # '1.2'

‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Boolean data type ✥

# An object of type Boolean can take on one of two values: True or False:

# Type of True
type(True) # bool

# Type of False
type(False) # bool

# cast a boolean (True) to an integer or float we will get a one
# cast a boolean (False) to an integer or float we will get a zero.
# cast a 1 to a Boolean get (True).  0 to a Boolean get (False)

# Convert True to int
int(True) # 1

# Convert 1 to boolean
bool(1) # True

# Convert 0 to boolean
bool(0) # False

```

📓**Expression and Variables**
```python 
‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Expressions ✥
# Expressions in Python can include operations among compatible types

# Addition operation expression
43 + 60 + 16 + 41  # 160

# Subtraction operation expression
50 - 60 # -10

# Multiplication operation expression
5 * 5 # 25

# Division operation expression
25 / 5 # 5.0

# Integer division operation expression
25 // 6 # 4

‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Variables ✥

# Store value into variable
x = 43 + 60 + 16 + 41
x # 160

# Use another variable to store the result of the operation between variable and value
y = x / 60
y # 2.6666666

# Overwrite variable with new value
x = x / 60
x # 2.6666666666666665

_________________
# use meaningful variable names, so you and others can read the code and understand it more easily
# Name the variables meaningfully

total_min = 43 + 42 + 57 # Total length of albums in minutes
total_min # 142

total_hours = total_min / 60 # Total length of albums in hours 
total_hours # 2.3666666666666667
```


📓**String Operations**
```python 

# Use " " or '' for defining string
"Michael Jackson"
'@#2_#]&*^%$'

# Print the string
print("hello!") # hello!

# Assign string to variable
name = "Michael Jackson"
name # 'Michael Jackson'

‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Indexing ✥
# string is an ordered sequence. 
# Each element in the sequence can be accessed using an index represented by the array of numbers

# indexing starts at 0, it means the first index is on the index 0

name = "Michael Jackson"

# Print the first element in the string
print(name[0]) # M

‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Negative Indexing ✥
# count the element from the end of the string.

# Print the last element in the string
print(name[-1]) # n

# Print the first element in the string
print(name[-15]) # M

# Find the length of string
len("Michael Jackson") # 15

‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Slicing ✥

# obtain multiple characters from a string using slicing

# Take the slice on variable name with only index 0 to index 3
name[0:4] # 'Mich'

# Take the slice on variable name with only index 8 to index 11
name[8:12] # 'Jack'

‗‗‗‗‗‗‗‗‗‗‗‗
✥ Stride ✥
name = "Michael Jackson"

# Get every second element. The elments on index 0, 2, 4 ...
name[::2] # 'McalJcsn'

# Get every second element in the range from index 0 to index 4
name[0:5:2] # 'Mca'

‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Concatenate Strings ✥

# Concatenate two strings

statement = name + "is the best"
statement # 'Michael Jacksonis the best'

# Print the string for 3 times
3 * "Michael Jackson"  # 'Michael JacksonMichael JacksonMichael Jackson'

_________________
# Concatenate strings
name = "Michael Jackson"
name = name + " is the best"
name # 'Michael Jackson is the best'

```

📓**Escape Sequences**
```python 
# \ represent the beginning of escape sequences

#\n  New line escape sequence
print(" Michael Jackson \n is the best" )

# Michael Jackson 
#  is the best

# \t Tab escape sequence
print(" Michael Jackson \t is the best" ) # Michael Jackson 	 is the best

# Include back slash in string
print(" Michael Jackson \\ is the best" ) # Michael Jackson \ is the best

# r will tell python that string will be display as raw string
print(r" Michael Jackson \ is the best" ) # Michael Jackson \ is the best

‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ String Manipulation Operations ✥

.upper() # Convert all the characters in string to upper case
a = "Thriller is the sixth studio album"
print("before upper:", a)
b = a.upper()
print("After upper:", b)

# before upper: Thriller is the sixth studio album
# After upper: THRILLER IS THE SIXTH STUDIO ALBUM
_________________

# Replace the old substring with the new target substring is the segment has been found in the string

a = "Michael Jackson is the best"
b = a.replace('Michael', 'Janet')
b
# 'Janet Jackson is the best'

_________________
# Find the substring in the string. Only the index of the first elment of substring in string will be the output

name = "Michael Jackson"
name.find('el') # 5

# If cannot find the substring in the string
name.find('Jasdfasdasdf') # -1 
_________________

#Split the substring into list at the specified separator
name = "Michael Jackson"
split_string = (name.split())
split_string
# ['Michael', 'Jackson']

```

📓**RegEx**
```python 
# RegEx (short for Regular Expression) is a tool for matching and handling strings.

# RegEx module provides several functions for working with regular expressions, including search(), split(), findall(), sub() 

search() # function searches for specified patterns within a string.

# re built-in module allows you to work with regular expressions

import re
s1 = "Michael Jackson is the best"

# Define the pattern to search for
pattern = r"Jackson"

# Use the search() function to search for the pattern in the string
result = re.search(pattern, s1)

# Check if a match was found
if result:
    print("Match found!")
else:
    print("Match not found.")

# Match found!
# (RegEx) are patterns used to match and manipulate strings of text.
# There are several special sequences in RegEx that can be used to match specific characters or patterns.

```
| Special Sequence | Meaning                 | 	Example             |
| -----------  | ----------------------- | ----------------------|
| \d|Matches any digit character (0-9)|"123" matches "\d\d\d"|
|\D|Matches any non-digit character|"hello" matches "\D\D\D\D\D"|
|\w|Matches any word character (a-z, A-Z, 0-9, and _)|"hello_world" matches "\w\w\w\w\w\w\w\w\w"|
|\W|Matches any non-word character|	"@#$%" matches "\W\W\W\W"|
|\s|Matches any whitespace character (space, tab, newline, etc.)|"hello world" matches "\w\s\w\w\w\w\w"|
|\S|Matches any non-whitespace character|"hello_world" matches "\S\S\S\S\S\S\S\S\S"|
|\b|Matches the boundary between a word character and a non-word character|"cat" matches "\bcat\b" in "The cat sat on the mat"|
|\B|Matches any position that is not a word boundary|"cat" matches "\Bcat\B" in "category" but not in "The cat sat on the mat"|


```python
pattern = r"\d\d\d\d\d\d\d\d\d\d"  # Matches any ten consecutive digits
text = "My Phone number is 1234567890"
match = re.search(pattern, text)

if match:
    print("Phone number found:", match.group())
else:
    print("No match")

# Phone number found: 1234567890

_________________
findall() # function finds all occurrences of a specified pattern within a string.

pattern = r"\W"  # Matches any non-word character
text = "Hello, world!"
matches = re.findall(pattern, text)

print("Matches:", matches)
Matches: [',', ' ', '!']
_________________
s2 = "Michael Jackson was a singer and known as the 'King of Pop'"

# Use the findall() function to find all occurrences of the "as" in the string
result = re.findall("as", s2)

# Print out the list of matched words
print(result) # ['as', 'as']

_________________
split() # function splits a string into an array of substrings based on a specified pattern.

s2 = "Michael Jackson was a singer and known as the 'King of Pop'"
# Use the split function to split the string by the "\s"
split_array = re.split("\s", s2)

# The split_array contains all the substrings, split by whitespace characters
print(split_array) 
# ['Michael', 'Jackson', 'was', 'a', 'singer', 'and', 'known', 'as', 'the', "'King", 'of', "Pop'"]

_________________
# Define the regular expression pattern to search for
pattern = r"King of Pop"

# Define the replacement string
replacement = "legend"

# Use the sub function to replace the pattern with the replacement string
new_string = re.sub(pattern, replacement, s2, flags=re.IGNORECASE)

# The new_string contains the original string with the pattern replaced by the replacement string
print(new_string) 
# Michael Jackson was a singer and known as the 'legend'
```


## W2 ❉ Python Data Structures
📓**Lists**
```python
# lists are versatile data structures that can hold a collection of items of different types. 
# They are mutable(changeable), ordered and allow duplicate elements.

# Creating a list
my_list = [1, 2, 3, 4, 5]
print(my_list)  # Output: [1, 2, 3, 4, 5]

‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Indexing Lists ✥

# Lists in Python are zero-indexed, meaning the first element is at index 0.

# Accessing elements in a list using indexing
print(my_list[0])  # Output: 1 (Accessing the first element)
print(my_list[2])  # Output: 3 (Accessing the third element)
print(my_list[-1]) # Output: 5 (Accessing the last element using negative indexing)
_________________
# Change the element based on the index
A = ["disco", 10, 1.2]
print('Before change:', A) # Before change: ['disco', 10, 1.2]
A[0] = 'hard rock'
print('After change:', A) # After change: ['hard rock', 10, 1.2]
_________________
# Delete the element based on the index
print('Before change:', A) # Before change: ['hard rock', 10, 1.2]
del(A[0])
print('After change:', A) # After change: [10, 1.2]
‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ List Content and Operations ✥

# Lists can contain different data type sand support various operations like appending, extending, slicing, etc.

# Lists with mixed data types and operations
mixed_list = [1, 'Hello', 3.14, True]
_________________
# Appending just one element to the list
mixed_list.append('World')
print(mixed_list)  # Output: [1, 'Hello', 3.14, True, 'World']
_________________
# Extending a list with another list
extension = [6, 7, 8]
mixed_list.extend(extension)
print(mixed_list)  # Output: [1, 'Hello', 3.14, True, 'World', 6, 7, 8]
_________________
# Slicing a list to get specific elements
sliced = mixed_list[2:5]
print(sliced)  # Output: [3.14, True, 'World']
_________________
# convert a string to a list using split
# Split the string, default is by space

'hard rock'.split() # ['hard', 'rock']
_________________
# Split the string by comma
'A,B,C,D'.split(',')  # ['A', 'B', 'C', 'D']

‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Copy and Clone List: ✥

# Copy (copy by reference) the list A
# A,B are referencing the same list in memory
A = ["hard rock", 10, 1.2]
B = A
print('A:', A) # A: ['hard rock', 10, 1.2]
print('B:', B) # B: ['hard rock', 10, 1.2]
_________________
# so if we change list A, then list B also changes.

# Examine the copy by reference

print('B[0]:', B[0]) # B[0]: hard rock
A[0] = "banana"
print('B[0]:', B[0]) # B[0]: banana
_________________
# Clone (clone by value) the list A

B = A[:]
B # ['banana', 10, 1.2]
# B references a new copy or clone of the original list.

# if you change A
# B will not change

print('B[0]:', B[0]) # B[0]: banana
A[0] = "hard rock"
print('B[0]:', B[0]) # B[0]: banana

```

📓**Tuples**
```python 
# immutable
# Create tuple

tuple1 = ("disco",10,1.2 )

‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Indexing ✥

# Each element of a tuple can be accessed via an index

# Print the variable of index 0
print(tuple1[0]) # disco

# Print the type of value of index 0
print(type(tuple1[0])) # <class 'str'>

# Use negative index to get the value of the last element
tuple1[-1] # 1.2

‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Concatenate Tuples ✥
# concatenate or combine tuples by using the + 

# Concatenate two tuples
tuple1 = ("disco",10,1.2 )
tuple2 = tuple1 + ("hard rock", 10)
tuple2 # ('disco', 10, 1.2, 'hard rock', 10)

‗‗‗‗‗‗‗‗‗‗‗‗
✥ Slicing ✥
# Slice from index 0 to index 2

tuple2[0:3] # ('disco', 10, 1.2)

# Get the length of tuple
len(tuple2) # 5

‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Sorting ✥

Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)
# sort the values in a tuple and save it to a new  List

# Sort the tuple
RatingsSorted = sorted(Ratings)
RatingsSorted  # [0, 2, 5, 6, 6, 8, 9, 9, 10]
‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Nested Tuple ✥
# tuple can contain another tuple as well as other more complex data types

# Create a nest tuple
NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))

# access the nested tuples:
print("Element 3 of Tuple: ", NestedT[3]) # Element 3 of Tuple:  (3, 4)

print("Element 3, 1 of Tuple: ",   NestedT[3][1]) # Element 3, 1 of Tuple:  4

```

📓**Dictionaries**
```python 
# dictionary consists of keys and values.
# Keys can only be strings, numbers, or tuples
# values can be any data type
# For every key, there can only be one single value, however, multiple keys can hold the same value

Dict_name={key:value}

# Create the dictionary
Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}

# Access to the value by the key
Dict["key1"] # 1
Dict[(0, 1)] # 6

‗‗‗‗‗‗‗‗‗
✥ Keys ✥

release_year_dict = {'Thriller': '1982',
 'Back in Black': '1980',
 'The Dark Side of the Moon': '1973',
 'The Bodyguard': '1992',
 'Bat Out of Hell': '1977',
 'Their Greatest Hits (1971-1975)': '1976',
 'Saturday Night Fever': '1977',
 'Rumours': '1977'}

# Get value by keys
release_year_dict['Thriller'] # '1982'

keys() # method to retrieve the keys of the dictionary 

# Get all the keys in dictionary
release_year_dict.keys() 

# dict_keys(['Thriller', 'Back in Black', 'The Dark Side of the Moon', 'The Bodyguard', 'Bat Out of Hell', 'Their Greatest Hits (1971-1975)', 'Saturday Night Fever', 'Rumours'])
_________________
values() # method to retrieve the values

# Get all the values in dictionary
release_year_dict.values() 
# dict_values(['1982', '1980', '1973', '1992', '1977', '1976', '1977', '1977'])

_________________
# Append value with key into dictionary
release_year_dict['Graduation'] = '2007'
_________________

# Delete entries by key
del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
_________________
# Verify the key is in the dictionary

'The Bodyguard' in release_year_dict  # True


```

📓**Sets**
```python 
# set is a unique collection of objects in Python remove duplicate items
# Create a set
set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
set1 # {'R&B', 'disco', 'hard rock', 'pop', 'rock', 'soul'}
_________________
# Convert list to set
album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19",
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)             
album_set # {'00:42:19', 10.0, 1982, '30-Nov-82', 46.0, 65, 'Michael Jackson',
#  None, 'Pop, Rock, R&B', 'Thriller'}

‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Set Operations ✥

A = set(["Thriller", "Back in Black", "AC/DC"])
A # {'AC/DC', 'Back in Black', 'Thriller'}

# Add element to set
A.add("NSYNC")
A # {'AC/DC', 'Back in Black', 'NSYNC', 'Thriller'}

# Try to add duplicate element to the set
A.add("NSYNC")
A # {'AC/DC', 'Back in Black', 'NSYNC', 'Thriller'}

_________________
# Remove the element from set
A.remove("NSYNC")
A # {'AC/DC', 'Back in Black', 'Thriller'}
_________________
# Verify if the element is in the set
"AC/DC" in A  # True

‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Sets Logic Operations ✥
# Sample Sets

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

# Print two sets
print(album_set1)# {'AC/DC', 'Back in Black', 'Thriller'}
print(album_set2) # {'AC/DC', 'Back in Black', 'The Dark Side of the Moon'}

# both sets contain AC/DC and Back in Black 
# find the intersect of two sets using &

# Find the intersections
intersection = album_set1 & album_set2
intersection # {'AC/DC', 'Back in Black'}

# only contained in album_set1 using the difference method:
# Find the difference in set1 but not set2
album_set1.difference(album_set2)  # {'Thriller'}

# elements in album_set2 but not in album_set1
album_set2.difference(album_set1)  


# Use intersection method to find the intersection of album_list1 and album_list2
album_set1.intersection(album_set2)   # {'AC/DC', 'Back in Black'}
_________________
# Find the union of two sets
album_set1.union(album_set2) # {'AC/DC', 'Back in Black', 'The Dark Side of the Moon', 'Thriller'}

_________________
# Check if superset

set(album_set1).issuperset(album_set2) # False 

# Check if subset
set(album_set2).issubset(album_set1) #  False

```

## W3 ❉ Python Programming Fundamentals
📓**Conditions and Branching**
```python 
‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Comparison Operators: ✥
# Comparison operators are used to compare values
# these operators return Boolean values (True / False) based on the comparison of operands.

# Equal to (==) operator
print(5 == 5)  # Output: True
print(5 == 6)  # Output: False

# Not equal to (!=) operator
print(5 != 6)  # Output: True
print(5 != 5)  # Output: False

# Greater than (>) operator
print(6 > 5)   # Output: True
print(5 > 6)   # Output: False

# Less than (<) operator
print(5 < 6)   # Output: True
print(6 < 5)   # Output: False

# Greater than or equal to (>=) operator
print(6 >= 5)  # Output: True
print(5 >= 6)  # Output: False

# Less than or equal to (<=) operator
print(5 <= 6)  # Output: True
print(6 <= 5)  # Output: False
‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Branching: ✥
 # Branching allows the program to execute different blocks of code based on specified conditions.

# If statement
x = 10
if x > 5:
    print("x is greater than 5")  # Output: x is greater than 5

# If-else statement
y = 4
if y % 2 == 0:
    print("y is even")
else:
    print("y is odd")  # Output: y is odd

# If-elif-else statement
z = 7
if z > 10:
    print("z is greater than 10")
elif z > 5:
    print("z is greater than 5 but not greater than 10")  # Output: z is greater than 5 but not greater than 10
else:
    print("z is 5 or less")

‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Logical Operators: ✥
# Logical operators are used to combine conditional statements. The logical operators in Python are (and - or - not )

# Using 'and' logical operator
a = 5
b = 10
if a > 0 and b > 0:
    print("Both a and b are positive")  # Output: Both a and b are positive

# Using 'or' logical operator
c = -3
d = 7
if c > 0 or d > 0:
    print("At least one of c or d is positive")  # Output: At least one of c or d is positive

# Using 'not' logical operator
e = True
if not e:
    print("e is False")
else:
    print("e is True")  # Output: e is True
```

📓**Loops**
```python 
‗‗‗‗‗‗‗‗‗‗‗‗
✥ Range: ✥
range() # built-in Python function used to generate a sequence of numbers

# Using range() to generate a sequence of numbers
for num in range(5):
    print(num)  # Output: 0 1 2 3 4

# Using range() with start and end parameters
for num in range(2, 6):
    print(num)  # Output: 2 3 4 5

# Using range() with a step value
for num in range(1, 10, 2):
    print(num)  # Output: 1 3 5 7 9

‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ for Loop: ✥

# for loop in Python is used to iterate over a sequence such as ( lists, tuples, strings, or the result of range())

# Iterating through a list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)  # Output: apple banana orange
_________________
# Iterating through a string
word = "Python"
for char in word:
    print(char)  # Output: P y t h o n
_________________
# Using a for loop to calculate the sum of numbers
numbers = [1, 2, 3, 4, 5]
sum_result = 0
for num in numbers:
    sum_result += num
print("Sum:", sum_result)  # Output: Sum: 15
_________________
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"At position {index}, I found a {fruit}")
# At position 0, I found a apple
# At position 1, I found a banana
# At position 2, I found a orange
‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ while Loop: ✥
# while loop in Python is used to execute a block of code repeatedly as long as the specified condition is True
_________________
# Using a while loop to print numbers from 1 to 5
count = 1
while count <= 5:
    print(count)  # Output: 1 2 3 4 5
    count += 1
_________________
# Using a while loop to find the factorial of a number
num = 5
factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print("Factorial:", factorial)  # Output: Factorial: 120

```

📓**Functions**
```python 
‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Functions: ✥
# Functions are blocks of reusable code that perform a specific task. They help in organizing code, making it more modular and easier to understand.

def function_name(parameters):
    """
    Function documentation (optional)
    """
    # Code block
    # Perform tasks
    return value(s)  # Optional return statement

# Define a function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

# Call the function with arguments
greet_person("Alice")  # Output: Hello, Alice!
greet_person("Bob")    # Output: Hello, Bob!

_________________
# Function to add two numbers and return the result
def add_numbers(a, b):
    sum_result = a + b
    return sum_result

# Call the function and store the result
result = add_numbers(5, 3)
print("Sum:", result)  # Output: Sum: 8

_________________
# Function with default parameter values
def greet_default(name="Guest"):
    print(f"Hello, {name}!")

# Call the function without providing an argument
greet_default()         # Output: Hello, Guest!
greet_default("Alice")  # Output: Hello, Alice!
_________________
# Function with variable number of arguments
def print_values(*args):
    for value in args:
        print(value)

# Call the function with different number of arguments
print_values(1, 2, 3)       # Output: 1 2 3
print_values('a', 'b')     # Output: a b

‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Predefined Functions: ✥
# Python has several built-in functions that perform various tasks.

# Using built-in functions
print(len("Python"))  # Output: 6 (returns the length of the string)
print(max(4, 8, 2))   # Output: 8 (returns the maximum value)
print(abs(-5))        # Output: 5 (returns the absolute value)
‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Using if/else Statements and Loops in Functions: ✥

# Function with if/else statement
def check_number(num):
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

check_number(7)   # Output: Positive
check_number(-3)  # Output: Negative
check_number(0)   # Output: Zero
_________________
# Function with loop
def print_numbers(n):
    for i in range(n):
        print(i, end=' ')
    print()

print_numbers(5)  # Output: 0 1 2 3 4

‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Global Variables: ✥
# Variables defined outside functions have a global scope, accessible from anywhere in the code. 
# Variables inside functions have local scope by default.

# Global variable
global_var = 10

def func():
    local_var = 5
    print("Inside func:", local_var)  # Output: Inside func: 5
    print("Inside func:", global_var) # Output: Inside func: 10

func()
print("Outside func:", global_var)   # Output: Outside func: 10
_________________
Scope of a Variable:

# Global variable
x = 10

def func():
    # Local variable
    x = 20
    print("Inside func:", x)  # Output: Inside func: 20

func()
print("Outside func:", x)    # Output: Outside func: 10
‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Collections and Functions: ✥
# Collections are data structures that can hold multiple items at once. They include lists, tuples, sets, and dictionaries. 
# Functions can accept these collections as arguments, allowing operations and manipulations on the data they contain.


# Function operating on a list
def process_list(my_list):
    for item in my_list:
        print(item, end=' ')
    print()

# Calling the function with a list argument
numbers = [1, 2, 3, 4, 5]
process_list(numbers)  # Output: 1 2 3 4 5

_________________
# Function operating on a tuple
def process_tuple(my_tuple):
    for item in my_tuple:
        print(item, end=' ')
    print()

# Calling the function with a tuple argument
fruits = ('apple', 'banana', 'orange')
process_tuple(fruits)  # Output: apple banana orange
_________________
# Function operating on a set
def process_set(my_set):
    for item in my_set:
        print(item, end=' ')
    print()

# Calling the function with a set argument
unique_numbers = {1, 2, 3, 4, 5}
process_set(unique_numbers)  # Output: 1 2 3 4 5
_________________
# Function operating on a dictionary
def process_dictionary(my_dict):
    for key, value in my_dict.items():
        print(f"Key: {key}, Value: {value}")

# Calling the function with a dictionary argument
student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
process_dictionary(student_grades)
# Output:
# Key: Alice, Value: 85
# Key: Bob, Value: 92
# Key: Charlie, Value: 78

```

📓**Exception Handling**

```python 
# Exception handling in Python involves managing and responding to errors or exceptional conditions that occur during program execution
# The try block contains the code that might raise an exception.
# If an exception occurs, the appropriate except block is executed based on the type of exception.
try:
    # Code block that may raise an exception
    #...
    #...
except SomeException as e:
    # Code to handle the exception
    #...
    #...
else:
    # Code to execute if no exceptions occur (optional)
    #...
    #...
finally:
    # Code that always executes, regardless of exceptions (optional)
    #...
    #...

_________________
# Handling a Specific Exception
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError as e:
    print("Error:", e)

_________________
# Handling Multiple Exceptions

try:
    file = open("nonexistent.txt", 'r')
    content = file.read()
    file.close()
except FileNotFoundError as e:
    print("File not found:", e)
except IOError as e:
    print("IO error:", e)
_________________
# Using 'else' Block
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError as e:
    print("Error:", e)
else:
    print("Result:", result)
_________________
# Using 'finally' Block
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError as e:
    print("Error:", e)
else:
    print("Result:", result)
finally:
    print("Execution complete.")
_________________
# Handling Any Exception
try:
    x = int('abc')
except Exception as e:
    print("An error occurred:", e)

```

📓**Creating a Class:**
```python 
# classes are used to create user-defined data structures that bundle data (attributes) and functions (methods) together. 
# Instances of classes are objects, which can be created based on the defined class.

__init__ # method serves as the constructor and is used to initialize the object's attributes when an instance is created.

# Objects (instances of classes) are created by calling the class name followed by parentheses containing any required arguments.

# Object attributes are accessed using dot notation (object.attribute)


class ClassName:
    """
    Class documentation (optional)
    """
    # Class attributes (variables shared by all instances)
    attribute = value

    # Constructor method (initializes object attributes)
    def __init__(self, parameter1, parameter2, ...):
        self.attribute1 = parameter1
        self.attribute2 = parameter2

    # Other methods (functions inside the class)
    def method_name(self, arguments):
        # Method body
        # Perform actions using self.attribute

‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Instances of a Class: Objects and Attributes: ✥

# Define a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create instances (objects) of the class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Accessing attributes of objects
print(person1.name, person1.age)  # Output: Alice 30
print(person2.name, person2.age)  # Output: Bob 25

‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Methods: ✥

# Methods are functions defined inside a class that can perform operations on object attributes.

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Car Make: {self.make}, Model: {self.model}")

# Create an instance of the class
car1 = Car("Toyota", "Corolla")

# Call a method of the object
car1.display_info()  # Output: Car Make: Toyota, Model: Corolla

```
## W4 ❉ Working With Data in Python
📓**Reading & Writing Files with Open**
```python 
# file handling involves reading and writing data to files. 
# The open() function is used to open files in different modes ('r' for reading, 'w' for writing, 'a' for appending)

# it automatically closes the file after operations are done (using the with statement)
with open('filename', 'r') as file:

‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Reading Files with open(): ✥

# Open file for reading
with open('filename.txt', 'r') as file:
    # Perform file reading operations
    content = file.read()
    # Use content or process data as needed

_________________

# Open a file in read mode
with open('sample.txt', 'r') as file:
    # Read the entire file contents
    content = file.read()
    print(content)

_________________
# Reading File Line by Line
# Open a file in read mode
with open('sample.txt', 'r') as file:
    # Read file line by line
    for line in file:
        print(line.strip())  # Strip newline character from each line

_________________
# Reading Fixed Number of Characters
# Open a file in read mode
with open('sample.txt', 'r') as file:
    # Read 10 characters from the file
    content = file.read(10)
    print(content)
_________________
# Reading Lines into a List

# Open a file in read mode
with open('sample.txt', 'r') as file:
    # Read lines into a list
    lines = file.readlines()
    for line in lines:
        print(line.strip())

‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Writing Files: ✥
# Writing to a file using 'w' mode creates a new file or overwrites an existing file.
# Appending to a file using 'a' mode appends content to the end of an existing file or creates a new file if it doesn't exist.
# Additional file modes ('r+', 'rb', 'wb', 'ab', 'x') provide different functionalities for reading, writing, and creating files.


# Open file for writing (creates a new file or overwrites existing file)
with open('filename.txt', 'w') as file:
    file.write("Content to be written\n")
    # Write additional content or perform writing operations

_________________
# Writing to a File
# Open a file in write mode
with open('output.txt', 'w') as file:
    file.write("Writing content to the file.")

‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Appending Files: ✥

# Open file for appending (creates a new file if it doesn't exist)
with open('filename.txt', 'a') as file:
    file.write("Content to be appended\n")
    # Append additional content or perform appending operations


_________________

# Open a file for reading and writing
with open('output.txt', 'r+') as file:
    content = file.read()
    file.write("\nAdditional content for writing.")

‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Copying a File ✥

# Open the source file in read mode
with open('source.txt', 'r') as source_file:
    # Read the content from the source file
    content = source_file.read()

    # Open the destination file in write mode
    with open('destination.txt', 'w') as destination_file:
        # Write the content to the destination file
        destination_file.write(content)


```

📓**Pandas**
```python 
# Pandas is a powerful library in Python for data manipulation and analysis.
# It provides versatile data structures like DataFrame and Series, along with numerous functions for data manipulation, cleaning, and analysis.

# Pandas introduces two key data structures: DataFrame and Series. The DataFrame represents tabular data, similar to a spreadsheet, while the Series is a one-dimensional labeled array. 
‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Pandas Basics: ✥

import pandas as pd

# Import pandas and check its version
print(pd.__version__)

‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Creating DataFrames: ✥
# Pandas DataFrame is a two-dimensional, labeled data structure with columns that can contain different types of data.



# Create a DataFrame from a dictionary
data = {'Column1': [value1, value2, value3],
        'Column2': [value4, value5, value6]}
df = pd.DataFrame(data)

_________________
import pandas as pd

# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print(df)
‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Creating a Series ✥

# Create a Series
s = pd.Series([value1, value2, value3])
_________________
import pandas as pd

# Creating a Series from a list
s = pd.Series([10, 20, 30, 40])
print(s)

0    10
1    20
2    30
3    40

‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Reading Data from Files: ✥


import pandas as pd

# Reading data from a CSV file into a DataFrame
df = pd.read_csv('data.csv')
print(df.head())  # Display the first few rows of the DataFrame


‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ DataFrame Attributes and Methods: ✥
# Pandas DataFrame has numerous attributes and methods to inspect and manipulate data.

# Shape of the DataFrame (rows, columns)
print(df.shape)

# Column names
print(df.columns)

# Summary statistics
print(df.describe())

# Accessing specific columns
print(df['Column1'])

_________________

loc() and iloc() # functions are used to locate and access data within a DataFrame.

# Using loc() to access data by label/index
df.loc[row_label, column_label]

# Using iloc() to access data by integer-based index
df.iloc[row_index, column_index]

# Accessing specific data using loc() and iloc()
print(df.loc[1, 'Name'])      # Output: Bob
print(df.iloc[2, 1])          # Output: 35
‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Slicing in DataFrames: ✥

# Slicing DataFrame using loc() or iloc()
df.loc[start_row_label:end_row_label, start_column_label:end_column_label]
df.iloc[start_row_index:end_row_index, start_column_index:end_column_index]

# Slicing rows and columns in a DataFrame
print(df.loc[0:1, 'Name'])          # Output: 0    Alice\n1      Bob
print(df.iloc[1:3, 0:1])            # Output:     Name\n1   Bob\n2 Charlie

```

📓**NumPy in Python**
```python 
# NumPy is a fundamental library in Python for numerical computations, providing support for multi-dimensional arrays and various mathematical operations.


import numpy as np

# Print NumPy version
print(np.__version__)

‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Data Types in NumPy: ✥
# NumPy supports various data types, such as integers, floats, and complex numbers, among others.



import numpy as np

# Define NumPy array with a specific data type
arr_int = np.array([1, 2, 3], dtype=np.int32)
arr_float = np.array([1.5, 2.5, 3.5], dtype=np.float64)
arr_complex = np.array([1 + 2j, 3 + 4j], dtype=np.complex128)

print(arr_int.dtype)      # Output: int32
print(arr_float.dtype)    # Output: float64
print(arr_complex.dtype)  # Output: complex128
type(arr_int)# numpy.ndarray (the type of the array)

‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ ssigning Values in NumPy Arrays: ✥

import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Assign a new value to an element
arr[2] = 10
print(arr)  # Output: [ 1  2 10  4  5]

‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Slicing Arrays in NumPy: ✥
# Slicing is used to extract specific portions of NumPy arrays.

import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Slice the array to extract a subset
subset = arr[1:4]
print(subset)  # Output: [2 3 4]

‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Assigning Values with List in NumPy Arrays: ✥

# Values can be assigned using a list to specific elements or slices of NumPy arrays.

import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Assign values using a list to a slice of the array
arr[1:4] = [10, 20, 30]
print(arr)  # Output: [ 1 10 20 30  5]

‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Other NumPy Array Attributes: ✥
# NumPy arrays have various attributes like shape, size, ndim, etc.

import numpy as np

# Create a NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# shape attribute returns a tuple indicating the dimensions of the array
print(arr.shape)     # Output: (2, 3)

# size attribute returns the total number of elements in the array
print(arr.size)      # Output: 6

# ndim attribute returns the number of dimensions (axes) in the array.
print(arr.ndim)      # Output: 2 (number of dimensions)

# dtype attribute returns the data type of the elements in the array
print(arr.dtype)     # Output: int64 (data type)

# itemsize attribute returns the size (in bytes) of each element in the array.
print(arr.itemsize)  # Output: 8 (size of each element in bytes)


‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Statistical Functions in NumPy: ✥

The np.mean()# function computes the arithmetic mean along a specified axis.

import numpy as np

# Create a NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Calculate mean of the entire array
mean_all = np.mean(arr)
print("Mean of the entire array:", mean_all)  # Output: Mean of the entire array: 3.5
_________________
np.median() # function computes the median along a specified axis.

import numpy as np

# Create a NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Calculate median along the specified axis (axis=None for the flattened array)
median_all = np.median(arr)
print("Median of the entire array:", median_all)  # Output: Median of the entire array: 3.5

_________________
 np.std() # function computes the standard deviation along a specified axis.

import numpy as np

# Create a NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Calculate standard deviation along the specified axis (axis=None for the flattened array)
std_all = np.std(arr)
print("Standard deviation of the entire array:", std_all)  # Output: Standard deviation of the entire array: 1.707825127659933
_________________

np.var() # function computes the variance along a specified axis.
import numpy as np

# Create a NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Calculate variance along the specified axis (axis=None for the flattened array)
var_all = np.var(arr)
print("Variance of the entire array:", var_all)  # Output: Variance of the entire array: 2.9166666666666665
_________________
np.corrcoef() # function computes the correlation coefficient matrix.

import numpy as np

# Create two NumPy arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([5, 4, 3, 2, 1])

# Compute correlation coefficient between arr1 and arr2
corr_coef = np.corrcoef(arr1, arr2)
print("Correlation coefficient matrix:")
print(corr_coef)
# Output:
# Correlation coefficient matrix:
# [[ 1. -1.]
#  [-1.  1.]]

‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ Numpy Array Operations ✥
# NumPy arrays support a wide range of mathematical and arithmetic operations, including element-wise operations, mathematical functions, aggregation functions, broadcasting, and more.

_________________
# Element-wise Operations:

import numpy as np

# Create two NumPy arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Perform element-wise addition, subtraction, multiplication, division
addition = arr1 + arr2
subtraction = arr1 - arr2
multiplication = arr1 * arr2
division = arr1 / arr2

print("Addition:", addition)           # Output: Addition: [5 7 9]
print("Subtraction:", subtraction)     # Output: Subtraction: [-3 -3 -3]
print("Multiplication:", multiplication) # Output: Multiplication: [ 4 10 18]
print("Division:", division)           # Output: Division: [0.25 0.4  0.5 ]
_________________
# Mathematical Functions:

import numpy as np

# Create a NumPy array
arr = np.array([1, 4, 9])

# Square root, exponential, sine, cosine
sqrt_arr = np.sqrt(arr)
exp_arr = np.exp(arr)
sin_arr = np.sin(arr)
cos_arr = np.cos(arr)

print("Square Root:", sqrt_arr)   # Output: Square Root: [1. 2. 3.]
print("Exponential:", exp_arr)    # Output: Exponential: [2.71828183e+00 5.45981500e+01 8.10308393e+03]
print("Sine:", sin_arr)          # Output: Sine: [ 0.84147098 -0.7568025   0.41211849]
print("Cosine:", cos_arr)        # Output: Cosine: [ 0.54030231 -0.65364362 -0.91113026]

_________________
# Aggregation Functions:

import numpy as np

# Create a NumPy array
arr = np.array([2, 4, 6, 8])

# Compute sum, minimum, maximum
arr_sum = np.sum(arr)
arr_min = np.min(arr)
arr_max = np.max(arr)

print("Sum:", arr_sum)    # Output: Sum: 20
print("Minimum:", arr_min) # Output: Minimum: 2
print("Maximum:", arr_max) # Output: Maximum: 8

_________________
# Broadcasting:
import numpy as np

# Create a NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Perform scalar addition using broadcasting
result = arr + 10

print("Result:", result)
# Output:
# Result: [[11 12 13]
#          [14 15 16]]

_________________
X = np.array([1, 2])
Y = np.array([3, 2])
# Calculate the dot product

np.dot(X, Y) # 7
```

## W5 ❉ APIs ,and Data Collection
📓**simple APIs**

**API connection** 
**API (Application Programming Interface)**

API acts as a bridge that allows one software application to interact with another

 
 **Endpoint**: specific URL or URI (Uniform Resource Identifier) that represents a specific function or resource in the API. Each endpoint corresponds to a particular operation that the API can perform.

 **Request Methods (HTTP Methods):**

- APIs use HTTP methods to specify the type of action the client wants to perform on a given resource. Common HTTP methods include:
    - **GET**: Retrieve data from the server.
    - **POST**: Send data to the server to create a new resource.
    - **PUT or PATCH**: Update an existing resource on the server.
    - **DELETE**: Remove a resource on the server.


**Request Headers:**
Headers contain additional information about the request, such as the content type, authentication tokens, or other metadata.

**Request Body:**
In some cases, a request may include a body that contains data to be sent to the server. This is common in POST or PUT requests, where the client is sending data to create or update a resource.


**Response Status Code:**
The server responds to a client request with an HTTP status code, indicating the success or failure of the operation.
![[Pasted image 20231213170146.png]]

 **Authentication:**

Many APIs require authentication to ensure that only authorized users or applications can access certain resources. This can be done using API keys, OAuth tokens, or other authentication mechanisms.

*Documentation*:
Good API design includes comprehensive documentation that explains how to use the API, the available endpoints, request and response formats, and any authentication requirements. This documentation helps developers understand and integrate with the API effectively.

*Structure of API URL*
![[Pasted image 20231213194007.png]]

**URI (Uniform Resource Identifier):** identifies name or a resource on the internet.

**URL (Uniform Resource Locator):**
The URL is a specific type of URI that provides the means to access a resource on the web.  


**Scheme:**
The protocol is specified at the beginning of the URL as **https://**, indicating that the communication should be secured using the HTTPS protocol.

**Route:**
This is the location on the web server; for example: /v1/get/json.xml


**API vs RESTAPI:**
API (Application Programming Interface) and REST API (Representational State Transfer API) are related terms, but there are distinctions between them.

|Feature|API|Rest API|
|---|---|---|
|Full form|Application Programming Interface|Representational State Transfer API|
|Definition|An API is a set of protocols and tools for building software applications. It defines how different software components should interact.|REST API is a specific type of web API that follows the principles of Representational State Transfer (REST). It is an architectural style for designing networked applications.|
|Scope|API is a broader term encompassing various types of interfaces.|REST API specifically refers to APIs following the principles of REST architecture.|
|Communication|API communication methods can vary.(e.g., RPC, SOAP, etc.)|REST API uses standard HTTP methods (GET, POST, PUT, DELETE) for communication.|
|Architectural Style|Does not necessarily adhere to a specific architectural style|Follows the REST architectural style|
|Data Format|Can use different data formats (e.g., JSON, XML, etc.)|Typically uses lightweight data formats, commonly JSON, for data exchange|
|URI|Resource identification methods may vary|Resources identified by URIs, each with multiple representations|
|Usage|Used in various contexts (web development, libraries, operating systems, etc.)|Primarily used for web services and web-based applications|

For example, to retrieve data from the FishWatch API, you can use the following code:

```python
# Import the requests and json modules for making HTTP requests and handling JSON data, respectively.
import requests
import json

# Specify the URL of the API endpoint for retrieving information about fish species.
url = "https://www.fishwatch.gov/api/species"

# Make an HTTP GET request to the specified URL and store the response in the data variable.
data = requests.get(url)

# Parse the JSON data received from the API response using json.loads() and store it in the results variable.
results = json.loads(data.text)

```

📓**REST APIs, Webscraping, and Working with Files**
Certainly! Here's an in-depth explanation of each topic you requested, structured in bullet points:

**Overview of HTTP:**

- **Hypertext Transfer Protocol (HTTP):** It is a protocol used for transferring hypertext requests and information on the World Wide Web.

- **Client-Server Model:** Operates on a client-server model where a client sends a request to a server, and the server responds with the requested resources.

- **Stateless Protocol:** HTTP is stateless, meaning each request from a client to a server is independent and not reliant on previous requests.
---
- **Methods:** HTTP defines various methods, including:

  - **GET:** Retrieves data from a specified resource.
  - **POST:** Sends data to a server to create/update a resource.
  - **PUT:** Updates a resource on the server.
  - **DELETE:** Removes a resource from the server.
  - **HEAD:** Similar to GET but retrieves response headers only without the body.
  - **OPTIONS:** Requests information about the communication options available for a resource.
---
- **Status Codes:** Responses from the server include status codes indicating the outcome of the request, such as:
  - **2xx:** Success (e.g., 200 OK).
  - **3xx:** Redirection (e.g., 301 Moved Permanently).
  - **4xx:** Client errors (e.g., 404 Not Found).
  - **5xx:** Server errors (e.g., 500 Internal Server Error).
---
**Uniform Resource Locator (URL):**

- **Definition:** A URL is a specific type of Uniform Resource Identifier (URI) that provides the means to access a resource on the internet.
- **Structure:** It comprises several parts:
  - **Scheme:** Indicates the protocol used (e.g., HTTP, HTTPS, FTP).
  - **Domain:** Identifies the server hosting the resource (e.g., www.example.com).
  - **Path:** Specifies the location of the resource on the server (/path/to/resource).
  - **Port:** Optional and specifies the communication endpoint on the server.
  - **Query Parameters:** Additional data passed in the URL's query string (?key=value&key2=value2).
---
**Request:**

- **HTTP Request:** Sent by a client to request data or actions from a server.
- **Components of a Request:**
  - **HTTP Method:** Specifies the action to be performed (GET, POST, PUT, DELETE, etc.).
  - **Headers:** Contain additional information about the request (content type, authentication, etc.).
  - **Body:** Holds data (optional) to be sent to the server, often used in POST or PUT requests.
---
**Response:**

- **HTTP Response:** Sent by the server in reply to a client's request.
- **Components of a Response:**
  - **Status Code:** Indicates the outcome of the request (success, redirection, client/server error).
  - **Headers:** Provide additional information about the response (content type, server type, caching instructions, etc.).
  - **Body:** Contains the requested resource's data, such as HTML content, JSON, images, etc.

Each of these elements plays a crucial role in the communication between clients and servers over the web, ensuring the exchange of information through standardized protocols and structures.

---
explanation of Requests in Python, including GET Requests with URL Parameters and POST Requests, with examples and comments:

```python
import requests  # Importing the requests library

# GET Request with URL Parameters

# Example 1: Sending a simple GET request to retrieve data
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
# The URL above fetches a specific post with ID 1 from a JSONPlaceholder API

print(response.status_code)  # Print the status code of the response (200 for success)
print(response.json())  # Print the JSON response content (in this case, the post data)
_________________
# Example 2: Sending a GET request with URL parameters
# We'll pass parameters to the API to filter or modify the response
url = 'https://jsonplaceholder.typicode.com/comments'
params = {'postId': 1, 'id': 5}  # Filtering comments for post ID 1 and comment ID 5

response = requests.get(url, params)
print(response.url)  # Print the final URL with parameters
print(response.json())  # Print the JSON response content (comments filtered by parameters)

‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
✥ POST Requests ✥


# Example 1: Sending a simple POST request with JSON data
url = 'https://jsonplaceholder.typicode.com/posts'
data = {'title': 'foo', 'body': 'bar', 'userId': 1}

response = requests.post(url, json=data)  # Sending JSON data in the request
print(response.status_code)  # Print the status code of the response (201 for resource created)
print(response.json())  # Print the JSON response content (the newly created post)
_________________
# Example 2: Sending a POST request with form data

url = 'https://httpbin.org/post'
data = {'key1': 'value1', 'key2': 'value2'}  # Form data to be sent

response = requests.post(url, data=data)  # Sending form data in the request
print(response.json())  # Print the JSON response content (HTTPBin response displaying form data)
_________________
# Example 3: Sending a POST request with headers
url = 'https://httpbin.org/post'
data = {'key': 'value'}  # Form data to be sent
headers = {'Content-Type': 'application/json'}  # Custom headers

response = requests.post(url, data=data, headers=headers)  # Sending form data with custom headers
print(response.json())  # Print the JSON response content (HTTPBin response with custom headers)
_________________
# Example 4: Sending a POST request with file upload
url = 'https://httpbin.org/post'
files = {'file': open('file.txt', 'rb')}  # Open a file for uploading

response = requests.post(url, files=files)  # Sending a POST request with file
print(response.json())  # Print the JSON response content (HTTPBin response showing uploaded file details)

```

