# 04_sets_and_dicts.py
# Set and dictionary operations

# Remove duplicates from list using set
my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = sorted(set(my_list))
print(unique_list)
print(type(unique_list))
print(unique_list[0:4])

# Set operations
nums = {1, 2, 3}
letters = {"A", "B", "C"}
print(nums.union(letters))
print(nums.symmetric_difference(letters))
nums.update(letters)
print(nums)

# Set methods
my_set = {1, 2, 3}
letters = {"A", "B", "C"}
print(my_set)
my_set.clear()
print(my_set)
my_set.add("A")
my_set.add("B")
print(my_set)
my_set.discard("C")  # No error if 'C' is not present
print(my_set)

# Subset check
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_one.issubset(set_two))

# Dictionary operations
one = {"name": "HTML", "progress": "90%"}
two = {"name": "CSS", "progress": "80%"}
three = {"name": "Python", "progress": "30%"}
four = {"name": "AI", "progress": "20%"}

my_dic = {
    1: one,
    2: two,
    3: three,
    4: four,
}
my_dic.update({"name": "java", "progress": "0%"})  # Adds/updates keys at top level
print(my_dic[1])
print(my_dic[2])
print(my_dic[3])
print(my_dic[4])
print(my_dic.popitem())
