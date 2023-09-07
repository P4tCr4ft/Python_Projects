import sys
import os

# sys.path.append(os.path.pardir)
# print(os.path.pardir)



# Get the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)

# Get the parent directory (one level up)
parent_dir = os.path.dirname(current_dir)
print(parent_dir)

# Add the parent directory to the sys.path list
sys.path.insert(0, parent_dir)

print(sys.path)

# print(os.getcwd())

import config

print(f"Host is {config.HOST}")
