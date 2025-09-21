# Odd or Even
# Write a Python program that asks the user to enter a number and checks if the
# number is odd or even.
# Note: Use the modulus operator and an if statement.

# Example of expected output:
# ---------------------------
# Enter a number: 4
# The number is even.
# ---------------------------

# Write your code below this line

value = input("Enter a number:")
if (int(value) % 2) == 0:
  print("The number is even")
else:
  print("the number is odd")

# Compare Two Numbers
# Write a Python program that takes two numbers as input and prints whether:
# - The first number is greater than the second
# - The second number is greater than the first
# - The two numbers are equal

# Example of expected output:
# ---------------------------
# Enter the first number: 10
# Enter the second number: 20
# The second number is greater than the first
# ---------------------------

# Write your code below this line

first_value = input("Enter the first number:")
second_value = input("Enter the second number:")
if int(first_value) > int(second_value):
  print("The first number is greater than the second")
else:
  print("The second number is greater than the first")

# FizzBuzz
# Write a Python program that prints the numbers from 1 to 20.
# But for multiples of 3, print "Fizz" instead of the number,
# and for multiples of 5, print "Buzz".
# For numbers which are multiples of both 3 and 5, print "FizzBuzz".

# Example output:
# ---------------------------
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# 16
# 17
# Fizz
# 19
# Buzz
# ---------------------------

# Write your code below this line

for number in range(1, 21):
  if (number % 3 == 0) and (number % 5 == 0):
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
