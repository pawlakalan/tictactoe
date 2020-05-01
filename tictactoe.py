# Tic-Tac-Toe game
# made by Alan Pawlak 

#global variables
cells_list = cells_list = [[' ' for j in range(3)] for i in range(3)]
winner = ''
turn = 'X'

# print the board
def print_board():
    global x_counter
    global o_counter
    print('---------')
    for i in range(len(cells_list)):
        line = "|"
        for j in range(len(cells_list[i])):
            line += ' ' + ((cells_list[i][j]))
            # count the X's and O's
            if cells_list[i][j] == 'X':
                x_counter += 1
            elif cells_list[i][j] == 'O':
                o_counter += 1
        print(line, "|")
    print('---------')

# make a move
def move():
    global turn
    global cells_list
    try:
        print(turn + "'s turn")
        a,b = input("Enter the coordinates(separated by space): ").split()
        if (int(a) > 3 or int(a) < 1) or (int(b) > 3 or int(b) < 1):
            print("Coordinates should be from 1 to 3!")
        elif cells_list[int(b) * -1][int(a)-1] == ' ':
            cells_list[int(b) * -1][int(a)-1] = turn
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
        elif cells_list[int(b) * -1][int(a)-1] != ' ':
            print("This cell is occupied! Choose another one")
    except ValueError:
        print("You should enter numbers!")

# main loop
print('''
-------------
|Tic-Tac-Toe|
-------------''')
while winner == '':
    x_counter = 0
    o_counter = 0
    print_board()
    move()
    if cells_list[0][0] == cells_list[0][1] == cells_list[0][2] !=' ': # across the top
        winner += cells_list[0][0]
    if cells_list[1][0] == cells_list[1][1] == cells_list[1][2] !=' ': # across the middle
        winner += cells_list[1][0]
    if cells_list[2][0] == cells_list[2][1] == cells_list[2][2] !=' ': # across the bottom
        winner += cells_list[2][0]
    if cells_list[0][0] == cells_list[1][0] == cells_list[2][0] !=' ': # down the left
        winner += cells_list[0][0]
    if cells_list[0][1] == cells_list[1][1] == cells_list[2][1] !=' ': # down the middle
        winner += cells_list[0][1]
    if cells_list[0][2] == cells_list[1][2] == cells_list[2][2] !=' ': # down the right
        winner += cells_list[0][2]
    if cells_list[0][0] == cells_list[1][1] == cells_list[2][2] !=' ': # first diagonal
        winner += cells_list[0][0]
    if cells_list[0][2] == cells_list[1][1] == cells_list[2][0] !=' ': # second diagonal
        winner += cells_list[0][2]
    
    # draw if there are no empty fields and no winner
    if not any(' ' in rows for rows in cells_list):
        print_board() 
        print("Draw")
        break

# print the winner
if winner == 'X' or winner == 'O':
    print_board()
    print(winner, "wins")
