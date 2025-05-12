# ==========================
# Assignments from Lesson 72 to 75
# Source: https://elzero.org/python-assignments-lesson-from-72-to-75/
# ==========================

# ========================== Assignment 01 ==========================
# Remove the first and last character from each string in the list using map

def remove_first_last_char(s):
    return s[1:-1]

friends_list = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

# Using map with a named function
cleaned_names = map(remove_first_last_char, friends_list)
print("Using map with named function:")
for name in cleaned_names:
    print(name)

print("#" * 50)

# Using map with a lambda function
print("Using map with lambda function:")
for name in map(lambda s: s[1:-1], friends_list):
    print(name)


# ========================== Assignment 02 ==========================
# Filter names that end with the letter 'm'

def ends_with_m(name):
    return name[-1] == "m"

friends_names = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

# Using filter with a named function
filtered_names = filter(ends_with_m, friends_names)
print("\nFiltered names ending with 'm' (named function):")
for name in filtered_names:
    print(name)

print("#" * 50)

# Using filter with a lambda function
print("Filtered names ending with 'm' (lambda function):")
for name in filter(lambda n: n[-1] == "m", friends_names):
    print(name)


# ========================== Assignment 03 ==========================
# Use reduce to multiply all numbers in the list

from functools import reduce

def multiply(x, y):
    return x * y

numbers = [2, 4, 6, 2]

# Using reduce with a named function
product_result = reduce(multiply, numbers)
print("\nProduct using reduce with named function:", product_result)

print("#" * 50)

# Using reduce with a lambda function
product_lambda = reduce(lambda x, y: x * y, numbers)
print("Product using reduce with lambda function:", product_lambda)


# ========================== Assignment 04 ==========================
# Enumerate reversed skills starting from 50, skipping integers

skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

enumerated_skills = enumerate(reversed(skills), 50)

print("\nEnumerated skills (excluding integers):")
for index, skill in enumerated_skills:
    if isinstance(skill, int):
        continue
    print(f"{index} - {skill}")
