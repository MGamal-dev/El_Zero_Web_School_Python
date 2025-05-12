# ==========================
# Assignments from Lesson 69 to 71
# Source: https://elzero.org/python-assignments-lesson-from-69-to-71/
# ==========================

# ========================== 01 ==========================
values = (0, 1, 2)

# Check if any value in 'values' is truthy
if any(values):
    # This will be True because 1 and 2 are truthy
    my_var = 0

my_list = [True, 1, 1, ["A", "B"], 10.5, my_var]

# Check if all elements in the slices of my_list are truthy
if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):
    print("Good")  # Output: Good
else:
    print("Bad")


# ========================== 02 ==========================
# Define variable v
v = 40

# Create a list from 0 to v-1
my_range = list(range(v))  # range(0, 40)

# Calculate sum of my_range plus v, then add pow(v, v, v)
# pow(v, v, v) is modular exponentiation, here equals 0
print(sum(my_range, v) + pow(v, v, v))  # Output: 820


# ========================== 03 ==========================
# Define variable n
n = 20

l = list(range(n))  # list from 0 to 19

# Check if rounded average of l equals max of given numbers
if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):
    print("Good")  # Output: Good


# ========================== 04 ==========================
def my_all(*all_num):
    """
    Custom implementation of all() function.
    Returns True if all elements (or all elements inside iterables) are truthy.
    """
    for num in all_num:
        if isinstance(num, (str, int, bool)):
            if not num:
                return False
            else:
                continue
        else:
            for l in num:
                if not l:
                    return False
            else:
                continue
    else:
        return True


print(my_all([1, 2, 3]))          # True
print(my_all([1, 2, 3, []]))      # False
print(my_all([True, True]))       # True
print(my_all(True, True))         # True
print(my_all(True, True, False))  # False


def my_any(*any_num):
    """
    Custom implementation of any() function.
    Returns True if any element (or any element inside iterables) is truthy.
    """
    for num in any_num:
        if isinstance(num, (str, int, bool)):
            if num:
                return True
            else:
                continue
        else:
            for l in num:
                if l:
                    return True
            else:
                continue
    else:
        return False


print(my_any([0, 1, [], False]))      # True
print(my_any([(), 0, False]))          # False
print(my_any(False, False, 0, "", [], [0]))  # False
print(my_any(False, 0, "", [1]))       # True
print(my_any([0, 0], [False], [True])) # True
print(my_any())                        # False


def my_min(*min_num):
    """
    Custom implementation of min() function.
    Finds the minimum value among all arguments and nested iterables.
    """
    value = []

    for item in min_num:
        if isinstance(item, (int, float, str)):
            value.append(item)
        if isinstance(item, (list, tuple)):
            value.extend(item)

    min_value = value[0]
    for num in value[1:]:
        if min_value > num:
            min_value = num
    else:
        return min_value


print(my_min([10, 100, -20, -100, 50]))  # -100
print(my_min((10, 100, -20, -100, 50)))  # -100
print(my_min(10, 5, 3))                   # 3
print(my_min([8, 4, 6], 10))              # 4
print(my_min(100, [7, 2, 99]))            # 2
print(my_min([9], [4, 2], 5))             # 2


def my_max(*min_max):
    """
    Custom implementation of max() function.
    Finds the maximum value among all arguments and nested iterables.
    """
    value = []

    for item in min_max:
        if isinstance(item, (int, float, str)):
            value.append(item)
        if isinstance(item, (list, tuple)):
            value.extend(item)

    max_value = value[0]
    for num in value[1:]:
        if max_value < num:
            max_value = num
    else:
        return max_value


print(my_max([10, 100, -20, -100, 50, 700]))  # 700
print(my_max((10, 100, -20, -100, 50, 700)))  # 700    
print(my_max(10, 20, 30))                      # 30
print(my_max([5, 1, 9], 7))                    # 9
print(my_max("cat", "dog", "apple"))           # dog
