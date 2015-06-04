"""
Clone of 2048 game.
"""
import random

import poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    temp_list = []
    zeros = []
    res = []
    for elem in line:
        if elem == 0:
            zeros.append(elem)
        else:
            temp_list.append(elem)

    temp_list.extend(zeros)

    zeros = []
    per = 0
    while per < len(temp_list):
        if per != 0:
            if temp_list[per] == temp_list[per - 1]:
                res.append(temp_list[per] * 2)
                per += 1
                zeros.append(0)
            else:
                res.append(temp_list[per - 1])
        if per + 1 == len(temp_list):
            res.append(temp_list[per])
        per += 1
    res.extend(zeros)
    return res

def traverse_grid(start_cell, direction, num_steps, grid):
    """
    Function that iterates through the cells in a grid
    in a linear direction

    Both start_cell is a tuple(row, col) denoting the
    starting cell

    direction is a tuple that contains difference between
    consecutive cells in the traversal
    """
    line = []
    for step in range(num_steps):
        row = start_cell[0] + step * direction[0]
        col = start_cell[1] + step * direction[1]
        line.append(grid[row][col])
    # print line
    return line

def is_line_changed(line_grid, line_merge):
    """
    check are lines match
    """
    num = 0
    for elem in line_grid:
        if elem != line_merge[num]:
            return False
        num += 1
    return True

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for dummy_col in range(self._grid_width)] for dummy_row in range(self._grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        res = ""
        for row in range(self._grid_height):
            for col in range(self._grid_width):
                res += str(self._grid[row][col]) + "  "
            res += "\n"
        return res

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """

        line_merge = []
        is_need_new_tile = False
        if direction == UP:
            for elem in range(self._grid_width):
                line_grid = traverse_grid((0, elem), OFFSETS[direction], self._grid_height, self._grid)
                line_merge = merge(line_grid)
                if not is_need_new_tile:
                    is_need_new_tile = not is_line_changed(line_grid, line_merge)
                self.set_line_to_grid(line_merge, direction, elem)
        elif direction == DOWN:
            for elem in range(self._grid_width):
                line_grid = traverse_grid((self._grid_height - 1, elem), OFFSETS[direction], self._grid_height, self._grid)
                line_merge = merge(line_grid)
                if not is_need_new_tile:
                    is_need_new_tile = not is_line_changed(line_grid, line_merge)
                self.set_line_to_grid(line_merge, direction, elem)
        elif direction == RIGHT:
            for elem in range(self._grid_height):
                line_grid = traverse_grid((elem, self._grid_width - 1), OFFSETS[direction], self._grid_width, self._grid)
                line_merge = merge(line_grid)
                if not is_need_new_tile:
                    is_need_new_tile = not is_line_changed(line_grid, line_merge)
                self.set_line_to_grid(line_merge, direction, elem)
        else:  # direction == LEFT
            for elem in range(self._grid_height):
                line_grid = traverse_grid((elem, 0), OFFSETS[direction], self._grid_width, self._grid)
                line_merge = merge(line_grid)
                if not is_need_new_tile:
                    is_need_new_tile = not is_line_changed(line_grid, line_merge)
                self.set_line_to_grid(line_merge, direction, elem)
        if is_need_new_tile:
            self.new_tile()

    def set_line_to_grid(self, line, direction, elem):
        """
        Set all tiles in the given direction
        """
        if direction == UP:
            for row in range(self._grid_height):
                self._grid[row][elem] = line[row]
        elif direction == DOWN:
            line.reverse()
            for row in range(self._grid_height):
                self._grid[row][elem] = line[row]
        elif direction == RIGHT:
            line.reverse()
            for col in range(self._grid_width):
                self._grid[elem][col] = line[col]
        else:  # direction == LEFT
            for col in range(self._grid_width):
                self._grid[elem][col] = line[col]

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        row = random.randrange(0, self._grid_height)
        col = random.randrange(0, self._grid_width)
        if self._grid[row][col] == 0:
            if random.randint(1, 10) > 9:
                self._grid[row][col] = 4
            else:
                self._grid[row][col] = 2
        else:
            if not self.is_grid_full():
                self.new_tile()
            else:
                pass

    def get_tiles_counter(self):
        """
        counting tiles in grid
        """
        res = 0
        for row in range(self._grid_height):
            for col in range(self._grid_width):
                if self._grid[row][col] != 0:
                    res += 1
        return res

    def is_grid_full(self):
        """
        check is grid full
        """
        return self.get_tiles_counter() == self._grid_width * self._grid_height

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]

poc_2048_gui.run_gui(TwentyFortyEight(4, 5))