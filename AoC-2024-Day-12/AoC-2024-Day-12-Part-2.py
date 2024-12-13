import sys
sys.path.append('..')
import AoCUtils
import itertools, functools
from itertools import product, accumulate
from functools import reduce
import numpy as np
import re
import math

rawInput = AoCUtils.listLines(day="12", part="2")
grid = [[i for i in s] for s in rawInput]
grid = np.array(grid, dtype=str)
height, width = grid.shape
visited = np.zeros_like(grid, dtype=int)

symbols = []

def check_bounds(y, x):
    return y >= 0 and y < height and x >= 0 and x < width

def find_sides(ind, area):
    area_coords = np.array(np.where(area == 1)).T
    corners = 0
    for coords in area_coords:
        y0, x0 = coords
        for delta_y1, delta_x1, delta_y2, delta_x2 in [(-1, 0, 0, -1), (0, -1, 1, 0), (1, 0, 0, 1), (0, 1, -1, 0)]:
            corner_y, corner_x = (delta_y1 + delta_y2, delta_x1 + delta_x2)
            c1 = check_bounds(y0+delta_y1, x0+delta_x1) and area[y0+delta_y1, x0+delta_x1]
            c2 = check_bounds(y0+delta_y2, x0+delta_x2) and area[y0+delta_y2, x0+delta_x2]
            c3 = check_bounds(y0+corner_y, x0+corner_x) and area[y0+corner_y, x0+corner_x]

            if c1 != c2:
                continue
            if c1 and c2 and c3:
                continue

            corners += 1

    symbols[ind][2] = corners

def find_area(ind, y0, x0, curr_area):
    visited[y0, x0] = 1
    curr_area[y0, x0] = 1
    symbols[ind][1] += 1
    for delta_y, delta_x in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        if check_bounds(y0+delta_y, x0+delta_x):
            if grid[y0+delta_y, x0+delta_x] == symbols[ind][0]:
                if not visited[y0+delta_y, x0+delta_x]:
                    find_area(ind, y0+delta_y, x0+delta_x, curr_area)
    
for coords in np.array(np.meshgrid(np.arange(height), np.arange(width))).T.reshape((height*width, 2)):
    row, col = coords
    if not visited[row, col]:
        symbols.append([grid[row, col], 0, 0])
        curr_area = np.zeros_like(grid, dtype=int)
        find_area(-1, row, col, curr_area)
        find_sides(-1, curr_area)
    
output = sum([s[1] * s[2] for s in symbols])
print(output)