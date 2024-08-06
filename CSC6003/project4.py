import random
"""
-------BATTLESHIPS-------
Pre-reqs: Loops, Strings, Arrays, 2D Arrays, Global Variables, Methods
How it will work:
1. A 10x10 grid will have 5 ships randomly placed about
2. You can choose a row and column to indicate where to shoot
3. For every shot that hits or misses it will show up in the grid
4. If all ships are shot, game over
Legend:
1. "." = water
2. "S" = ship position
3. "O" = water that was shot with bullet, a miss because it hit no ship
4. "X" = ship sunk!
"""
# Global variable for grid size
grid_size = 10

# Global variable for grid
grid = [ ['']*grid_size for i in range(grid_size) ]

# Global variable for number of ships to place
num_of_ships = 5

def drawBoard(myBoard):
    # implement draw board here
    #top of board
    print("+---+" + "---+" * grid_size)
    #sides of board
    print("|   |" + "".join(f" {i} |" for i in range(grid_size)))
    #bottom of baord
    print("+---+" + "---+" * grid_size)
    # Print each row
    for i in range(grid_size):
        print(f"| {i} |" + "".join(f" {myBoard[i][j]} |" for j in range(grid_size)))
        print("+---+" + "---+" * grid_size)

def setupBoard(myBoard):
    # implement setup board here
    # initialize all grid[i][j] = '.'
    for i in range(grid_size):
        for j in range(grid_size):
            myBoard[i][j] = '.'
    # now place the ships
    ships_placed = 0
    while ships_placed < num_of_ships:
        # you can get a random row by using
        randomRow = random.randint(0, grid_size - 1)
        randomCol = random.randint(0, grid_size - 1)
        if myBoard[randomRow][randomCol] == '.':
            myBoard[randomRow][randomCol] = 'S'
            ships_placed += 1

# remember to call myBoard[randomRow][randomCol] = 'S' for every ship
def hitOrMiss(myBoard, row, col):
    # implement the hit or miss functionality here
    if myBoard[row][col] == 'S':
        myBoard[row][col] = 'X'
        return 'HIT!'
    elif myBoard[row][col] == '.':
        myBoard[row][col] = 'O'
        return 'MISS!'
    else:
        return 'Already shot here!'

def isGameOver(myBoard):
    # check if there are ships remaining on the grid.
    for row in myBoard:
        # if there are ships remaining, return false else return true
        if 'S' in row:
            return False
    return True

#a loop to return error message if user continues to input incorrect value
def get_valid_input(prompt, validation_func, error_message):
    while True:
        try:
            value = input(prompt)
            if validation_func(value):
                return int(value)
            else:
                print(error_message)
        except ValueError:
            print("Invalid input.")

#validates if input is accessible in board
def validate_value(val):
    try:
        value = int(val)
        return 0 <= value < grid_size
    except ValueError:
        return False

def main(myBoard):
    # here do everything like
    # set up the board
    setupBoard(myBoard)
    turns = 0
    # till the game is over
    # draw the board
    # ask for a row and column and check it is a hit or a miss
    while not isGameOver(myBoard):
        drawBoard(myBoard)
        col = get_valid_input("Enter a column (X): ", validate_value, "Invalid column. Please enter a number.")
        row = get_valid_input("Enter a row (Y): ", validate_value, "Invalid row. Please enter a number.")
        result = hitOrMiss(myBoard, row, col)
        print(result)
        turns += 1

    drawBoard(myBoard)
    # when the game is over, print that message!
    print(f'Game over! You completed the game in {turns} turns.')



#continously reruns the program to try with different number unless user prompts not to do so
while True:
    # do not forget to call main!
    main(grid)
    choice = input('Would you like to try with different numbers? (y/n): ').strip().lower()
    while choice != 'y' and choice != 'n':
        choice = input('Please enter a valid response, would you like to try again with different numbers? (y/n): ').strip().lower()
    if choice != 'y':
        print('Goodbye!')
        break