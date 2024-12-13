import sys
sys.path.append('..')
import AoCUtils
import itertools, functools
from itertools import product, accumulate
from functools import reduce
import numpy as np
import re
import math

rawInput = AoCUtils.listLines(day="12", part="1")
grid = [[i for i in s] for s in rawInput]
grid = np.array(grid, dtype=str)
height, width = grid.shape
visited = np.zeros_like(grid, dtype=int)

symbols = []

def check_bounds(y, x):
    return y >= 0 and y < height and x >= 0 and x < width

def find_area_perim(ind, y0, x0):
    visited[y0, x0] = 1
    symbols[ind][2] += 4
    symbols[ind][1] += 1
    for delta_y, delta_x in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        if check_bounds(y0+delta_y, x0+delta_x):
            if grid[y0+delta_y, x0+delta_x] == symbols[ind][0]:
                symbols[ind][2] -= 1
                if not visited[y0+delta_y, x0+delta_x]:
                    find_area_perim(ind, y0+delta_y, x0+delta_x)

for coords in np.array(np.meshgrid(np.arange(height), np.arange(width))).T.reshape((height*width, 2)):
    row, col = coords
    if not visited[row, col]:
        symbols.append([grid[row, col], 0, 0])
        find_area_perim(-1, row, col)
    
output = sum([s[1] * s[2] for s in symbols])
print(output)