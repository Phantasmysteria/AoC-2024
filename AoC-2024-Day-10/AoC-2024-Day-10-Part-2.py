import sys
sys.path.append('..')
import AoCUtils
import itertools, functools
from itertools import product, accumulate
from functools import reduce
import numpy as np
import re
import math

rawInput = AoCUtils.listLines(day="10", part="2")

grid = [[i for i in s] for s in rawInput]
grid = np.array(grid, dtype=int)
height, width = grid.shape

def check_bounds(y, x):
    return y >= 0 and y < height and x >= 0 and x < width

def traverse( y0, x0, curr_step ):
    if not check_bounds(y0, x0):
        return 0
    
    # Part 1
    # was here

    if grid[y0, x0] == curr_step:

        if curr_step == 9:
            return 1

        return traverse( y0-1, x0, curr_step+1 ) \
            + traverse( y0, x0-1, curr_step+1 ) \
            + traverse( y0+1, x0, curr_step+1 ) \
            + traverse( y0, x0+1, curr_step+1 ) \

    return 0
    

starts = np.array(np.where(grid == 0)).T

output = 0
for coords in starts:
    output += traverse(coords[0], coords[1], 0)
    
print(output)