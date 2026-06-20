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
    os.system("cls")

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
        sleep(0.00001)   
    input("\n\nPress Enter to start the game...")

def game():
    # Get the bomb grid
    bomb_grid = random_bomb_placement()[0]
    # Create the display grid
    show_grid = set_grid()
    
    # Game loop
    while True:
        clear_screen()
        display_grid(show_grid)
        
        # Get user input
        user_input = coordinate_user_input()
        
        # Convert input to coordinates
        if len(user_input) == 2 and user_input[0] in "ABCDEFGH" and user_input[1] in "12345678":
            if user_input[0] == "A":
                col = 0
            elif user_input[0] == "B":
                col = 1
            elif user_input[0] == "C":
                col = 2
            elif user_input[0] == "D":
                col = 3
            elif user_input[0] == "E":
                col = 4
            elif user_input[0] == "F":
                col = 5
            elif user_input[0] == "G":
                col = 6
            elif user_input[0] == "H":
                col = 7
            row = int(user_input[1]) - 1
            
            # Check if cell already revealed
            if show_grid[row][col] != "⬜️":
                print("Cell already revealed!")
                time.sleep(1)
                continue
            
            # Check for bomb
            if bomb_grid[row][col] == "💣":
                show_grid[row][col] = "💣"
                clear_screen()
                display_grid(show_grid)
                print("You hit a bomb! Game Over.")
                break
            
            # Reveal the cell
            reveal_cell_simple(row, col, bomb_grid, show_grid)
            
            # Check for win
            revealed_count = 0
            for r in range(8):
                for c in range(8):
                    if show_grid[r][c] != "⬜️":
                        revealed_count += 1
            if revealed_count == 54:  # 64 - 10 bombs
                clear_screen()
                display_grid(show_grid)
                print("Congratulations! You won!")
                break
                
        elif "flag" in user_input:
            # Handle flag
            flag_parts = user_input.split()
            if len(flag_parts) == 2:
                flag_coord = flag_parts[1]
                if len(flag_coord) == 2 and flag_coord[0] in "ABCDEFGH" and flag_coord[1] in "12345678":
                    if flag_coord[0] == "A":
                        col = 0
                    elif flag_coord[0] == "B":
                        col = 1
                    elif flag_coord[0] == "C":
                        col = 2
                    elif flag_coord[0] == "D":
                        col = 3
                    elif flag_coord[0] == "E":
                        col = 4
                    elif flag_coord[0] == "F":
                        col = 5
                    elif flag_coord[0] == "G":
                        col = 6
                    elif flag_coord[0] == "H":
                        col = 7
                    row = int(flag_coord[1]) - 1
                    
                    if show_grid[row][col] == "⬜️":
                        show_grid[row][col] = "🚩"
                        print("Cell flagged!")
                    elif show_grid[row][col] == "🚩":
                        show_grid[row][col] = "⬜️"
                        print("Cell unflagged!")
                    time.sleep(1)
        else:
            print("Invalid Coordinate. Please try again.")
            time.sleep(1)

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
    return grid_display, grid

def calculate_bombs_around():
    grid, chosen_bomb_cells = random_bomb_placement()
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    bomb_count_grid = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

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
                bomb_count_grid[x][y] = "0"
            elif bomb_count == 1:
                bomb_count_grid[x][y] = "1"
            elif bomb_count == 2:
                bomb_count_grid[x][y] = "2"
            elif bomb_count == 3:
                bomb_count_grid[x][y] = "3"
            elif bomb_count == 4:
                bomb_count_grid[x][y] = "4"
            elif bomb_count == 5:
                bomb_count_grid[x][y] = "5"
            elif bomb_count == 6:
                bomb_count_grid[x][y] = "6"
            elif bomb_count == 7:
                bomb_count_grid[x][y] = "7"
            elif bomb_count == 8:
                bomb_count_grid[x][y] = "8"
            else:
                bomb_count_grid[x][y] = "0"
    return bomb_count_grid

def display_grid(show_grid):
    rows = len(show_grid)
    cols = len(show_grid[0])
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
    user_input = input("Choose a square by typing the coordinates (eg. A1) or 'flag A1' to flag: ")
    return user_input

def reveal_cell_simple(row, col, bomb_grid, show_grid):
    # Get the number grid
    number_grid = calculate_bombs_around()
    
    # Reveal the current cell
    show_grid[row][col] = number_grid[row][col]
    
    # If it's a 0 (empty), reveal neighbors
    if number_grid[row][col] == "0":
        # Check all 8 directions
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dx, dy in directions:
            new_row = row + dx
            new_col = col + dy
            # Make sure we're in bounds
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                # Only reveal if not already revealed and not a flag
                if show_grid[new_row][new_col] == "⬜️":
                    reveal_cell_simple(new_row, new_col, bomb_grid, show_grid)

def reveal_cell():
    grid = random_bomb_placement()[0]
    show_grid = set_grid()
    user_input = coordinate_user_input()

    if grid[int(user_input[0])][int(user_input[1])] == "💣":
        show_grid[int(user_input[0])][int(user_input[1])] = "💣"
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
        print("You hit a bomb! Game Over.")
        sys.exit()

def flag():
    pass

main()