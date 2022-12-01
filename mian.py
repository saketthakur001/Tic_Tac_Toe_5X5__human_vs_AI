
# X or O if continued 4 times by add the key given by the values given if placed on a board wins, I don't know it's hard to
# explain
wins = {1:[1, 2, 6, 7, 11, 12, 16, 17, 21, 22],
        5:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        6:[1, 2, 6, 7],
        4:[4, 5, 9, 10]}

three_from_the_five = {1:[2, 7, 12, 17, 22],
               5:[6, 7, 8, 9, 10],
               6:[7],
               4:[9]
               }

five_spaces = {1:[1, 6, 11, 16, 21],
               5:[1, 2, 3, 4, 5],
               6:[1],
               4:[5]
              }

# return 4 numbers that starts from the "number" and has "difference" difference
def diff(number, difference, range_):
    lis = []
    num = number-1
    for i in range(range_):
        lis.append(num)
        num += difference
    return lis


def possible_wins(danger_level):
    possible_moves = wins
    range_ = 4
    if danger_level == 2:
        possible_moves = three_from_the_five
        range_ = 3
    for diff_num in wins: # iterating through different differences
        for num in possible_moves[diff_num]: # iterating through all the possiblities a player can win
            # print(diff(num, diff_num,range_))
            yield diff(num, diff_num, range_)

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
    # print(x_pos, o_pos)
    num = 0
    for diff_num in wins: # iterating through different differences
        for num in wins[diff_num]: # iterating through all the possiblities a player can win
            four_to_win = 0
            win_pattern = diff(num, diff_num, 4) # get these numbers and you win
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

def player_moves(board, opponent):
    opponent_moves = []
    opponent = opponent.upper()
    for i in range(len(empty_board)):
        if board[i] == opponent:
            opponent_moves.append(i)
    # print(opponent_moves)
    return opponent_moves

# def analise_the_board(board, opponent):
#     opponent_moves = player_moves(board, opponent)
def who_won(board):
    x_pos = player_moves(empty_board, 'x') # list of moves made by x
    o_pos = player_moves(empty_board, 'o') # list of moves made by o
    for i in possible_wins(1):
        if i == x_pos:
            print('X wins the game!')
            return "X"
        elif i == o_pos:
            print('O wins the game!')
            return "O"

# trying to find the best move to defend

def defend(board, opponent, danger_level):
    best_moves = []
    best_moves2 = []
    pos_list = player_moves(board, opponent.upper())

    for win_pattern in possible_wins(danger_level): # check if the opponent moves are on the list of possible_wins
        # print(win_pattern)
        four_to_win = 0
        x_times_in_pos_list = 0
        for i in win_pattern:
            if i in pos_list:
                x_times_in_pos_list += 1
        if x_times_in_pos_list >= danger_level:
            for i in win_pattern:
                if not board[i].isalpha():
                    best_moves.append(i)
    for i in best_places_ordered:
        if i in best_moves: best_moves2.append(i)
    print(best_moves2, 'best move?')
    return best_moves2  

def opponent_raw(opponent):
    player_moves_ = player_moves(empty_board, opponent)
    for diff_num in five_spaces:
        for num in five_spaces[diff_num]:
            print(num)

            lis = diff(num, diff_num, 5)
            print(lis)

    # lis = []
    # lis2 = [] # i know this is a dumb thing to do, but I am tired and just gonna do it
    # win_moves = possible_wins(1)
    # for diff_num in wins:
    #     for num in wins[diff_num]:
    #         moves_list = diff(num, diff_num, 5)
    #         for move in moves_list:
    #             if move in players_moves:
    #                 lis.append(moves_list)
    #                 break
    # for i in lis:
        # print(i)
    # print(lis)


def three_move_trap(board, opponent):
    best_moves = []
    opponent = opponent.upper()
    if opponent == 'X': me = 'O'
    my_moves = player_moves(board, me)
    opponent_moves = player_moves(board, opponent)
    for moves in possible_wins(2):
        for move in moves:
            if move in my_moves:
                for i in moves:
                    if i not in opponent_moves:
                        best_moves.append(i)
                break
    print(best_moves)
    return best_moves

def best_move(board, opponent):
    defense = defend(board, opponent, 2)
    defense2 = defend(board, opponent, 1)
    opponenet_moves = player_moves(board, opponent)
    three_move_trap(board, opponent)
    # print([i+1 for i in defense])
    # print([i+1 for i in defense2])


select_space(empty_board, 2, "x")
# select_space(empty_board, , "o")
# three_move_trap(empty_board, "X")
print_board(empty_board)

def play_the_game(board):
    while True:
        print_board(board)
        x = input("X make your move: ")
        select_space(board, int(x), "x")
        best_move(board, 'X')
        print_board(board)
        if who_won(board):
            return "X"
        o = input("O make your move: ")
        who_won(board)
        select_space(board, int(o), "o")
        if who_won(board):
            print_board(board)
            return "X"

# play_the_game(empty_board)

opponent_raw('X')