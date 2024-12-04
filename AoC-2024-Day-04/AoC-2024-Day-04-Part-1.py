import sys
sys.path.append('..')
import AoCUtils
import itertools, functools
from itertools import product, accumulate
from functools import reduce
import numpy as np
import re

rawInput = AoCUtils.listLines(day="04", part="1")
inp_1 = [ [i for i in item] for item in rawInput ]
inp_2 = np.array(inp_1, dtype=str)

hor = np.array(inp_1, dtype=str)
ver = np.array(inp_1, dtype=str).T
xmas = []

# Horizontal
for row in range(len(inp_1)-3):
    for col in range(len(inp_1[0])):
        app = "".join([ inp_2[row, col], inp_2[row+1, col], inp_2[row+2, col], inp_2[row+3, col] ])
        xmas.append( app )

# Vertical
for row in range(len(inp_1)):
    for col in range(len(inp_1[0])-3):
        app = "".join([ inp_2[row, col], inp_2[row, col+1], inp_2[row, col+2], inp_2[row, col+3] ])
        xmas.append( app )

downright = []
# Downright
for row in range(len(inp_1)-3):
    for col in range(len(inp_1[0])-3):
        app = "".join([ inp_2[row, col], inp_2[row+1, col+1], inp_2[row+2, col+2], inp_2[row+3, col+3] ])
        downright.append( app )

upright = []
# Upright
for row in range(3, len(inp_1)):
    for col in range(len(inp_1[0])-3):
        app = "".join([ inp_2[row, col], inp_2[row-1, col+1], inp_2[row-2, col+2], inp_2[row-3, col+3] ])
        upright.append( app )

xmas.extend(downright)
xmas.extend(upright)

output = sum([ 1 if (x == 'XMAS' or x == 'SAMX') else 0 for x in xmas ])

print(output)