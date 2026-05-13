## Personal Programming Project - William Peng
import os, time, random, sys
from random import randint
from time import sleep

def main():
    showrules()
    game()

def clear_screen():
    for i in range(3):
        print(".")
        time.sleep(1)
    os.system("cls")

def showrules():
    rules = ("""
Starting: The first click is always safe, often revealing a blank area.
Numbers: A number (1-8) indicates exactly how many mines are in the 8 adjacent cells - horizontal, vertical, and diagonal.
Empty Cells: Choosing a cell with no adjacent mines reveals a large area
Winning: Clear all non-mine cells.
Losing: If you choose a cell with a mine.
Flagging: type 'flag' before coordinate to mark cells you suspect are mines (eg. if you wanted to flag cell 'H2' you would say 'flag H2')""")        
    for char in rules:
        print(char, end = "", flush = True)
        # sleep(0.02)
        sleep(0.00001)   
    pass

def game():
    # set_timer()
    # difficulty = set_difficulty()
    grid = set_grid()
    random_bomb_placement()
    hidden_no_number_grid()
    display_grid()
    # display_bombs_detected()
    # coordinate_user_input()

# def set_timer():
#     start_time = time.time
#     print(start_time())

# def set_difficulty():
#     print("Game load difficulty level based on number of bombs 💣 and board size. \nEasy - 10 bombs size 8*8\nMid - 40 bombs size 16 * 16\nHard - 99 bombs size 26 * 16 ")
#     difficulty = input("Choose your difficulty... (Easy, Medium, Hard)").lower()
#     return difficulty
def set_grid():
    # grid = [["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1"],
    #          ["A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2"],
    #          ["A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3"],
    #          ["A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4"],
    #          ["A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5"],
    #          ["A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6"],
    #          ["A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7"],
    #          ["A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8"]]
    grid = [["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
             ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
             ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
             ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
             ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
             ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
             ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
             ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"]]  
    return grid

def display_grid():
    grid = set_grid()
    show_grid = [["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
             ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
             ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
             ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
             ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
             ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
             ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
             ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"]]
    rows = len(grid)
    print(rows)
    cols = len(grid[0])
    print(cols)
    column_headers = "A B C D E F G H"
    print("   " + column_headers)
    for row in range(1, rows + 1):
        row_display = f"{row:<3}"
        row_display += show_grid[row - 1][0] + show_grid[row - 1][1] + show_grid[row - 1][2] + show_grid[row - 1][3] + show_grid[row - 1][4] + show_grid[row - 1][5] + show_grid[row - 1][6] + show_grid[row - 1][7]
        print(row_display)
    return(row_display)
    

def random_bomb_placement():
    grid = set_grid()
    chosen_bomb_cells = []
    while len(chosen_bomb_cells) < 10:
        random_cell = str(randint(1, 8)) + str(randint(1, 8))
        if random_cell not in chosen_bomb_cells:
            chosen_bomb_cells.append(random_cell)
    print(chosen_bomb_cells)
    for cell in chosen_bomb_cells:
        x, y = int(cell[0]) - 1, int(cell[1]) - 1
        grid[x][y] = "💣"
    return grid, chosen_bomb_cells
    
    

def hidden_no_number_grid():
    grid, chosen_bomb_cells = random_bomb_placement()
    rows = len(grid)
    cols = len(grid[0])
    column_headers = "A B C D E F G H"
    print("   " + column_headers)
    for row in range(1, rows + 1):
        grid_display = f"{row:<3}"
        grid_display += grid[row - 1][0] + grid[row - 1][1] + grid[row - 1][2] + grid[row - 1][3] + grid[row - 1][4] + grid[row - 1][5] + grid[row - 1][6] + grid[row - 1][7]
        print(grid_display)
    return grid_display

def hidden_grid():
    grid, chosen_bomb_cells = random_bomb_placement()
    
    

     
    
#   for

# print(random_letter)

    # if difficulty == "easy":



#   for room in house:
#     for colour in room:
#       print("{:<10}".format(colour), end = "")
#     print("\n")
    
    
main()
