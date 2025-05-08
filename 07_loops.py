# 07_loops.py
# Loops and control flow

# Countdown with a skip
# num = int(input("Enter your number: "))
# user_num = num
# if num > 0:
#     while num > 1:
#         num -= 1
#         if num == 7:
#             continue
#         print(num)
#     print(f"{user_num - 1} Numbers Printed Successfully.")
# else:
#     print(f"Number {num} is not larger than 0.")

# Sorted friends list
friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
friends.sort()
for friend in friends:
    print(friend)
print(f"Friends Printed And Ignored Names Count Is: 0")

# Print skills using while loop
skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]
while skills:
    print(f"{skills.pop(0)}")
