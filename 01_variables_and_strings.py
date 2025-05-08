# 01_variables_and_strings.py
# Basic variable assignments and string manipulations

# Variable assignments
x = "Mohamed"
y = 19
c = "Egypt"

print(x)
print(y)
print(c)

# String concatenation and formatting
msg = "Hello my " + x + " and my age is " + str(y) + " and my " + c
print(msg)

# Checking variable types
print(type(x))
print(type(c))
print(type(y))

# Using f-strings with escape characters
print(f'''Hello '{x}', how you doing \\  """ your age is "{y}"" + and your country is : {c} ''')

# String slicing and manipulation
name = "#@#@Elzero#@#@"
print(name[1])         # '@'
print(name[2])         # '#'
print(name[5])         # 'E'
print(name[1:4])       # '@#@'
print(name[::2])       # '#@Eeo@#'
print(name[-2::-2])    # '@oE@#'
print(name.strip("#@")) # Remove '#' and '@' from both ends

# Zero-filling numbers as strings
for num in ["9", "15", "130", "950", "1500"]:
    print(num.zfill(4))

# String alignment
name_one = "Osama"
name_two = "Osama_Elzero"
print(name_one.rjust(20, "@"))
print(name_two.rjust(20, "@"))

# Swap case
name_one = "OSamA"
name_two = "osaMA"
print(name_one.swapcase())
print(name_two.swapcase())

# String count and index
msg = "I Love Python And Although Love Elzero Web School"
print(msg.count("Love"))

name = "Elzero"
print(name.index("z"))

# String replace
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3", "Love"))

# Numeric types and properties
print(type(1))
print(type(1.2))
print(type(1+2j))

num = 2 + 3j
print(num.imag)
print(num.real)

# Floating point formatting
num = 10
print(f"{num:.10f}")

num = 159.650
print(int(num))
print(type(int(num)))
