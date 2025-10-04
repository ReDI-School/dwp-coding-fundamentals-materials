# Coding exercises using Lists
"""
You’ve made a weekend to-do list in Python, but it needs a little organizing. Use list operations to solve this exercise.

1. "watch Netflix" isn’t very productive. Replace it with "read a book".
2. You already called your mom. Remove "call mom" from the list.
3. Add "meal prep" and "take a walk" to the end of the list.
4. Move "laundry" to the end of the list (Hint: remove it first, then append it.).
5. Insert "meditate" at the beginning of the list.
6. Create a new list called top_3 that contains the first three tasks from the updated todo list.
"""

# My weekend to-do list
todo = ["laundry", "grocery shopping", "call mom", "watch Netflix", "clean kitchen", "nap"]

# 1. Replace "watch Netflix" with "read a book"
index_netflix = todo.index("watch Netflix")  # Find the index of "watch Netflix"
todo[index_netflix] = "read a book"          # Assign a new value ("read a book") at the index of "watch Netflix" (index_netfilx). 

# 2. Remove "call mom" from the list
todo.remove("call mom")  # Remove the first occurrence of "call mom"

# 3. Add "meal prep" and "take a walk" to the end of the list
todo.append("meal prep")
todo.append("take a walk")

# 4. Move "laundry" to the end of the list
todo.remove("laundry")   # Remove "laundry" from its current position
todo.append("laundry")   # Add it to the end of the list

# 5. Insert "meditate" at the beginning of the list
todo.insert(0, "meditate")  # Insert at index 0

# 6. Create a new list called top_3 with the first three tasks
top_3 = todo[:3]  # Slice the first three items from the updated list

# Print final lists for verification
print("Updated To-Do List:", todo)
print("Top 3 Tasks:", top_3)
