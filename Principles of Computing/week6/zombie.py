"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7

class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list=None,
                 zombie_list=None, human_list=None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)
        else:
            self._human_list = []

    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        self._human_list = []
        self._zombie_list = []

    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))

    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)

    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        # replace with an actual generator
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))

    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)

    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        # replace with an actual generator
        for human in self._human_list:
            yield human

    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        boundary = poc_queue.Queue()
        visited = poc_grid.Grid(self._grid_height, self._grid_width)
        distance_field = [[self._grid_height * self._grid_width for dummy_col in range(self._grid_width)]
                          for dummy_row in range(self._grid_height)]

        if entity_type is HUMAN:
            for human in self.humans():
                boundary.enqueue(human)
        else:
            for zombie in self.zombies():
                boundary.enqueue(zombie)

        for current_cell in boundary:
            row = current_cell[0]
            col = current_cell[1]
            visited.set_full(row, col)
            distance_field[row][col] = 0

        while bool(len(boundary)):
            current_cell = boundary.dequeue()
            for neighbor_cell in self.four_neighbors(current_cell[0], current_cell[1]):
                row = neighbor_cell[0]
                col = neighbor_cell[1]
                if self.is_empty(row, col) and visited.is_empty(row, col):
                    visited.set_full(row, col)
                    distance_field[row][col] = distance_field[current_cell[0]][current_cell[1]] + 1
                    boundary.enqueue(neighbor_cell)

        return distance_field

    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        new_list = []
        remove_list = []
        for human in self.humans():
            coord = human
            row = human[0]
            col = human[1]
            current_cell = zombie_distance_field[row][col]
            for row, col in self.eight_neighbors(row, col):
                if zombie_distance_field[row][col] > current_cell and self.is_empty(row, col):
                    coord = (row, col)
            new_list.append(coord)
            remove_list.append(human)

        for remove in remove_list:
            self._human_list.remove(remove)
        for row, col in new_list:
            self.add_human(row, col)

    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        new_list = []
        remove_list = []
        for zombie in self.zombies():
            coord = zombie
            row = zombie[0]
            col = zombie[1]
            current_cell = human_distance_field[row][col]
            for row, col in self.four_neighbors(row, col):
                if human_distance_field[row][col] < current_cell and self.is_empty(row, col):
                    coord = (row, col)
            new_list.append(coord)
            remove_list.append(zombie)

        for remove in remove_list:
            self._zombie_list.remove(remove)
        for row, col in new_list:
            self.add_zombie(row, col)

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

# poc_zombie_gui.run_gui(Apocalypse(30, 40))

# tests
# obj = Apocalypse(3, 3, [], [], [(2, 2)])
# print obj.compute_distance_field(HUMAN)

# obj = Apocalypse(3, 3, [], [(1, 1)], [])
# obj.add_human(1, 1)

# obj = Apocalypse(3, 3, [], [(1, 1)], [])
# print obj.compute_distance_field(ZOMBIE)

# obj = Apocalypse(3, 3, [], [(2, 2)], [(1, 1)])
# dist = [[4, 3, 2], [3, 2, 1], [2, 1, 0]]
# obj.move_humans(dist)

# obj = Apocalypse(3, 3, [(0, 0), (0, 1), (0, 2), (1, 0)], [(2, 1)], [(1, 1)])
# dist = [[9, 9, 9], [9, 1, 2], [1, 0, 1]]
# obj.move_humans(dist)

# obj = Apocalypse(20, 30, [(4, 15), (5, 15), (6, 15), (7, 15), (8, 15), (9, 15), (10, 15), (11, 15), (12, 15), (13, 15), (14, 15), (15, 15), (15, 14), (15, 13), (15, 12), (15, 11), (15, 10)], [(12, 12), (7, 12)], [(18, 14), (18, 20), (14, 24), (7, 24), (2, 22)])
# dist = [[19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], [18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], [17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 4, 5, 600, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 3, 4, 600, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 600, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 600, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 600, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26], [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 3, 4, 600, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27], [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 3, 4, 600, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28], [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 600, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29], [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 600, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 600, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 3, 4, 600, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29], [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 600, 600, 600, 600, 600, 600, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28], [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27], [17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28], [18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29], [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]]
# obj.move_humans(dist)

# obj = Apocalypse(3, 3, [(0, 0), (0, 1), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)], [(0, 2)], [(1, 1)])
# dist = [[9, 9, 0], [9, 9, 9], [9, 9, 9]]
# obj.move_humans(dist)