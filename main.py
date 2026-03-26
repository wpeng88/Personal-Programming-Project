## Personal Programming Project - William Peng
import os, time, random
from random import randint

def main():
    showrules()
    game()

def clear_screen():
    for i in range(3):
        print(".")
        time.sleep(1)
    os.system("cls")

def showrules():
    rules = ("Starting: The first click is always safe, often revealing a blank area. \nNumbers: A number (1-8) indicates exactly how many mines are in the 8 adjacent cells - horizontal, vertical, and diagonal.\nEmpty Cells: Choosing a cell with no adjacent mines reveals a large area\nWinning: Clear all non-mine cells.\nLosing: If you choose a cell with a mine.\nFlagging: type 'flag' before coordinate to mark cells you suspect are mines (eg. if you wanted to flag cell 'H2' you would say 'flag H2')")
    for char in rules:
        for let in char:
            print(let, end='')  
            time.sleep(0.01)                                                                                                                                                                                                                                                                                                                                                                                                                                                 
def game():
    # set_timer()
    # difficulty = set_difficulty()
    grid = set_grid()
    random_bomb_placement()
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
             ["A6", "B6", "C6", "D6", "E6", "6F", "G6", "H6"],
             ["A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7"],
             ["A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8"]]
    return grid

def random_bomb_placement():
    pass
    # if difficulty == "easy":




    
    


main()
