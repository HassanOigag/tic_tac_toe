
def print_board(matrix):
    print("---------")
    print(f"| {matrix[0][0]} {matrix[0][1]} {matrix[0][2]} |")
    print(f"| {matrix[1][0]} {matrix[1][1]} {matrix[1][2]} |")
    print(f"| {matrix[2][0]} {matrix[2][1]} {matrix[2][2]} |")
    print("---------")

def list_to_matrix(symbols):
    matrix = []
    for i in range(3):
        matrix.append([])
        for j in range(3):
            matrix[i].append(symbols[j + i * 3])
    return matrix

def check_rows(matrix, symbol):
    symbols = [symbol for _ in range(3)]
    return any([row for row in matrix if row == symbols])

def count_symbol_matrix(matrix, symbol):
    counter = 0
    for row in matrix:
        for col in row:
            if col == symbol:
                counter += 1
    return counter

def check_columns(matrix, symbol):
    symbols = [symbol for _ in range(3)]
    for j in range(3):
        column = [row[j] for row in matrix]
        if column == symbols:
            return True
    return False

def check_diagonal(matrix, symbol):
    diagonal1 = [matrix[i][i] for i in range(3)]
    diagonal2 = [matrix[0][2], matrix[1][1], matrix[2][0]]
    symbol = [symbol for _ in range(3)]
    return diagonal1 == symbol or diagonal2 == symbol

def check_game_status(matrix, symbol):
    if check_rows(matrix, symbol) or check_columns(matrix, symbol) or check_diagonal(matrix, symbol):
        return 1 #symbol wins
    elif count_symbol_matrix(matrix, " ") == 0:
        return 0 # no empty spaces and no winner means draw
    else:
        return 2 # no winner and empty spces means game not finished yet

if __name__ == "__main__":
    board = list_to_matrix(" "*9)
    print_board(board)
    x_turn = True
    while check_game_status(board, "X") == 2:  
        symbol = "X" if x_turn else "O"
        try:
            x,y = input(f"this is {symbol} turn:\n>").split()
            x,y = int(x) - 1, int(y) - 1
        except  ValueError:
            print("You should enter numbers!")
        else:
            if x not in [0, 1, 2] or y not in [0, 1, 2]:
                print("Coordinates should be from 1 to 3!")
            elif board[x][y] != " ":
                print("This cell is occupied! Choose another one!")
            else:
                board[x][y] = symbol
                print_board(board)
                x_turn = not x_turn

        if check_game_status(board, symbol) == 1:
            print(f"{symbol} wins!")
            break
        elif check_game_status(board, symbol) == 0:
            print("Draw")
            break
