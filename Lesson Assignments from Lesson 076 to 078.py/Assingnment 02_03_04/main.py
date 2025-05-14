# ==========================
# main.py - Demonstrate importing and using functions from my_mod.py
# ==========================

# Option 1: Import the whole module and use its functions with module prefix
import my_mod
print(my_mod.say_hello("Osama"))
print(my_mod.say_welcome("Osama"))

# Option 2: Import specific function from the module
from my_mod import say_welcome
print(say_welcome("Osama"))

# Option 3: Import specific function with alias
from my_mod import say_welcome as new_welcome
print(new_welcome("Osama"))
