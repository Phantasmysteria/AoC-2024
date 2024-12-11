import sys
sys.path.append('..')
import AoCUtils
import itertools, functools
from itertools import product, accumulate
from functools import reduce
import numpy as np
import re
import math
import copy

rawInput = AoCUtils.listLines(day="11", part="2")

stones = rawInput[0].split(' ')
stones_dict = {}
for stone in stones:
    if stone not in stones_dict:
        stones_dict[stone] = 0
    stones_dict[stone] += 1

def mod_dict(d, k, v):
    if k not in d:
        d[k] = 0
    d[k] += v
    if d[k] == 0:
        d.pop(k)

# Part 2: 75 iterations (yep that's the only change)
for it in range(75):
    next_stones_dict = copy.deepcopy(stones_dict)
    for key, val in stones_dict.items():
        if key == '0':
            mod_dict(next_stones_dict, '1', val)
            mod_dict(next_stones_dict, '0', -val)
        elif not len(key) % 2:
            mod_dict(next_stones_dict, key, -val)
            mod_dict(next_stones_dict, key[0:len(key)//2], val)
            mod_dict(next_stones_dict, str(int(key[len(key)//2:])), val)
        else:
            mod_dict(next_stones_dict, key, -val)
            mod_dict(next_stones_dict, str(int(key)*2024), val)

    stones_dict = copy.deepcopy(next_stones_dict)

output = sum([v for v in stones_dict.values()])
print(output)