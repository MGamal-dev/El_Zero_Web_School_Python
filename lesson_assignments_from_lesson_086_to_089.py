"""
Assignments from Lesson 86 to 89
Source: https://elzero.org/python-assignments-lesson-from-86-to-89/
"""

#=====================================01======================================
# Combine elements from a list and a tuple, then join and capitalize the result

my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []

for data in zip(my_list, my_tuple):
    my_data.extend(data)

final_string = "".join(my_data).capitalize()
print(final_string)  # Expected output: Elzero


#=====================================02======================================
# Combine three sequences, append only string items from the first list, join and capitalize

my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []

for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
    if isinstance(item1, str):
        my_data.append(item1)

final_string = "".join(my_data).capitalize()
print(final_string)  # Expected output: Elzero


#=====================================03======================================
# Image processing with Pillow: cropping, converting to grayscale, rotating, and saving

from PIL import Image


def process_image():
    """
    Open an image, crop parts, convert to grayscale,
    rotate one part, then show and save the results.
    """
    image_path = r"C:\Users\asd\OneDrive\Documents\Python\elzero-pillow.png"
    original_image = Image.open(image_path)

    # Crop the letter L, convert to grayscale, show and save
    crop_box1 = (400, 0, 800, 400)
    cropped_image1 = original_image.crop(crop_box1)
    gray_image1 = cropped_image1.convert("L")
    gray_image1.show()
    gray_image1.save("letter_L_gray.png")

    # Crop the second row, convert to grayscale, rotate 180 degrees, show and save
    crop_box2 = (0, 400, 1200, 800)
    cropped_image2 = original_image.crop(crop_box2)
    gray_image2 = cropped_image2.convert("L")
    rotated_image = gray_image2.rotate(180)
    rotated_image.show()
    rotated_image.save("second_row_gray_rotated.png")


# Uncomment to run image processing function
# process_image()


#=====================================04======================================
def say_hello_to(name):
    """
    Greet a person by name.

    Args:
        name (str): The name of the person.

    Returns:
        str: Greeting message.
    """
    return f"Hello {name}"


print(say_hello_to("Osama"))  # Expected output: Hello Osama
help(say_hello_to)


#=====================================05======================================
def say_hello(some_people):
    """
    Say hello to each person in the list.

    Args:
        some_people (list): List of names (str).

    Returns:
        None
    """
    for user_name in some_people:
        print(f"Hello {user_name}")


my_friends = ["Ahmed", "Osama", "Sayed"]
say_hello(my_friends)
