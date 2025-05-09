# ========================== 01 ==========================
# Assignment: Function Packing and Unpacking with **kwargs

def get_score(**skills):
    """
    Print out each skill and its score.
    Accepts any number of keyword arguments.
    """
    for subject, score in skills.items():
        print(f"{subject} => {score}%")

# Example usage with a dictionary (unpacking)
skill_list = {"Math": 90, "Science": 80, "Language": 70}
get_score(**skill_list)
# Output:
# Math => 90%
# Science => 80%
# Language => 70%

print("#" * 50)

# Example usage with direct keyword arguments
get_score(Math=90, Science=80, Language=70)
# Output:
# Math => 90%
# Science => 80%
# Language => 70%

print("#" * 50)

get_score(Logic=70, Problems=60)
# Output:
# Logic => 70%
# Problems => 60%

print("#" * 50)

# ========================== 02 ==========================
# Assignment: Function to display a person's scores with optional name and variable subjects

def get_people_scores(name=None, **scores):
    """
    Prints a score table for a person.

    Parameters:
    - name (str, optional): The person's name.
    - scores (dict): Arbitrary keyword arguments representing subject-score pairs.

    Behavior:
    - If name and scores are provided, prints a greeting and the score table.
    - If name is provided but no scores, notifies that there are no scores to show.
    - If no name but scores are provided, prints just the score table.
    - If neither name nor scores are provided, does nothing.
    """
    if name and scores:
        print(f"Hello {name}, This Is Your Score Table:")
        for subject, score in scores.items():
            print(f"{subject} => {score}")
    elif name and not scores:
        print(f"Hello {name}, You Have No Scores To Show")
    elif not name and scores:
        for subject, score in scores.items():
            print(f"{subject} => {score}")
    else:
        # Neither name nor scores provided - no output
        pass

# Test 1
get_people_scores("Osama", Math=90, Science=80, Language=70)
# Output:
# Hello Osama, This Is Your Score Table:
# Math => 90
# Science => 80
# Language => 70

# Test 2
get_people_scores("Mahmoud", Logic=70, Problems=60)
# Output:
# Hello Mahmoud, This Is Your Score Table:
# Logic => 70
# Problems => 60

print("#" * 50)

# Test 3
get_people_scores(Logic=70, Problems=60)
# Output:
# Logic => 70
# Problems => 60

print("#" * 50)

# Test 4
get_people_scores("Ahmed")
# Output:
# Hello Ahmed, You Have No Scores To Show

print("#" * 50)

# ========================== 03 ==========================
# Assignment: Function to print a score table with optional name and variable subjects

scores_list = {
    "Math": 90,
    "Science": 80,
    "Language": 70
}

def get_the_scores(name=None, **scores):
    """
    Prints a score table for a person.

    Behavior:
    - If name and scores are provided, prints a greeting and the score table.
    - If scores are provided but no name, prints just the score table.
    - If name is provided but no scores, notifies that there are no scores to show.
    - If neither name nor scores are provided, does nothing.
    """
    if name and scores:
        print(f"Hello {name}, This Is Your Score Table:")
        for subject, score in scores.items():
            print(f"{subject} => {score}%")
    elif scores and not name:
        for subject, score in scores.items():
            print(f"{subject} => {score}%")
    elif name and not scores:
        print(f"Hello {name}, You Have No Scores To Show")
    else:
        # Neither name nor scores provided - no output
        pass

# Test 1
get_the_scores("Osama", **scores_list)
# Output:
# Hello Osama, This Is Your Score Table:
# Math => 90%
# Science => 80%
# Language => 70%

print("#" * 50)

# Test 2
get_the_scores("Osama")
# Output:
# Hello Osama, You Have No Scores To Show

print("#" * 50)

# Test 3
get_the_scores(**scores_list)
# Output:
# Math => 90%
# Science => 80%
# Language => 70%

print("#" * 50)
