# Game board
board = ["-","-","-",
         "-","-","-",
         "-","-","-",]

def show_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


# Player inputs
def inputs(current_player):
    position = int(input("Field from 1 to 9: ")) - 1
    board[position] = current_player


# Player switching from X to O
def switch(player):
    if player == "X":
        return "O"
    else:
        return "X"


# Win conditions
def check_row(board):
    row_1 = (True if (board[0] == board[1] == board[2]) and (board[0] + board[1] + board[2]) != "---" else False)
    row_2 = (True if (board[3] == board[4] == board[5]) and (board[3] + board[4] + board[5]) != "---" else False)
    row_3 = (True if (board[6] == board[7] == board[8]) and (board[6] + board[7] + board[8]) != "---" else False)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_column(board):
    column_1 = (True if (board[0] == board[3] == board[6]) and (board[0] + board[3] + board[6]) != "---" else False)
    column_2 = (True if (board[1] == board[4] == board[7]) and (board[1] + board[4] + board[7]) != "---" else False)
    column_3 = (True if (board[2] == board[5] == board[8]) and (board[2] + board[5] + board[8]) != "---" else False)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals(board):
    diagonal_1 = (True if (board[0] == board[4] == board[8]) and (board[0] + board[4] + board[8]) != "---" else False)
    diagonal_2 = (True if (board[2] == board[4] == board[6]) and (board[2] + board[4] + board[6]) != "---" else False)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return

# Checking win conditions
def win_check():
    check_row(board)
    check_column(board)
    if check_diagonals(board):
        return "Win by diagonal."

# Playing game
def start_game():
    current_player = "X"
    #counter = 0
    while True:
        show_board()
        if "-" not in board:
            break
        win_check()
        inputs(current_player)
        current_player = switch(current_player)
        #counter += 1


start_game()