#! /usr/bin/python3
# strongPassword - A program that uses regex to determine password strength

import re

# Regex for lowercase letters
lowRegex = re.compile(r'[a-z]+')

# Regex for uppercase letters
upRegex = re.compile(r'[A-Z]+')

# Regex for numbers
numRegex = re.compile(r'[0-9]+')

# TODO: Get the password from user input

# TODO: Match the password with the different regex to determine strength
