# 08_functions.py
# Function definitions and usage

def calculate(num1, num2, operation="add"):
    """
    Perform basic arithmetic operations: add, subtract, multiply.
    """
    op = operation.strip().lower()
    if op == "add" or op == "a":
        print(num1 + num2)
    elif op == "subtract" or op == "s":
        print(num1 - num2)
    elif op == "multiply" or op == "m":
        print(num1 * num2)
    else:
        print("This operation is unknown.")

# Tests
calculate(10, 20)
calculate(10, 20, "AdD")
calculate(10, 20, "a")
calculate(10, 20, "A")
calculate(10, 20, "S")
calculate(10, 20, "subTRACT")
calculate(10, 20, "Multiply")
calculate(10, 20, "m")

def addition(*nums):
    """
    Sum numbers, skip 10, subtract 5 if present.
    """
    result = 0
    for number in nums:
        if number == 10:
            continue
        elif number == 5:
            result -= 5
        else:
            result += number
    print(result)

addition(10, 20, 30, 10, 15, 5, 100)
addition(10, 20, 30, 10, 15)

def people(name, *skills):
    """
    Print person's name and their skills.
    """
    if skills:
        print(f"Hello {name}, your skills are:")
        for skill in skills:
            print(skill)
    else:
        print(f"Hello {name}, you have no skills to show.")

people("Osama", "HTML", "CSS", "JS", "Python")
people("Ahmed")

def say_hello(name="unknown", age="unknown", country="unknown"):
    print(f"Hello {name}, your age is {age} and your country is {country}")

say_hello("Osama", 38, "Egypt")
say_hello()
