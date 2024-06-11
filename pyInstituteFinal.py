def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    b = board[:]
    print(f"""
            +-------+-------+-------+
            |       |       |       |
            |   {b[0]}   |   {b[1]}   |   {b[2]}   |
            |       |       |       |
            +-------+-------+-------+
            |       |       |       |
            |   {b[3]}   |   {b[4]}   |   {b[5]}   |
            |       |       |       |
            +-------+-------+-------+
            |       |       |       |
            |   {b[6]}   |   {b[7]}   |   {b[8]}   |
            |       |       |       |
            +-------+-------+-------+
            """,end=' ')


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while True:
        move = int(input("Enter your move: "))
        if move in board:
            temp = board.index(move)
            board[temp] = "O"
            break
        else:
            continue



def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    pass


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    pattern = [[0,1,2],[0,3,6],[0,4,8],[2,5,8],[2,4,6],[3,4,5],[6,7,8],[1,4,7]]
    win = False
    for i in pattern:
        if (board[i[0]] == sign) and (board[i[1]] == sign) and (board[i[2]] == sign): 
            win = True
            if win == True:
                return True
                break
    return False



def draw_move(board):
    import random
    while True:
        rand = random.randint(1,10)
        if rand in board:
            temp = board.index(rand)
            board[temp] = "X"
            break
        else:
            continue
        
board = [1,2,3,4,5,6,7,8,9]
win = False
while True:
    board[4] = "X"
    display_board(board)
    enter_move(board)
    win = victory_for(board, "O")
    if win == True:
        print("Player Win!")
        break
    display_board(board)
    draw_move(board)
    win = victory_for(board, "X")
    if win == True:
        print("Computer Win!")
        break
        
