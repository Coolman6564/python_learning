#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip
import re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?          # Optional (?) area code (1)
    (\s|-|\.)?                  # Optional (?) seperator
    (\d{3})                     # First three digits
    (\s|-|\.)                   # Separator
    (\d{4})                     # last four digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # optional (?) extension (group 8)
    )''', re.VERBOSE)

# Create email regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+           # Username (One or more '+')
    @                           # @ symbol
    [a-zA-Z0-9,-]+              # Domain name (One or more '+')
    (\.[a-zA-Z]{2,4})           # dot-something (URL: com, edu, etc...)
    )''', re.VERBOSE)

# Find matches in clipboard
text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
    print(matches)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("Copied to clipboard: ")
    print('\n'.join(matches))
else:
    print("No phone numbers or email addresses found!!")
