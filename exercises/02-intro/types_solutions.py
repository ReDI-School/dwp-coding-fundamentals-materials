"""
Solution to Types Practice Exercise 1:
"""

my_int = 10
my_float = 3.14
my_str = "Hello, world!"

print(my_int, type(my_int))
print(my_float, type(my_float))
print(my_str, type(my_str))

"""
Solution to Exercise 2: Type Conversion
"""

num_str = "123"
num_int = int(num_str)
print(num_int, type(num_int))

"""
Solution to Exercise 3: Type Checking
"""

value = 7.5
if type(value) == float:
	print("It's a float!")