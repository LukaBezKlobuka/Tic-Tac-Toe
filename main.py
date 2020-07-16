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
    position = int(input(f"{current_player}'s turn. Field from 1 to 9: ")) - 1
    if position not in range(0, 9):
        position = int(input(f"{current_player}'s invalid input. Field from 1 to 9: ")) - 1
    else:
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
        print(board[0] + " has won by row.")
        return True
    elif row_2:
        print(board[3] + " has won by row.")
        return True
    elif row_3:
        print(board[6] + " has won by row.")
        return True
    else:
        return None

def check_column(board):
    column_1 = (True if (board[0] == board[3] == board[6]) and (board[0] + board[3] + board[6]) != "---" else False)
    column_2 = (True if (board[1] == board[4] == board[7]) and (board[1] + board[4] + board[7]) != "---" else False)
    column_3 = (True if (board[2] == board[5] == board[8]) and (board[2] + board[5] + board[8]) != "---" else False)
    if column_1:
        print(board[0] + " has won by column.")
        return True
    elif column_2:
        print(board[1] + " has won by column.")
        return True
    elif column_3:
        print(board[2] + " has won by column.")
        return True
    else:
        return None


def check_diagonals(board):
    diagonal_1 = (True if (board[0] == board[4] == board[8]) and (board[0] + board[4] + board[8]) != "---" else False)
    diagonal_2 = (True if (board[2] == board[4] == board[6]) and (board[2] + board[4] + board[6]) != "---" else False)
    if diagonal_1:
        print(board[0] + " has won by diagonal.")
        return True
    elif diagonal_2:
        print(board[2] + " has won by diagonal.")
        return True
    else:
        return None


# Checking win conditions
def win_check():
    if check_row(board) or check_column(board) or check_diagonals(board):
        return True


# Playing game
def start_game():
    global board
    current_player = "X"
    game_running = True
    while game_running:
        show_board()
        inputs(current_player)
        current_player = switch(current_player)
        if win_check():
            game_running = False
            again = input("Do you want to play again? Y/N: ").lower()
            if again == "y":
                board = ["-"] * 9
                start_game()
            elif again == "n":
                break
        elif "-" not in board:
            print("Tie.")
            break



start_game()
