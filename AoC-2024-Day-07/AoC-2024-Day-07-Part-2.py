import sys
sys.path.append('..')
import AoCUtils
import itertools, functools
from itertools import product, accumulate
from functools import reduce
import numpy as np
import re
import math

rawInput = AoCUtils.listLines(day="07", part="2")

targets = [ int(item.split(': ')[0]) for item in rawInput ]
eqns = [ item.split(': ')[1] for item in rawInput ]
eqns = [ [int(x) for x in item.split(' ')] for item in eqns ]

def recur(curr, acc, target, operations):
    curr_copy = curr[:]
    if not len(curr_copy):
        return acc == target
    else:
        if acc > target:
            return False
    
    return recur(curr_copy[1:], acc + curr[0], target, operations + "+") or recur(curr_copy[1:], acc * curr[0], target, operations + "*") or recur(curr_copy[1:], int(str(acc) + str(curr[0])), target, operations + "|")
                                                                                  
output = 0
for i in range(len(targets)):
    if recur(eqns[i], 0, targets[i], ""):
        output += targets[i]

print(output)
