
# X or O if continued 4 times by add the key given by the values given if placed on a board wins, I don't know it's hard to
# explain
wins = {1:[1, 2, 6, 7, 11, 12, 16, 17, 21, 22],
        5:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        6:[1, 2, 6, 7],
        4:[4, 5, 9, 10]}

# empty_board = [str(i+1) for i in range(25)]
empty_board = [" " for i in range(25)]

# better_ones = [12, 7, 11, 13, 17, 6, 8, 16, 18]
best_places_ordered = [12, 7, 11, 13, 17, 6, 8, 16, 18, 0, 4, 24, 20, 2, 10, 14, 22, 1, 3, 5, 9, 15, 19]

def print_board(lis):
    print(f' {lis[0]} | {lis[1]} | {lis[2]} | {lis[3]} | {lis[4]}')
    print(f'-------------------')
    print(f' {lis[5]} | {lis[6]} | {lis[7]} | {lis[8]} | {lis[9]}')
    print(f'-------------------')
    print(f' {lis[10]} | {lis[11]} | {lis[12]} | {lis[13]} | {lis[14]}')
    print(f'-------------------')
    print(f' {lis[15]} | {lis[16]} | {lis[17]} | {lis[18]} | {lis[19]}')
    print(f'-------------------')
    print(f' {lis[20]} | {lis[21]} | {lis[22]} | {lis[23]} | {lis[24]}')

# enter the board you wanna play on, enter the move and whose turn it is
def select_space(board, move, turn):
    if move not in range(1, 26):
        print('out of range')
        return False
    elif board[move-1].isalpha():
        print('There is already a '+board[move-1]+' on '+str(move))
        return False
    else:
        board[move-1] = turn.upper()
        return True

# return 4 numbers that starts from the "number" and has "difference" difference
def diff(number, difference):
    lis = []
    num = number-1
    for i in range(4):
        lis.append(num)
        num += difference
    return lis


# it checks if anyone won                        working status - yes it is working
# need to add (check if there a draw)
def who_won(board): 
    x_pos = [] # list of moves made by x
    o_pos = [] # list of moves made by o
    for i in range(len(board)):
        if 'x' in board[i].lower():
            x_pos.append(i)
        elif 'o' in board[i].lower():
            o_pos.append(i)
    print(x_pos, o_pos)
    num = 0
    for diff_num in wins: # iterating through different differences
        for num in wins[diff_num]: # iterating through all the possiblities a player can win
            four_to_win = 0
            win_pattern = diff(num, diff_num) # get these numbers and you win
            for i in win_pattern:
                if i in x_pos:
                    four_to_win +=1
            if four_to_win == 4:
                return "X wins!"
            four_to_win = 0
            for i in win_pattern:
                if i in o_pos:
                    four_to_win +=1
            if four_to_win == 4:
                return "O wins!"                                            

def possible_wins():
    for diff_num in wins: # iterating through different differences
        for num in wins[diff_num]: # iterating through all the possiblities a player can win
            yield diff(num, diff_num)

def opponent_moves(board, opponent):
    opponent_moves = []
    for i in range(len(empty_board)):
        if board[i] == opponent:
            opponent_moves.append(i)
    return opponent_moves

# def analise_the_board(board, opponent):
#     opponent_moves = opponent_moves(board, opponent)


# trying to find the best move to defend

def defend(board, opponent):
    best_moves = []
    best_moves2 = []
    pos_list = opponent_moves(board, opponent)

    for win_pattern in possible_wins():
        for move in win_pattern:
            if move in pos_list:
                for move in win_pattern:
                    if move not in best_moves: best_moves.append(move)
                break
    for i in best_places_ordered:
        if i in best_moves:
            best_moves2.append(i)
    print(best_moves2)
    return best_moves2



def best_move(board, opponent):
    best_moves = []
    pos_list = []
    for i in range(len(empty_board)):
        if board[i] == opponent:
            pos_list.append(i)
    defense = defend(board, opponent)
    print(defense)
    
# for i in possible_wins():
#     print(i)

select_space(empty_board, 5, "X")
# select_space(empty_board, 13, "X")
# select_space(empty_board, 8, "X")
# select_space(empty_board, 13, "X")


# best_move(empty_board, "X")
print_board(empty_board)

print(
defend(empty_board, "X")
)
# loop the game until someone wins
# while True:
#     x = int(input("X it's your turn: "))
#     select_space(empty_board, x, "X")
#     print_board(empty_board)
#     if who_won(empty_board):
#         print(who_won(empty_board))
#         break
#     o = int(input(("O it's your turn: ")))
#     select_space(empty_board, o, "O")
#     if who_won(empty_board):
#         print(who_won(empty_board))
#         break
#     print_board(empty_board)

# lis = [1, 2, 3]

# for i in lis:
#     if i not in lis:
#         print(i)

