# 1 Modulus and Exponentiation
# Write a Python program that takes a number from the user and prints:
# 1. The remainder when divided by 3 (using the modulus operator %)
# 2. The number raised to the power of 2 (using the exponentiation operator **)
# Note: remember, the input function returns a string type

# Example of expected output:
# ---------------------------
# Enter a number: 7
# Remainder when divided by 3: 1
# Number raised to the power of 2: 49
# ---------------------------

# Write your code below this line

value = input("Please enter a number:")
print("Remainder when divided by 3:", int(value) % 3)
print("Number raised to the power of 2:", int(value) ** 2 )

# 2. Odd or Even
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

# 3. Compare Two Numbers
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

# 4. Print Numbers 1 to 10
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

# 5. Multiplication Table
# Write a Python program that takes a number from the user and prints the multiplication table (from 1 to 10) for that number.

# Example Output:
# ---------------------------
# Enter a number: 3
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12
# 3 x 5 = 15
# 3 x 6 = 18
# 3 x 7 = 21
# 3 x 8 = 24
# 3 x 9 = 27
# 3 x 10 = 30
# ---------------------------

# Write your code below this line

number = input("Enter a number:")
for value in range(1, 11):
  print(number, 'x', value, '=', int(number)*value)

# BONUS. FizzBuzz
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
