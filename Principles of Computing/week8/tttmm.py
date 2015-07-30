"""
Mini-max Tic-Tac-Toe Player
"""
import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
import codeskulptor
# import SimpleGUICS2Pygame.codeskulptor as codeskulptor

codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1, provided.DRAW: 0, provided.PLAYERO: -1}

def maximize(results):
    """
    :param results: array
    :return: max score
    """
    min_score, scores, move = -1, -1, (-1, -1)
    for result in results:
        if result[0] >= min_score:
            min_score = result[0]
            scores = result[0]
            move = result[1]
    return scores, move

def minimize(results):
    """
    :param results: array
    :return: min score
    """
    scores, move = maximize(map(lambda x: (x[0] * -1, x[1]), results))
    return scores * -1, move

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    empty_squares = board.get_empty_squares()
    # Base case
    if len(empty_squares) == 1:
        cell = empty_squares[0]
        new_board = board.clone()
        new_board.move(cell[0], cell[1], player)
        return SCORES[new_board.check_win()], cell
    # recursion
    else:
        results = []
        for cell in empty_squares:
            new_board = board.clone()
            new_board.move(cell[0], cell[1], player)
            if new_board.check_win() is None:
                scores = mm_move(new_board, provided.switch_player(player))[0]
                results.append((scores, cell))
            else:
                score = SCORES[new_board.check_win()]
                return score, cell
        # find best move
        if player == provided.PLAYERX:
            score, desired_move = maximize(results)
        else:
            score, desired_move = minimize(results)
        return score, desired_move

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(move_wrapper, 1, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
