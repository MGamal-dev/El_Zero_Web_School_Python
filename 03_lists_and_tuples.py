# 03_lists_and_tuples.py
# Working with lists and tuples

# List indexing and slicing
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[0])      # First element
print(friends[4])      # Last element
print(friends[-1])     # Last element (negative index)
print(friends[-5])     # First element (negative index)

print(friends[::2])    # Every other element
print(friends[1::2])   # Every other element starting from index 1

print(friends[1:4])    # Slice from index 1 to 3
print(friends[3:5])    # Slice from index 3 to 4

# List append and insert
friends.append("Elzero")
print(friends)

friends = ["Osama", "Ahmed", "Sayed"]
friends.insert(0, "Nasser")
print(friends)
friends.append("Sayed")

# List extend
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
friends.extend(employees)
friends.extend(school)
print(friends)

# List sorting
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)

# List length
print(len(friends))

# Nested lists
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[4][0])  # Django
print(technologies[4][-1]) # Web

# Tuple operations
name = ("osama",)
print(name[0])
print(type(name))

friends = ("Osama", "Ahmed", "Sayed")
friends = ("Elzero",) + friends[-2:]
print(friends)
print(type(friends))
print(len(friends))

# Tuple concatenation
nums = (1, 2, 3)
letters = ("A", "B", "C")
x = nums + letters
print(x)
print(len(x))

# Tuple unpacking
my_tuple = (1, 2, 3, 4)
a, b, _, c = my_tuple
print(a, "\n", b, "\n", c)
