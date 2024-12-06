import sys
sys.path.append('..')
import AoCUtils
import itertools, functools
from itertools import product, accumulate
from functools import reduce
import numpy as np
import re
import math

rawInput = AoCUtils.listLines(day="06", part="1")
grid = [[i for i in s] for s in rawInput]
grid = np.array(grid, dtype=str)
grid = np.pad(grid, 1, constant_values='B')
height, width = grid.shape

starting_row, starting_col = tuple(x[0] for x in np.where(grid == '^'))
grid[starting_row, starting_col] = '0'

# traverse maze
directions = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1)
}

guard_row, guard_col = starting_row, starting_col
current_dir = 0
while grid[guard_row+directions[current_dir][0], guard_col+directions[current_dir][1]] != 'B':
    while grid[guard_row+directions[current_dir][0], guard_col+directions[current_dir][1]] == '#':
        current_dir = (current_dir + 1) % 4
    grid[guard_row, guard_col] = 'X'
    guard_row, guard_col = guard_row+directions[current_dir][0], guard_col+directions[current_dir][1]
    grid[guard_row, guard_col] = 'X'

output = np.count_nonzero(grid == 'X')
print(output)