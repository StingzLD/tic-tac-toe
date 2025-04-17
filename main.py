"""
--------------------------------------------------------------------------------
                                 REQUIREMENTS
--------------------------------------------------------------------------------
Implement the following features:
- The board should be stored as a three-element list, while each element is
another three-element list (the inner lists represent rows) so that all the
squares may be accessed using the following syntax:
        board[row][column]
- Each of the inner list's elements can contain 'O', 'X', or a digit
representing the square's number (such a square is considered free).
- The board's appearance should be exactly the same as the one presented below.
        +-------+-------+-------+
        |       |       |       |
        |   1   |   2   |   3   |
        |       |       |       |
        +-------+-------+-------+
        |       |       |       |
        |   4   |   X   |   6   |
        |       |       |       |
        +-------+-------+-------+
        |       |       |       |
        |   7   |   8   |   9   |
        |       |       |       |
        +-------+-------+-------+
- Implement the functions defined for you in the editor.
--------------------------------------------------------------------------------
                                 ASSUMPTIONS
--------------------------------------------------------------------------------
- The computer (i.e., your program) should play the game using 'X's.
- The user (e.g., you) should play the game using 'O's.
- The first move belongs to the computer − it always puts its first 'X' in the
  middle of the board.
- All the squares are numbered row by row starting with 1 (see the example
  session below for reference).
- The user inputs their move by entering the number of the square they choose.
− The number must be valid, i.e., it must be an integer, it must be greater than
  0 and less than 10, and it cannot point to a field which is already occupied.
- The program checks if the game is over − there are four possible verdicts:
    1. The game should continue
    2. The game ends with a tie
    3. You win
    4. The computer wins
- The computer responds with its move and the check is repeated.
- Don't implement any form of artificial intelligence. A random field choice
  made by the computer is good enough for the game.
--------------------------------------------------------------------------------
                                     NOTES
--------------------------------------------------------------------------------
Drawing a random integer number can be done by utilizing a Python function
called randrange(). The example program below shows how to use it (the program
prints ten random numbers from 0 to 8).
    from random import randrange
     
    for i in range(10):
        print(randrange(8))
"""
from random import randrange

def display_board(board):
    """
    The function accepts one parameter containing the board's current status
    and prints it out to the console.
    """


def enter_move(board):
    """
    The function accepts the board's current status, asks the user about their
    move, checks the input, and updates the board according to the user's
    decision.
    """


def make_list_of_free_fields(board):
    """
    The function browses the board and builds a list of all the free squares.
    The list consists of tuples, while each tuple is a pair of row and column
    numbers.
    """


def victory_for(board, sign):
    """
    The function analyzes the board's status in order to check if the player
    using 'O's or 'X's has won the game.
    """


def draw_move(board):
    """
    The function draws the computer's move and updates the board.
    """
