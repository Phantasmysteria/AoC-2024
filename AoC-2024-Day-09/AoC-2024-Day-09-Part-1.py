import sys
sys.path.append('..')
import AoCUtils
import itertools, functools
from itertools import product, accumulate
from functools import reduce
import numpy as np
import re
import math

rawInput = AoCUtils.listLines(day="09", part="1")
file_space, free_space = [ int(rawInput[0][i]) for i in range(len(rawInput[0])) if not i % 2 ], [ int(rawInput[0][i]) for i in range(len(rawInput[0])) if i % 2 ]

front_ptr, back_ptr = 0, len(file_space)-1
free_ptr = 0
block_pos = 0

output = 0

while front_ptr < back_ptr:
    # count front file
    front_file = np.arange(block_pos, block_pos+file_space[front_ptr]) * front_ptr
    
    output += np.sum(front_file)

    # move front pointer
    block_pos += file_space[front_ptr]
    front_ptr += 1
    
    # count back files
    cont = True
    while cont:
        # Free space > file space
        if free_space[free_ptr] - file_space[back_ptr] > 0:
            back_file = np.arange(block_pos, block_pos+file_space[back_ptr]) * back_ptr
            
            output += np.sum(back_file)

            block_pos += file_space[back_ptr]
            free_space[free_ptr] -= file_space[back_ptr]
            back_ptr -= 1
            

        # Free space < file space
        elif free_space[free_ptr] - file_space[back_ptr] < 0:
            back_file = np.arange(block_pos, block_pos+free_space[free_ptr]) * back_ptr
            

            output += np.sum(back_file)

            block_pos += free_space[free_ptr]
            file_space[back_ptr] -= free_space[free_ptr]
            free_ptr += 1
            cont = False
            
        else:
            back_file = np.arange(block_pos, block_pos+file_space[back_ptr]) * back_ptr
            
            output += np.sum(back_file)

            block_pos += file_space[back_ptr]
            free_ptr += 1
            back_ptr -= 1
            cont = False
            
# count front file
front_file = np.arange(block_pos, block_pos+file_space[front_ptr]) * front_ptr

output += np.sum(front_file)

print(output)



