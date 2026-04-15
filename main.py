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
#     rules = ("""
# Starting: The first click is always safe, often revealing a blank area.
# Numbers: A number (1-8) indicates exactly how many mines are in the 8 adjacent cells - horizontal, vertical, and diagonal.
# Empty Cells: Choosing a cell with no adjacent mines reveals a large area
# Winning: Clear all non-mine cells.
# Losing: If you choose a cell with a mine.
# Flagging: type 'flag' before coordinate to mark cells you suspect are mines (eg. if you wanted to flag cell 'H2' you would say 'flag H2')""")        
#     for char in rules:
#         print(char, end = "", flush = True)
#         sleep(0.02)   
    pass

def game():
    # set_timer()
    # difficulty = set_difficulty()
    grid = set_grid()
    random_bomb_placement(grid)
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
    grid = [["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1"],
             ["A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2"],
             ["A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3"],
             ["A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4"],
             ["A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5"],
             ["A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6"],
             ["A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7"],
             ["A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8"]]
    return grid


def random_bomb_placement(grid):
    x = ""
    y = ""
    chosen_bomb_cells = []
    for i in range (10):
        random_cell = str(randint(1,8)) + str(randint(1,8))
        if random_cell not in chosen_bomb_cells:
            chosen_bomb_cells.append(random_cell)
    print(chosen_bomb_cells)
    for cell in chosen_bomb_cells:
        print(cell)
        int(cell)
        cell[0] = x
        cell[1] = y
        print(grid[x][y])
    return chosen_bomb_cells
    
#   for

# print(random_letter)

    # if difficulty == "easy":



#   for room in house:
#     for colour in room:
#       print("{:<10}".format(colour), end = "")
#     print("\n")
    
    
main()
