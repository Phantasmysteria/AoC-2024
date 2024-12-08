import sys
sys.path.append('..')
import AoCUtils
import itertools, functools
from itertools import product, accumulate
from functools import reduce
import numpy as np
import re
import math

rawInput = AoCUtils.listLines(day="08", part="2")
grid = [[i for i in s] for s in rawInput]
grid = np.array(grid, dtype=str)

height, width = grid.shape
antennae = np.zeros_like(grid, dtype=str)

unique_letters = np.unique(grid, return_counts=True)
unique_pairs = [ l for l,c in zip(unique_letters[0],unique_letters[1]) if c > 1 and l != '.']

coord_pairs = []

for item in unique_pairs:
    coord_pairs.append(np.array(np.where(grid == item)).T)

def check_inbounds(y, x):
    return y >= 0 and y < height and x >= 0 and x < width

for l in coord_pairs:
    for c1 in range(len(l)):
        for c2 in range(c1+1, len(l)):
            y1, x1 = l[c1]
            y2, x2 = l[c2]
            diff_y, diff_x = y1-y2, x1-x2

            while check_inbounds(y1, x1):
                antennae[y1, x1] = '#'
                y1, x1 = y1+diff_y, x1+diff_x

            while check_inbounds(y2, x2):
                antennae[y2, x2] = '#'
                y2, x2 = y2-diff_y, x2-diff_x

output = np.count_nonzero(antennae == '#')
print(output)