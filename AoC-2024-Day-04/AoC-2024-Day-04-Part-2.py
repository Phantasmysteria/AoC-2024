import sys
sys.path.append('..')
import AoCUtils
import itertools, functools
from itertools import product, accumulate
from functools import reduce
import numpy as np
import re

rawInput = AoCUtils.listLines(day="04", part="2")

inp_1 = [ [i for i in item] for item in rawInput ]
grid_arr = np.array(inp_1, dtype=str)

width, height = grid_arr.shape

A_indices = np.where(grid_arr == 'A')

mases = 0
for row, col in zip(A_indices[0], A_indices[1]):
    if row == 0 or row == width-1 or col == 0 or col == height-1:
        continue

    # check for x-mases
    if (( grid_arr[row-1, col-1] == 'M' and grid_arr[row+1, col+1] == 'S' ) or ( grid_arr[row-1, col-1] == 'S' and grid_arr[row+1, col+1] == 'M' )) \
        and (( grid_arr[row-1, col+1] == 'M' and grid_arr[row+1, col-1] == 'S' ) or ( grid_arr[row-1, col+1] == 'S' and grid_arr[row+1, col-1] == 'M' )):
        mases += 1
    
output = mases

print(output)
