#test
import time, sys
from time import sleep
rules = ("""
Starting: The first click is always safe, often revealing a blank area.
Numbers: A number (1-8) indicates exactly how many mines are in the 8 adjacent cells - horizontal, vertical, and diagonal.
Empty Cells: Choosing a cell with no adjacent mines reveals a large area
Winning: Clear all non-mine cells.
Losing: If you choose a cell with a mine.
Flagging: type 'flag' before coordinate to mark cells you suspect are mines (eg. if you wanted to flag cell 'H2' you would say 'flag H2')""")

for char in rules:
    print(char, end = "", flush = True)
    sleep(0.02)
    # sys.stdout.write(char)
    # sys.stdout.flush() # Forces immediate display
    # time.sleep(0.02) # Delays for 0.1 seconds 