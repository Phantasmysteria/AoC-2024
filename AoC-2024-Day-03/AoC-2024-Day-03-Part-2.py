import sys
sys.path.append('..')
import AoCUtils
import itertools, functools
from itertools import product, accumulate
from functools import reduce
import numpy as np
import re

rawInput = AoCUtils.listLines(day="03", part="2")

inp_1 = [re.findall('mul\([0-9]*,[0-9]*\)|do\(\)|don\'t\(\)', line) for line in rawInput]
inp_1 = [item for i in inp_1 for item in i]

inp_2 = [item for l in inp_1 for item in re.findall('[0-9]*,[0-9]*|do\(\)|don\'t\(\)', l)]

inp_3 = []
state = True
for item in inp_2:
    if item[0].isdigit():
        if state:
            inp_3.append(int(item.split(',')[0]) * int(item.split(',')[1]))
    elif item == "do()":
        state = True
    elif item == "don't()":
        state = False

output = sum(inp_3)

print(output)