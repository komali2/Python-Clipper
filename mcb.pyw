#! python3
# mcb.pw - Saves and loads pieces of text to the clipboard. 
# Usage: py.exe mcb.pyw save <keyword>     Saves clipboard to keyword. 
#        py.exe mcb.pyw <keyword>          Loads keyword to clipboard.
#        py.exe mcb.pyw list               Loads all keywords to clipboard. 

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

#   TODO: Save clipboard content.

# Save <keyword>
if len(sys.argv) > 2 and sys.argv[1] == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    print(mcbShelf[sys.argv[2]])


#   TODO: List keywords and laod content.

mcbShelf.close()