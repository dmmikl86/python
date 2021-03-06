"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""

import poc_fifteen_gui

class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers        
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        # Tile zero is positioned at (i,j)
        # assert self.get_number(target_row, target_col) == 0, "Tile zero is not positioned at ({0},{1})".format(target_row, target_col)
        if not self.get_number(target_row, target_col) == 0:
            return False
        # All tiles in rows i+1 or below are positioned at their solved location
        for row in range(self.get_height()):
            if row > target_row:
                for col in range(self.get_width()):
                    expected_value = row * self.get_width() + col
                    # assert expected_value == self.get_number(row, col), "Tile {0}, {1} is not positioned at solved location".format(row, col)
                    if not expected_value == self.get_number(row, col):
                        return False
            # All tiles in row i to the right of position (i,j) are positioned at their solved location
            if row == target_row:
                for col in range(self.get_width()):
                    if col > target_col:
                        expected_value = row * self.get_width() + col
                        # assert expected_value == self.get_number(row, col), "Tile {0}, {1} is not positioned at solved location".format(row, col)
                        if not expected_value == self.get_number(row, col):
                            return False
        return True

    def move(self, target_row, target_col, row, column):
        '''
        place a tile at target position;
        target tile's current position must be either above the target position
        (k < i) or on the same row to the left (i = k and l < j);
        returns a move string
        '''
        move_it = ''
        combo = 'druld'

        # calculate deltas
        column_delta = target_col - column
        row_delta = target_row - row

        # always move up at first
        move_it += row_delta * 'u'
        # simplest case, both tiles in the same column, combo 'ld' shall go first
        if column_delta == 0:
            move_it += 'ld' + (row_delta - 1) * combo
        else:
            # tile is on the left form target, specific move first
            if column_delta > 0:
                move_it += column_delta * 'l'
                if row == 0:
                    move_it += (abs(column_delta) - 1) * 'drrul'
                else:
                    move_it += (abs(column_delta) - 1) * 'urrdl'
            # tile is on the right from target, specific move first
            elif column_delta < 0:
                move_it += (abs(column_delta) - 1) * 'r'
                if row == 0:
                    move_it += abs(column_delta) * 'rdllu'
                else:
                    move_it += abs(column_delta) * 'rulld'
            # apply common move as last
            move_it += row_delta * combo

        return move_it

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        row, column = self.current_position(target_row, target_col)
        result = self.move(target_row, target_col, row, column)
        self.update_puzzle(result)
        return result

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        result = "u"
        result += "r"
        self.update_puzzle(result)
        row, column = self.current_position(target_row, 0)
        if row == target_row and column == 0:
            # move tile zero to the right end of that row
            step = (self.get_width() - 2) * "r"
            self.update_puzzle(step)
            result += step
        else:
            # target tile to position (i-1, 1) and zero tile to position (i-1, 0)
            step = self.move(target_row - 1, 1, row, column)
            # use move string for a 3x2 puzzle to bring the target tile into position (i, 0),
            # then moving tile zero to the right end of row i-1
            step += "ruldrdlurdluurddlu" + (self.get_width() - 1) * "r"
            self.update_puzzle(step)
            result += step
        return result

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        if not self.get_number(0, target_col) == 0:
            return False

        for column in range(self.get_width()):
            for row in range(self.get_height()):
                if (row == 0 and column > target_col) or (row == 1 and column >= target_col) or row > 1:
                    if not (row, column) == self.current_position(row, column):
                        return False

        return True

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        if not self.lower_row_invariant(1, target_col):
            return False

        for column in range(0, self.get_width()):
            for row in range(2, self.get_height()):
                if not (row, column) == self.current_position(row, column):
                    return False
        return True

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        result = 'ld'
        self.update_puzzle(result)

        row, column = self.current_position(0, target_col)
        if row == 0 and column == target_col:
            return result
        else:
            step = self.move(1, target_col - 1, row, column)
            step += 'urdlurrdluldrruld'
            self.update_puzzle(step)
            result += step

        return result

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        row, column = self.current_position(1, target_col)
        result = self.move(1, target_col, row, column)
        result += 'ur'

        self.update_puzzle(result)
        return result

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        result = ''
        first_step = ''

        if self.get_number(1, 1) == 0:
            first_step += 'ul'
            self.update_puzzle(first_step)
            if (0, 1) == self.current_position(0, 1) and (1, 1) == self.current_position(1, 1):
                return first_step
            if self.get_number(0, 1) < self.get_number(1, 0):
                result += 'rdlu'
            else:
                result += 'drul'
            self.update_puzzle(result)

        return first_step + result

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        return ""

# Start interactive simulation
# puzzle = Puzzle(4, 4)
# poc_fifteen_gui.FifteenGUI(puzzle)

# print puzzle.lower_row_invariant(2, 1)
# print puzzle.lower_row_invariant(0, 1)
