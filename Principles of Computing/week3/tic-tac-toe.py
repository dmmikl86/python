"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
# do not change their names.
NTRIALS = 1  # Number of trials to run
SCORE_CURRENT = 1.0  # Score for squares played by the current player
SCORE_OTHER = -1.0  # Score for squares played by the other player
SCORE_EMPTY = 0

# Add your functions here.
def mc_trial(board, player):
    curplayer = player
    while board.check_win() == None:
        empty_squares = board.get_empty_squares()
        length = len(board.get_empty_squares())
        index = random.randrange(length)
        row, col = empty_squares[index]
        board.move(row, col, curplayer)
        curplayer = provided.switch_player(curplayer)

def mc_update_scores(scores, board, player):
    winner = board.check_win()
    if winner == provided.DRAW:
        return
    elif winner == player:
        index = 1
    else:
        index = -1

    for row in range(board.get_dim()):
        for col in range(board.get_dim()):
            if board.square(row, col) == player:
                scores[row][col] += SCORE_CURRENT * index
            elif board.square(row, col) == provided.EMPTY:
                scores[row][col] += SCORE_EMPTY * index
            else:
                scores[row][col] += SCORE_OTHER * index

def get_best_move(board, scores):
    max_score = max(scores)

def mc_move(board, player, trials):
    scores = [[0 for dummy_col in range(board.get_dim())] for dummy_row in range(board.get_dim())]
    for trial in range(trials):
        clone_board = board.clone()
        mc_trial(clone_board, player)
        mc_update_scores(scores, clone_board, player)
    return get_best_move(board, scores)

# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.

provided.play_game(mc_move, NTRIALS, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
