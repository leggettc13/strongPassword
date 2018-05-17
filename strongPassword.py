#! /usr/bin/python3
# strongPassword - A program that uses regex to determine password strength

import re

# Get the password from user input
passwd = input('Input your password: ')

# Match the password with the different regex to determine strength
def strength( passwd ):
    # Regex for lowercase letters
    lowRegex = re.compile(r'[a-z]+')

    # Regex for uppercase letters
    upRegex = re.compile(r'[A-Z]+')

    # Regex for numbers
    numRegex = re.compile(r'[0-9]+')

    level = 0
    if len(passwd) >= 8:
        level += 1
    if lowRegex.search(passwd) != None:
        level += 1
    if upRegex.search(passwd) != None:
        level += 1
    if numRegex.search(passwd) != None:
        level += 1
    
    if level == 4:
        return 'This Password is Strong'
    else:
        return 'This is Password is Weak'

print(strength(passwd))
