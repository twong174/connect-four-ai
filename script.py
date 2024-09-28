from connect_four import *

def two_ai_game():
    my_board = make_board()
    while not game_is_over(my_board):
      #The "X" player finds their best move.
      result = minimax(my_board, True, 4, -float("Inf"), float("Inf"), my_evaluate_board)
      print( "X Turn\nX selected ", result[1])
      print(result[1])
      select_space(my_board, result[1], "X")
      print_board(my_board)

      if not game_is_over(my_board):
        #The "O" player finds their best move
        result = minimax(my_board, False, 4, -float("Inf"), float("Inf"), computer_evaluate_board)
        print( "O Turn\nO selected ", result[1])
        print(result[1])
        select_space(my_board, result[1], "O")
        print_board(my_board)
    if has_won(my_board, "X"):
        print("X won!")
    elif has_won(my_board, "O"):
        print("O won!")
    else:
        print("It's a tie!")

def random_eval(board):
  return random.randint(-100, 100)

def count_streaks(board, symbol, length):
    count = 0
    for col in range(len(board)):
        for row in range(len(board[0])):
            # Check right
            if col <= len(board) - length and all(board[col + i][row] == symbol for i in range(length)):
                count += 1
            # Check down
            if row <= len(board[0]) - length and all(board[col][row + i] == symbol for i in range(length)):
                count += 1
            # Check diagonal (down-right)
            if col <= len(board) - length and row <= len(board[0]) - length and all(board[col + i][row + i] == symbol for i in range(length)):
                count += 1
            # Check diagonal (up-right)
            if col <= len(board) - length and row >= length - 1 and all(board[col + i][row - i] == symbol for i in range(length)):
                count += 1
    return count

def my_evaluate_board(board):
    if has_won(board, 'X'):
        return float('Inf')
    elif has_won(board, 'O'):
        return -float('Inf')

    score = 0
    # Count streaks of different lengths
    for length in range(2, 5):  # 2, 3, and 4
        x_streaks = count_streaks(board, 'X', length)
        o_streaks = count_streaks(board, 'O', length)
        score += x_streaks * length  # Weighted positively
        score -= o_streaks * length  # Weighted negatively
    return score

two_ai_game()



