## Personal Programming Project - William Peng
import colorama, time
from random import randint

def main():
    showrules()
    game()

def showrules():
    print("Starting: The first click is always safe, often revealing a blank area. \nNumbers: A number (1-8) indicates exactly how many mines are in the 8 adjacent cells - horizontal, vertical, and diagonal.\nEmpty Cells: Choosing a cell with no adjacent mines reveals a large area\nWinning: Clear all non-mine cells.\nLosing: If you choose a cell with a mine.\nFlagging: type “flag” before coordinate to mark cells you suspect are mines (eg. if you wanted to flag cell “H2” you would say “flag H2”).")

#
def game():
    # set_timer()
    difficulty = set_difficulty()
    random_bomb_placement(difficulty)
    # display_bombs_detected()
    # coordinate_user_input()
# def set_timer():
#     start_time = time.time
#     print(start_time())

def set_difficulty():
    difficulty = input("Choose your difficulty... (Easy, Medium, Hard)").lower()
    return difficulty

def random_bomb_placement(difficulty):
    if difficulty == "easy":


    
    


main()
