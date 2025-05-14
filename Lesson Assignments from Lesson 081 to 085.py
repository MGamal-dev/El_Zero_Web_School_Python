# ==========================
# Assignments from Lesson 81 to 85
# Source: https://elzero.org/python-assignments-lesson-from-81-to-85/
# Topic: Generators & Decorators
# ==========================

# ========================== Assignment 01 ==========================
# Generator function to reverse a string character by character

def reverse_string(my_string):
    # Iterate over the string in reverse order and yield each character
    for char in reversed(my_string):
        yield char

# Using the generator to print each character in reverse
for c in reverse_string("Elzero"):
    print(c)


# ========================== Assignment 02 ==========================
# Decorator function to add behavior before and after a function call

def myDecorator(func):
    def nestedFunc(*myfunc):
        print("Sugar Added From Decorators")
        func(*myfunc)
        print("#"*30)
    return nestedFunc

@myDecorator
def make_tea():
    print("Tea Created")

@myDecorator
def make_coffe():
    print("Coffe Created")

# Calling decorated functions
make_tea()
make_coffe()

# Expected Output:
# Sugar Added From Decorators
# Tea Created
# ##############################
# Sugar Added From Decorators
# Coffe Created
# ##############################
