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

# Multiplication Table
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

