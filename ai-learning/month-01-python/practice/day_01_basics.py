"""Day 1 practice: Python basics, strings, operators, conditions and loops."""

from math import sqrt  # Importing the sqrt function from the math module

print('Hello World!', 'How are you?')
print('I am fine, thank you!' + ' How about you?')
# name = input('What is your name? ')
name = 'John'
print('Hello ' + name + ', nice to meet you!')
age = 18
print('type of name variable is: ', type(name), 'and type of age variable is: ', type(age))
weight = '70.5'
total_weight = float(weight) + 5.5
print('Total weight is: ', total_weight)

# Optional practice: add two subject marks
# maths_marks = int(input('Enter your Maths marks: '))
# science_marks = int(input('Enter your Science marks: '))
# total_marks = maths_marks + science_marks
# print('Total marks is: ', total_marks)


# String operations
# Built-in function: len(); string methods: upper(), lower(), title(), count(), find(), replace().
example_text = 'Hello World! Welcome to Python Programming.'  # Immutable string
print('Length of example_text is: ', len(example_text))
print('Uppercase of example_text is: ', example_text.upper())
print('Lowercase of example_text is: ', example_text.lower())
print('Title case of example_text is: ', example_text.title())
print('Count of "o" in example_text is: ', example_text.count('o'))
print('Index of "Python" in example_text is: ', example_text.find('Python'))
updated_text = example_text.replace('Python', 'Java')
print('New string after replacement is: ', updated_text)
print('Slicing example_text from index 0 to 5: ', example_text[0:5])

# Check whether a substring is present
print('Is "Hello" present in example_text? ', 'Hello' in example_text)
print(9 / 4)  # Division
print(9 // 4)  # Floor Division
print(9 % 4)  # Modulus
print(9 ** 4)  # Exponentiation

# Operator precedence (arithmetic operators shown below)
# 1. Parentheses ()
# 2. Exponentiation **
# 3. Multiplication *, Division /, Floor Division //, Modulus %
# 4. Addition +, Subtraction -
# Example of precedence
result = 2 + 3 * 4
print('Result of 2 + 3 * 4 is: ', result)

# Logical Operators: and, or, not
is_adult = True
has_id = False
if is_adult and has_id:
    print('You can enter the club.')
    # Remember to use indentation in Python, it is very important.
else:
    print('You cannot enter the club.')
print('This is outside the if block.')

print(not False)  # True

basic_range = range(5)  # range(start, stop, step)
print('Range example: ', basic_range)
# Custom range: start is included; stop is excluded.
stepped_range = range(1, 10, 2)  # Values from 1 up to, but not including, 10, with a step of 2.
print('Custom range example: ', stepped_range)
odd_numbers = list(range(1, 10, 2))  # convert range to list
print('List example from range: ', odd_numbers)

# Loops examples
# While loop
count = 0
while count < 5:
    print('Count is: ', count)
    count += 1  # increment count by 1

# Star pattern printing
star_count = 1
while star_count < 5:
    print('*' * star_count)
    star_count += 1

# For loop
for number in range(5):
    print('Value of number is: ', number)

for number in range(1, 5):
    print('Value of number is: ', number)

# Loop control: break, continue and else
for number in range(1, 10):
    if number == 5:
        print('Breaking the loop at number = ', number)
        break
    elif number == 3:
        print('Skipping the iteration at number = ', number)
        continue
    print('Value of number is: ', number)
else:
    print('This is else block of for loop, it will execute only if the loop is not broken.')

 # List example
fruits = ['apple', 'banana', 'cherry', 'date']
print('List of fruits: ', fruits)
print('First fruit is: ', fruits[0])
print('last index fruit is: ', fruits[-1])
print('second last index fruit is: ', fruits[-2])   
#fruits.append('elderberry')  # Add an item to the end of the list
#slicing a list
# The slicing syntax is [start:stop:step]:
print('Sliced list of fruits from index 1 to 3: ', fruits[1:4])  # Slicing from index 1 to 3 (4 is excluded)
print('Sliced list of fruits from index 2 to end: ', fruits[2:])  # Slicing from index 2 to end
print('Sliced list of fruits from index 2 to end: ', fruits[2:5])  # Slicing from index 2 to end
# Leaving start and stop empty means the slice spans the whole list.
print('Reversed list: ', fruits[::-1])
# 2. Print each element one by one in reverse
for fruit in fruits[::-1]: {
    print(fruit)
}

studentNames = ['Alice', 'Bob', 'Charlie', 'David']  
print('current list of studentNames: ', studentNames)
print('Reversed studentNames: ', studentNames[3:1:-1])
"""
Quick Cheat-Sheet
fruits[start : stop]         # Forward from start to stop - 1
fruits[start :]              # From start to the end
fruits[: stop]               # From start of list to stop - 1
fruits[start : stop : step]  # With a custom step
fruits[::-1]                 # Entire list reversed
"""
print(studentNames[1:3])  # Forward from index 1 to 2
print(studentNames[1:])   # From index 1 to the end
print(studentNames[:3])   # From start to index 2   
print(studentNames[1:3:1])  # From index 1 to 2 with a step of 1
print(studentNames[::-1])  # Entire list reversed

#Tuple example
studentMarks = (85, 90, 78, 92)  # Immutable tuple
print('Tuple of studentMarks: ', studentMarks)
print('First student mark is: ', studentMarks[0])
print('Last student mark is: ', studentMarks[-1])

# Set example
studentSubjects = {'Maths', 'Science', 'English', 'History', 'Maths'}  # Unordered collection of unique elements
print('Set of studentSubjects: ', studentSubjects)
# studentSubjects.add('Geography')  # Add an element to the set
# print('Updated set of studentSubjects: ', studentSubjects)
print('Length of studentSubjects set is: ', len(studentSubjects))
# Dictionary example
studentInfo = {'name': 'Alice', 'age': 20, 'grade': 'A'}  # Key-value pairs
print('Dictionary of studentInfo: ', studentInfo)
print('Student name is: ', studentInfo['name'])
print('Student age is: ', studentInfo['age'])
print('Student grade is: ', studentInfo['grade'])
for key, value in studentInfo.items():
    print(f'{key}: {value}')# f is used for string formatting in Python. It allows you to embed expressions inside string literals, using curly braces {}. The expressions are evaluated at runtime and then formatted using the format() protocol.
    print(key, value)

# Functions example
def greet(name):
    """Function to greet a person by name."""
    return f'Hello {name}, nice to meet you!'

print(greet('Alice'))

# Sum function example
def sum_numbers(a, b):
    """Function to return the sum of two numbers."""
    return a + b    
sum_result = sum_numbers(5, 10)
print('Sum of 5 and 10 is: ', sum_result)
print('square root of 16 is: ', sqrt(16))  # Using the sqrt function from the math module
