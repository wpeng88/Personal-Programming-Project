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
        time.sleep(0.5)
    os.system("cls" if os.name == "nt" else "clear")

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
        sleep(0.005)
    input("\n\nPress Enter to start the game...")

def game():
    # Store the bomb grid once
    bomb_grid = random_bomb_placement()[0]
    # Create display grid
    display_grid = set_grid()
    # Track game state
    game_over = False
    cells_revealed = 0
    total_cells = 64
    bombs = 10
    
    while not game_over:
        clear_screen()
        # Display the grid using your existing display_grid function
        display_grid(display_grid)
        
        # Get user input
        user_input = coordinate_user_input()
        
        if user_input == "quit":
            print("Thanks for playing!")
            break
        
        # Process the move
        action_type, row, col = user_input
        
        if action_type == "flag":
            # Handle flagging
            if display_grid[row][col] == "⬜️":
                display_grid[row][col] = "🚩"
                print("Cell flagged!")
            elif display_grid[row][col] == "🚩":
                display_grid[row][col] = "⬜️"
                print("Cell unflagged!")
            time.sleep(1)
            continue
        
        # Handle reveal
        if display_grid[row][col] != "⬜️":
            print("Cell already revealed!")
            time.sleep(1)
            continue
            
        if bomb_grid[row][col] == "💣":
            display_grid[row][col] = "💣"
            clear_screen()
            display_grid(display_grid)
            print("💥 You hit a bomb! Game Over.")
            game_over = True
            break
        
        # Reveal the cell using recursive reveal
        reveal_recursive(row, col, bomb_grid, display_grid)
        
        # Count revealed cells
        cells_revealed = sum(1 for r in range(8) for c in range(8) 
                           if display_grid[r][c] not in ["⬜️", "🚩"])
        
        # Check win condition
        if cells_revealed == total_cells - bombs:
            clear_screen()
            display_grid(display_grid)
            print("🎉 Congratulations! You won! 🎉")
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
        random_cell = (randint(0, 7), randint(0, 7))
        if random_cell not in chosen_bomb_cells:
            chosen_bomb_cells.append(random_cell)
    # Place bombs
    for cell in chosen_bomb_cells:
        x, y = cell[0], cell[1]
        grid[x][y] = "💣"
    return grid, chosen_bomb_cells

def hidden_grid():
    """Your original function - kept intact"""
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
    """Your original display_grid function - kept exactly the same"""
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
    """Modified slightly to return structured data for the game loop"""
    while True:
        user_input = input("Choose a square (eg. A1) or 'flag A1' to flag: ").strip()
        
        # Handle quit
        if user_input.lower() == "quit":
            return "quit"
        
        # Handle flag
        if user_input.lower().startswith("flag "):
            coord_part = user_input[5:].strip()
            if len(coord_part) == 2 and coord_part[0].upper() in "ABCDEFGH" and coord_part[1] in "12345678":
                col = ord(coord_part[0].upper()) - ord('A')
                row = int(coord_part[1]) - 1
                return ("flag", row, col)
            else:
                print("Invalid coordinates. Use format: flag A1")
                continue
        
        # Handle reveal using your original logic
        if len(user_input) == 2 and user_input[0].upper() in "ABCDEFGH" and user_input[1] in "12345678":
            # Convert letter to number using your approach
            if user_input[0].upper() == "A":
                col = 0
            elif user_input[0].upper() == "B":
                col = 1
            elif user_input[0].upper() == "C":
                col = 2
            elif user_input[0].upper() == "D":
                col = 3
            elif user_input[0].upper() == "E":
                col = 4
            elif user_input[0].upper() == "F":
                col = 5
            elif user_input[0].upper() == "G":
                col = 6
            elif user_input[0].upper() == "H":
                col = 7
            row = int(user_input[1]) - 1
            return ("reveal", row, col)
        else:
            print("Invalid Coordinate. Please try again.")

def reveal_cell():
    """Your original function - kept exactly as is"""
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

def reveal_recursive(row, col, bomb_grid, display_grid):
    """Helper function for cascading reveals"""
    if not (0 <= row < 8 and 0 <= col < 8):
        return
    if display_grid[row][col] not in ["⬜️", "🚩"]:
        return
    
    # Get the number grid from calculate_bombs_around
    number_grid = calculate_bombs_around()
    
    # Reveal current cell
    display_grid[row][col] = number_grid[row][col]
    
    # If it's an empty cell (0), reveal neighbors
    if number_grid[row][col] == "0":
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dx, dy in directions:
            reveal_recursive(row + dx, col + dy, bomb_grid, display_grid)

def flag():
    """Your original flag function - kept as is"""
    pass

main()