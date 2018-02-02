#! python3
# mcb.pw - Saves and loads pieces of text to the clipboard. 
# Usage: py.exe mcb.pyw save <keyword>     Saves clipboard to keyword. 
#        py.exe mcb.pyw <keyword>          Loads keyword to clipboard.
#        py.exe mcb.pyw list               Loads all keywords to clipboard. 

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save <keyword>
if len(sys.argv) > 2 and sys.argv[1] == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    print('Saved ' + pyperclip.paste()  + ' under keyword: ' + sys.argv[2])
elif len(sys.argv) == 2 and sys.argv[1] != 'list':
    try:
        saved = mcbShelf[sys.argv[1]]
        desire = input('This will copy ' + saved + ' to the clipboard, type y to continue, anything else to cancel.')
        if desire == 'y':
            pyperclip.copy(saved)
            print('Copied ' + saved + ' to the clipboard.')
    except KeyError:
        print('Nothing saved under "' + sys.argv[1] + '".')
    

#   TODO: List keywords 

mcbShelf.close()