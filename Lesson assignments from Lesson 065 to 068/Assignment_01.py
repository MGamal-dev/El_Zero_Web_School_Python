# Assignment 01
# Create a folder named "Python" on your Desktop, then create and open a file named "assign.py" inside it.
# Programmatically create 50 text files named txt1, txt2, ..., txt50 inside the "Python" folder.
# Write the sentence "Elzero Web School => {File Number}" inside each file, where {File Number} is the file's number.
# Ensure that file number 25 is named "special-text.txt" and is empty without any content.
# On the first line, print the Current Working Directory.
# On the second line, print the directory path where the current file is located.
# On the third line, print the name of the currently opened file.
# On the fourth line, print the total number of files inside the "Python" folder.

import os

# Define the path to the folder where files will be created
folder_path = r"C:\Users\asd\OneDrive\Desktop\Python"

num = 0
while num < 50:
    num += 1
    if num == 25:
        # Create an empty file named "special-text.txt" for file number 25
        open(os.path.join(folder_path, "special-text.txt"), "w").close()
    else:
        # Create a text file named txt{num}.txt and write the specified message inside
        file_path = os.path.join(folder_path, f"txt{num}.txt")
        file_num = open(file_path, "w")
        file_num.write(f"Elzero Web School => {num}")
        file_num.close()

# Print the current working directory
print(os.getcwd())
print("=" * 40)

# Print the directory path where the current script file is located
print(os.path.dirname(os.path.abspath(__file__)))

# Change the current working directory to the directory of the current script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Print the current working directory after the change
print(os.getcwd())

# Print the absolute path of the current script file
print(os.path.abspath(__file__))

# List all files in the target folder and print the total count
file_list = os.listdir(folder_path)
print(len(file_list))
