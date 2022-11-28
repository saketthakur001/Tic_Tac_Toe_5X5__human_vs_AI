
wins = {1:[1, 2, 6, 7, 11, 12, 16, 17, 21, 22],
        5:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        6:[1, 2, 6, 7],
        4:[4, 5, 9, 10]}

empty_board = [" " for i in range(25)]

def defend(board, opponent):
    best_moves = []
    best_places = [6, 7, 8, 11, 12, 13, 16, 17, 18]
    pos_list = []
    for i in range(len(empty_board)):
        if board[i] == opponent:
            pos_list.append(i)

    for win_pattern in possible_wins():
        four_to_win = 0
        # win_pattern = diff(num, diff_num) # get these numbers and you win
        x_times_in_pos_list = 0
        for i in win_pattern:
            if i in pos_list:
                x_times_in_pos_list += 1
        if x_times_in_pos_list >= 2:
            for i in win_pattern:
                if i in best_places and not board[i].isalpha():
                    if i not in best_moves:
                        best_moves.append(i)
    return best_moves





# def best_move(board, you):
#     best_places = [6, 7, 8, 11, 12, 13, 16, 17, 18]
#     pos_list = []
#     for i in range(len(empty_board)):
#         if board[i] == opponent:
#             pos_list.append(i)    

# def check_if_empty(board, pos):
#     if board[pos].isalpha():
#         return [True, board[pos]]
#     else: return [False]

# select_space(empty_board, 19, "X")
# print(
# empty_board[3],
# check_if_empty(empty_board, 3)
# )
# select_space(empty_board, 4, "X")
# select_space(empty_board, 3, "X")
# print_board(empty_board)

# def ai_move(board):