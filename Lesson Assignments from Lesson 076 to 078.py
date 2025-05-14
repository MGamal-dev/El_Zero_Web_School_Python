# ==========================
# Assignments from Lesson 76 to 78
# Source: https://elzero.org/python-assignments-lesson-from-76-to-78/
# ==========================

# ========================== Assignment 1 ==========================
# Generate random numbers using the random module

import random

# Generate a random integer between 10 and 50 (inclusive)
random_num = random.randint(10, 50)

# Generate a random even number between 2 and 10 (step 2 ensures even numbers)
random_even_num = random.randrange(2, 10, 2)

# Generate a random odd number between 1 and 9 (step 2 ensures odd numbers)
random_odd_num = random.randrange(1, 9, 2)

# Print the generated random numbers with descriptive messages
print(f"Random Number Between 10 And 50 => {random_num}")
print(f"Random Even Number Between 2 And 10 => {random_even_num}")
print(f"Random Odd Number Between 1 And 9 => {random_odd_num}")

# Print all attributes and methods available in the random module
print(dir(random))
