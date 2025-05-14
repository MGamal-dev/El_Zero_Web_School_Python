# ==========================
# Assignments from Lesson 79 to 80
# Source: https://elzero.org/python-assignments-lesson-from-79-to-80/
# Topic: Date & Time
# ==========================

# ========================== Assignment 01 ==========================
# Calculate the number of days from a specific date to now

import datetime

# Define a specific date: June 25, 2021
the_date = datetime.datetime(2021, 6, 25)

# Get the current date and time
now = datetime.datetime.now()

# Calculate the difference in days between now and the_date
days_difference = (now - the_date).days

print(f"Days From 2021-06-25 To now Is => {days_difference}")


# ========================== Assignment 02 ==========================
# Format and print the current date in various formats

# Get current date (without time)
current_date = datetime.datetime.now().date()

# Print date in different string formats using strftime
print(current_date.strftime("%b %d, %Y"))   # Example: May 14, 2025
print(current_date.strftime("%d - %b - %Y")) # Example: 14 - May - 2025
print(current_date.strftime("%d / %b / %y")) # Example: 14 / May / 25
print(current_date.strftime("%d / %B / %Y")) # Example: 14 / May / 2025
print(current_date.strftime("%a, %d  %B %Y")) # Example: Wed, 14  May 2025
