import sys
sys.path.append('..')
import AoCUtils
import itertools, functools
from itertools import product, accumulate
from functools import reduce
import numpy as np
import re
import math

rawInput = AoCUtils.listLines(day="09", part="2")

file_stream = []
file_arr = []

for i, s in enumerate(rawInput[0]):
    file_arr.append([str(math.floor(i/2)) if not i%2 else '.', int(s)])

file_space, free_space = [ file_arr[i] for i in range(len(file_arr)) if not i%2 ], [ [file_arr[i]] for i in range(len(file_arr)) if i%2 ]

front_free_ptr = 0
back_free_ptr = len(free_space)-1
front_space_ptr = 1
back_space_ptr = len(file_space)-1

for _ in range(int(file_space[-1][0])):
    
    for i in range(front_free_ptr, back_free_ptr+1):
        if i == len(free_space):
            continue

        if free_space[i][-1][1] >= file_space[back_space_ptr][1]:
            new_space = [ file_space[back_space_ptr][:], ['.', free_space[i][-1][1] - file_space[back_space_ptr][1]] ]
            free_space[i] = free_space[i][:-1]
            free_space[i].extend(new_space)
            file_space[back_space_ptr][0] = '.'
            break
    back_space_ptr -= 1
    back_free_ptr -= 1

# flatten
new_file_arr = []
for i in range(len(file_space)):
    new_file_arr.append(file_space[i])
    if i != len(file_space)-1:
        new_file_arr.extend(free_space[i])

new_file_stream = []
for item in new_file_arr:
    new_file_stream.extend([item[0] for _ in range(item[1])])

# calculate
output = 0
for i in range(len(new_file_stream)):
    if new_file_stream[i] == '.':
        continue
    output += int(new_file_stream[i]) * i

print(output)