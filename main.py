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
    random_bomb_placement()
    hidden_grid()
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
    grid = [["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
             ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
             ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
             ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
             ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
             ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
             ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
             ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"]]  
    return grid



def random_bomb_placement():
    grid = set_grid()
    chosen_bomb_cells = []
    while len(chosen_bomb_cells) < 10:
        random_cell = str(randint(1, 8)) + str(randint(1, 8))
        if random_cell not in chosen_bomb_cells:
            chosen_bomb_cells.append(random_cell)
    for cell in chosen_bomb_cells:
        x, y = int(cell[0]) - 1, int(cell[1]) - 1
        grid[x][y] = "💣"
    return grid, chosen_bomb_cells
    

def hidden_grid():
    grid = calculate_bombs_around()
    rows = len(grid)
    cols = len(grid[0])
    column_headers = "A B C D E F G H"
    print("   " + column_headers)
    for row in range(1, rows + 1):
        grid_display = f"{row:<3}"
        grid_display += grid[row - 1][0] + " " + grid[row - 1][1] + " " + grid[row - 1][2] + " " + grid[row - 1][3] + " " + grid[row - 1][4] + " " + grid[row - 1][5] + " " + grid[row - 1][6] + " " + grid[row - 1][7]
        print(grid_display)
    return grid_display

def calculate_bombs_around():
    grid, chosen_bomb_cells = random_bomb_placement()
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    bomb_count_grid = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
    print(bomb_count_grid)
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == "💣":
                bomb_count_grid[x][y] = "💣"
                continue
            bomb_count = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy 
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == "💣":
                    bomb_count += 1
            if bomb_count == 0:   
                bomb_count_grid[x][y] = "0️⃣"
            elif bomb_count == 1:
                bomb_count_grid[x][y] = "1️⃣"
            elif bomb_count == 2:
                bomb_count_grid[x][y] = "2️⃣"
            elif bomb_count == 3:
                bomb_count_grid[x][y] = "3️⃣"
            elif bomb_count == 4:
                bomb_count_grid[x][y] = "4️⃣"
            elif bomb_count == 5:
                bomb_count_grid[x][y] = "5️⃣"
            elif bomb_count == 6:
                bomb_count_grid[x][y] = "6️⃣"
            elif bomb_count == 7:
                bomb_count_grid[x][y] = "7️⃣"
            elif bomb_count == 8:
                bomb_count_grid[x][y] = "8️⃣"
            else:
                bomb_count_grid[x][y] = "0️⃣"
    return bomb_count_grid

# def hidden_grid():
#     grid, chosen_bomb_cells = random_bomb_placement()
#     grid_display = hidden_no_number_grid()
    



    

def display_grid():
    show_grid = set_grid()
    rows = len(show_grid)
    print(rows)
    cols = len(show_grid[0])
    print(cols)
    column_headers = "A B C D E F G H"
    print("   " + column_headers)
    for row in range(1, rows + 1):
        row_display = f"{row:<3}"
        row_display += show_grid[row - 1][0] + show_grid[row - 1][1] + show_grid[row - 1][2] + show_grid[row - 1][3] + show_grid[row - 1][4] + show_grid[row - 1][5] + show_grid[row - 1][6] + show_grid[row - 1][7]
        print(row_display)
    return(row_display)
    
    
main()
