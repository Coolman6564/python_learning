#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - saves clipboard to keyword.
#        py.exe mcb.pyw delete <keyword> - Deletes a keyword from the list.
#        py.exe mcb.pyw delete all - Deletes ALL keywords from the list.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve
import pyperclip
import sys

mcbShelf = shelve.open("mcb")

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    # Clipboard content is saved to shelf file at the key as the keyword.
    # Key is located/given at sys.argv[2]
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and (sys.argv[1].lower == 'delete' and sys.argv[2].lower() == 'all'):
    # Want to delete ALL keywords
    for keyword in list(mcbShelf.keys()):
        del mcbShelf[keyword]
    print("ALL KEYWORDS DELETED!!!")
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    # Want to delete the specified keyword ONLY!!
    if sys.argv[2] in mcbShelf:
        del mcbShelf[sys.argv[2]]
    else:
        print("Keyword not found!!")
elif len(sys.argv) == 2:
    # List keywords OR load content...
    if sys.argv[1].lower() == 'list':
        # List keywords
        pyperclip.copy(str(list(mcbShelf.keys())))
        # Also print list to terminal for usefulness
        print(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        # then its a keyword and we want to load it into the clipboard
        pyperclip.copy(mcbShelf[sys.argv[1]])
    else:
        print("Keyword not found!")
else:
    # If the syntax from the command line isn't correct, print the usage to term
    print("""Usage: py.exe mcb.pyw save <keyword> - saves clipboard to keyword.
         py.exe mcb.pyw delete <keyword> - Deletes a keyword from the list.
         py.exe mcb.pyw delete all - Deletes ALL keywords from the list.
         py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
         py.exe mcb.pyw list - Loads all keywords to clipboard.""")
mcbShelf.close()