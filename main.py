## Personal Programming Project - William Peng
import os, time, random, sys
from random import randint
from time import sleep

def main():
    showrules()
    clear_screen()
    game()

def clear_screen():
    for i in range(3):
        print(".")
        time.sleep(1)
    print("\n" * 100)

def showrules():
    rules = ("""
Starting: Choose a square by typing the coordinates (eg. A1) for the first square in the first row.
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
    bomb_grid, bomb_locations = random_bomb_placement()
    number_grid = calculate_bombs_around(bomb_grid)
    show_grid = set_grid()
    game_over = False
    bombs = 10
    total_cells = 64
    
    while not game_over:
        clear_screen()
        display_grid(show_grid)
        print(f"💣 Bombs: {bombs} | 🚩 Flags: {count_flags(show_grid)}")
        
        user_input = coordinate_user_input()
        
        if user_input == "quit":
            print("Thanks for playing!")
            break
        
        if user_input.startswith("flag"):
            handle_flag(user_input, show_grid)
            time.sleep(1)
            continue
        
        if not is_valid_coordinate(user_input):
            print("Invalid coordinate! Use format: A1 to H8")
            time.sleep(1)
            continue
        
        row, col = convert_coordinate(user_input)
        
        if show_grid[row][col] != "⬜️":
            print("Cell already revealed!")
            time.sleep(1)
            continue
        
        if bomb_grid[row][col] == "💣":
            show_grid[row][col] = "💣"
            clear_screen()
            display_grid(show_grid)
            print("💥 BOOM! You hit a bomb! Game Over.")
            reveal_all_bombs(bomb_grid, show_grid)
            game_over = True
            break
        
        reveal_cell(row, col, number_grid, show_grid)
        
        if check_win(show_grid, total_cells, bombs):
            clear_screen()
            display_grid(show_grid)
            print("🎉 Congratulations! You cleared all the cells! You win! 🎉")
            game_over = True
            break


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
    print(chosen_bomb_cells)
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
    return grid_display, grid

def calculate_bombs_around(bomb_grid):
    bomb_count_grid = [["0" for _ in range(8)] for _ in range(8)]
    for row in range(8):
        for col in range(8):
            if bomb_grid[row][col] == "💣":
                bomb_count_grid[row][col] = "💣"
                continue
            
            count = 0
            for r in range(row - 1, row + 2):
                for c in range(col - 1, col + 2):
                    if 0 <= r < 8 and 0 <= c < 8:
                        if bomb_grid[r][c] == "💣":
                            count += 1
            
            bomb_count_grid[row][col] = str(count)
    
    return bomb_count_grid

    

def display_grid(show_grid):
    rows = len(show_grid)
    cols = len(show_grid[0])
    print(cols)
    column_headers = "A B C D E F G H"
    print("   " + column_headers)
    print("   " + "-" * 15)
    for row in range(1, rows + 1):
        row_display = f"{row:<2}|"
        row_display += " "
        for col in range(cols):
            row_display += show_grid[row - 1][col] + " "
        print(row_display)

def coordinate_user_input():
    user_input = input("Choose a square (eg. A1) or 'flag A1' to flag: ").strip()
    return user_input

def is_valid_coordinate(coord):
    if len(coord) != 2 or coord[0].upper() not in "ABCDEFGH" or coord[1] not in "12345678":
        return False
    else:
        return True
    
def convert_coordinate(coord):
    letter = coord[0].upper()
    number = int(coord[1])
    
    if letter == "A":
        col = 0
    elif letter == "B":
        col = 1
    elif letter == "C":
        col = 2
    elif letter == "D":
        col = 3
    elif letter == "E":
        col = 4
    elif letter == "F":
        col = 5
    elif letter == "G":
        col = 6
    elif letter == "H":
        col = 7
    
    row = number - 1
    return row, col

def handle_flag(user_input, show_grid):
    flag_part = user_input[5:]
    
    if len(flag_part) == 2 and flag_part[0] in "ABCDEFGH" and flag_part[1] in "12345678":
        if flag_part[0] == "A":
            col = 0
        elif flag_part[0] == "B":
            col = 1
        elif flag_part[0] == "C":
            col = 2
        elif flag_part[0] == "D":
            col = 3
        elif flag_part[0] == "E":
            col = 4
        elif flag_part[0] == "F":
            col = 5
        elif flag_part[0] == "G":
            col = 6
        elif flag_part[0] == "H":
            col = 7
        
        row = int(flag_part[1]) - 1
        
        if show_grid[row][col] == "⬜️":
            show_grid[row][col] = "🚩"
            print("🚩 Cell flagged!")
        elif show_grid[row][col] == "🚩":
            show_grid[row][col] = "⬜️"
            print("Cell unflagged!")
        else:
            print("You can only flag hidden cells!")
    else:
        print("Invalid flag! Use format: flag A1")
    time.sleep(1)

def reveal_cell(show_grid, number_grid, row, col):
    if show_grid[row][col] != "⬜️":
        return
    show_grid[row][col] = number_grid[row][col]
    
    if number_grid[row][col] == "0":
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dx, dy in directions:
            new_row = row + dx
            new_col = col + dy
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if show_grid[new_row][new_col] == "⬜️":
                    reveal_cell(new_row, new_col, number_grid, show_grid)

def reveal_all_bombs(bomb_grid, show_grid):
    print("\nBomb locations:")
    for row in range(8):
        for col in range(8):
            if bomb_grid[row][col] == "💣":
                show_grid[row][col] = "💣"
    display_grid(show_grid)
    
def count_flags(show_grid):
    count = 0
    for row in range(8):
        for col in range(8):
            if show_grid[row][col] == "🚩":
                count += 1
    return count

    pass


    
main()
