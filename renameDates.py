#! python3
# renameDates.py - Rename file names with American MM-DD-YYY date format
# to "European" DD-MM-YYY (where the hell is Europe??)

import shutil
import os
import re

# Create a regex that matches files with the American date format.

datePattern = re.compile(r"""
    ^(.?)                       # All text before the data (1)
    ((0|1)?\d)                  # One or two digits for the MONTH (2) (3)
    -                           # A dash character
    ((0|1|2|3)?\d)              # One or two digits for the DAY (4) (5)
    -                           # A dash character
    ((19|20)\d\d)               # Four digits for the YEAR (6) (7)
    (.^?)$                      # All text after the date (8)
    """, re.VERBOSE)

# Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    match_object = datePattern.search(amerFilename)

    # Skip files that don't have a date
    if match_object is None:
        continue

    # Get the groups of regular expression text pieces
    beforePart = match_object.group(1)
    monthPart = match_object.group(2)
    dayPart = match_object.group(4)
    yearPart = match_object.group(6)
    afterPart = match_object.group(8)

# Form the European - style filename (DD-MM-YYY)
euroFilename = beforePart + dayPart + "-" + monthPart + "-" + yearPart + \
               afterPart

# Get the full, absolute path.
absWorkingDir = os.path.abspath('.')
amerFilename = os.path.join(absWorkingDir, amerFilename)
euroFilename - os.path.join(absWorkingDir, euroFilename)

# Rename the files.
print('Renaming "%s" ot "%s"... ' % (amerFilename, euroFilename))
# shutil.move(amerFilename, euroFilename) # Uncomment after testing!
