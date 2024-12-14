import sys
sys.path.append('..')
import AoCUtils
import itertools, functools
from itertools import product, accumulate
from functools import reduce
import numpy as np
import re
import math
import cv2

np.set_printoptions(threshold = np.inf)

rawInput = AoCUtils.listLines(day="14", part="2")
inp_1 = np.array([[int(i) for i in re.findall('-*\d+', item)] for item in rawInput]).T

num_seconds = 100
actual_space_y, actual_space_x = (103, 101)
example_space_y, example_space_x = (7, 11)

curr_space_y, curr_space_x = actual_space_y, actual_space_x

grid_actual = np.zeros((actual_space_y, actual_space_x), dtype=int)
grid_example = np.zeros((example_space_y, example_space_x), dtype=int)

grid_curr = grid_actual

coords = np.vstack((inp_1[1], inp_1[0]))

num_iters = 1
min_dist = 9223372036854775807
middle_y, middle_x = math.floor(curr_space_y / 2), math.floor(curr_space_x / 2)

for i in range(10000):
    coords[0] = (coords[0] + inp_1[3])
    coords[1] = (coords[1] + inp_1[2])
    coords[0] = np.vectorize(lambda x: x % curr_space_y)(coords[0])
    coords[1] = np.vectorize(lambda x: x % curr_space_x)(coords[1])

    grid_check = np.zeros_like(grid_curr)
    check = coords

    curr_dist = np.sum(np.sqrt((check[0] - middle_y)**2) + (check[1] - middle_x)**2)
    
    if curr_dist < min_dist:
        min_dist = curr_dist
        for coord in check.T:
            grid_check[coord[0], coord[1]] = 1

        grid_check = grid_check * 255    
        cv2.imwrite(f"iter-{i+1}-{curr_dist}.png", grid_check)
    
# No explicit output, just eyeball the final image which resembles a christmas tree :>