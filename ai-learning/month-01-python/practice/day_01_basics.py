"""Day 1 practice: Python basics, strings, operators, conditions and loops."""

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
