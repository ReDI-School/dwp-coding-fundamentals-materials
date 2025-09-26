# Coding exercises using FOR loop
"""
You're building a simple fitness tracking tool. You want to calculate the total steps you walked over a week using a for loop.
1. Loop through the list and print how many steps you walked each day.
2. Calculate the total number of steps walked in the week using a for loop.
3. Calculate the average steps per day.
4. Print a motivational message for each day where you walked more than 7,000 steps:
Example output: "Great job on Wednesday! You walked 8100 steps!"
(Assume the first day in the list is Monday)
"""

# Steps for each day of the week
daily_steps = [3450, 6890, 7450, 8100, 10200, 4600, 5900]

# Create a list to store the days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# 1. Loop through the list and print how many steps you walked each day.
for i in range(len(daily_steps)): # Loop through the list
    print(f"{days[i]}: {daily_steps[i]} steps") # Use the index to print the day and the corresponding steps

# 2. Calculate the total number of steps walked in the week using a for loop.
total_steps = 0 # Start with an initial value of 0

for steps in daily_steps: # Loop through each day's step count
    total_steps += steps # Add to the running total

print(f"\nTotal steps this week: {total_steps}") # Print the total steps after the loop

# 3. Calculate the average steps per day.
average_steps = total_steps / len(daily_steps)  # Divide total steps by the number of days to get the average
print(f"Average steps per day: {average_steps}")

# 4. Print a motivational message for each day where you walked more than 7,000 steps:
## Example output: "Great job on Wednesday! You walked 8100 steps!"

for i in range(len(daily_steps)):
    if daily_steps[i] > 7000: # Check if the steps for the day are more than 7000
        print(f"Great job on {days[i]}! You walked {daily_steps[i]} steps!")
