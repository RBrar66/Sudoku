def draw_board(board):
    print('\n-------------------------')
    for x in range(9):
        print('|',board[x][0], board[x][1], board[x][2], '|',board[x][3], board[x][4], board[x][5], '|',board[x][6], board[x][7], board[x][8], '|')
        if x == 2 or x == 5 or x == 8:
            print('-------------------------')


def next_empty(board):
    # finds next empty space in the board
    for row in range(9):
        for col in range(9):
            if board[row][col] == ' ':
                return row, col
    # returns this if there are no empty spaces left
    return None, None


def check_validity(board, row, col, guess):
    # check if the guess has already been taken in the row, column or 3x3 matrix
    if guess in board[row]:
        return False
    for x in range(9):
        if guess == board[x][col]:
            return False
    r_start = row // 3 * 3
    c_start = col // 3 * 3
    for r in range(r_start, r_start + 3):
        for c in range(c_start, c_start + 3):
            if board[r][c] == guess:
                return False
    return True


def solver(board):
    row, col = next_empty(board)
    if row is None and col is None:
        return True
    for guess in range(1, 10):
        if check_validity(board, row, col, guess):
            board[row][col] = guess

            if solver(board):
                return True
        board[row][col] = ' '
    return False


board = [
[3, 9, ' ',         ' ', 5, ' ',            ' ', ' ', ' '],
[' ',' ',' ',       2,' ',' ',              ' ',' ',5],
[' ',' ',' ',       7,1,9,                  ' ',8,' ',],

[' ',5,' ',         ' ',6,8,                ' ',' ',' '],
[2,' ',6,           ' ',' ',3,              ' ',' ',' '],
[' ',' ',' ',       ' ',' ',' ',            ' ',' ',4],

[5,' ',' ',         ' ',' ',' ',            ' ',' ',' ',],
[6,7,' ',           1,' ',5,                ' ',4,' '],
[1,' ',9,           ' ',' ',' ',            2,' ',' ']

]
draw_board(board)
if solver(board):
    draw_board(board)
else:
    print('This Sudoku puzzle is impossible.')