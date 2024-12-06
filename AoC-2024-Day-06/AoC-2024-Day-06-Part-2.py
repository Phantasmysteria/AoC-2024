import sys
sys.path.append('..')
import AoCUtils
import itertools, functools
from itertools import product, accumulate
from functools import reduce
import numpy as np
import re
import math

rawInput = AoCUtils.listLines(day="06", part="2")
grid = [[i for i in s] for s in rawInput]
grid = np.array(grid, dtype=str)
grid = np.pad(grid, 1, constant_values='B')
height, width = grid.shape

starting_row, starting_col = tuple(x[0] for x in np.where(grid == '^'))
grid[starting_row, starting_col] = '0'

clean_grid = np.copy(grid)

# traverse maze
directions = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1)
}

def check_stuck(grd, r, c):

    gd = np.copy(grd)
    gd_traversals = np.zeros_like(gd, dtype=int)
    
    gd[r, c] = '#'
    guard_r, guard_c = starting_row, starting_col
    curr_dir = 0

    while gd[guard_r+directions[curr_dir][0], guard_c+directions[curr_dir][1]] != 'B':
        while gd[guard_r+directions[curr_dir][0], guard_c+directions[curr_dir][1]] == '#':
            curr_dir = (curr_dir + 1) % 4
        gd[guard_r, guard_c] = 'X'
        gd_traversals[guard_r, guard_c] += 1
        if gd_traversals[guard_r, guard_c] >= 5:
            # Uncomment for logging
            #print(f"Guard gets stuck with ({r},{c})")
            #gd[r, c] = '!'
            #print(gd)
            #print(gd_traversals)
            #print()
            return True
        guard_r, guard_c = guard_r+directions[curr_dir][0], guard_c+directions[curr_dir][1]
    
    return False
        

grid_traversals = np.zeros_like(grid, dtype=int)

guard_row, guard_col = starting_row, starting_col
current_dir = 0
while grid[guard_row+directions[current_dir][0], guard_col+directions[current_dir][1]] != 'B':
    while grid[guard_row+directions[current_dir][0], guard_col+directions[current_dir][1]] == '#':
        current_dir = (current_dir + 1) % 4
    grid[guard_row, guard_col] = 'X'
    grid_traversals[guard_row, guard_col] += 1
    guard_row, guard_col = guard_row+directions[current_dir][0], guard_col+directions[current_dir][1]
    
grid[guard_row, guard_col] = 'X'
grid_traversals[guard_row, guard_col] += 1    

traversed_pos = np.where(grid_traversals > 0)

output = 0
for arow, acol in zip(traversed_pos[0], traversed_pos[1]):
    if check_stuck(clean_grid, arow, acol):
        output += 1
print(output)

