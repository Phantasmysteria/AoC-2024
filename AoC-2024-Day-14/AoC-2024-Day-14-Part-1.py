import sys
sys.path.append('..')
import AoCUtils
import itertools, functools
from itertools import product, accumulate
from functools import reduce
import numpy as np
import re
import math

rawInput = AoCUtils.listLines(day="14", part="2")

inp_1 = np.array([[int(i) for i in re.findall('-*\d+', item)] for item in rawInput]).T

num_seconds = 100
actual_space_y, actual_space_x = (103, 101)
example_space_y, example_space_x = (7, 11)

curr_space_y, curr_space_x = actual_space_y, actual_space_x

grid_actual = np.zeros((actual_space_y, actual_space_x), dtype=int)
grid_example = np.zeros((example_space_y, example_space_x), dtype=int)

grid_curr = grid_actual

coords = np.vstack(((inp_1[1] + inp_1[3] * num_seconds), (inp_1[0] + inp_1[2] * num_seconds))).T

for coord in coords:
    new_coords = (coord[0] %  curr_space_y, coord[1] % curr_space_x)
    grid_curr[new_coords] += 1

def split_down(g, y, x):
    return np.array([
        g[:math.floor(y / 2), :math.floor(x / 2)],
        g[math.ceil(y / 2):, :math.floor(x / 2)],
        g[:math.floor(y / 2), math.ceil(x / 2):],
        g[math.ceil(y / 2):, math.ceil(x / 2):],
    ])

quads = split_down(grid_curr, curr_space_y, curr_space_x)
robots = np.sum(quads, axis=(1,2))
output = reduce(lambda acc, next: acc * next, robots)
print(output)
