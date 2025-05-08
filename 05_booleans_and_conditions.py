# 05_booleans_and_conditions.py
# Boolean values and conditional logic

print(bool("me"))
print(bool(1))
print(bool(True))
print(bool(100.00))
print(bool([1, 2, 3]))
print(bool(None))
print(bool(""))
print(bool(''))
print(bool(0))
print(bool(False))
print(bool([]))
print(bool())

# Logical conditions
html = 80
css = 60
javascript = 70
print(html and css and javascript > 50)

num_one = 10
num_two = 20
num = 20
print(num > num_one or num_two)
print(num > num_one and num > num_two)

# More arithmetic and type conversion
num_one = 10
num_two = 20
result = num_one + num_two
print(result)
print(result ** 3)
print((result ** 3) % 26000)
print((result ** 3) % 26000 / 5)
print(type(str((result ** 3) % 26000 / 5)))
