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

# Print Numbers 1 to 10
# Write a Python program that uses a while loop to print the numbers from
# 1 to 10.

# Example of expected output:
# ---------------------------
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# ---------------------------

# Write your code below this line

value = 1
while value <= 10:
  print(value)
  value += 1

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

