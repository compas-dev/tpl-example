import re
import sys

example_name = "{{cookiecutter.example_name}}"

if not example_name:
    print("ERROR: The example name cannot be empty.")
    sys.exit(1)
