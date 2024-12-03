import sys
sys.path.append('..')
import AoCUtils
import itertools, functools
from itertools import product, accumulate
from functools import reduce
import numpy as np
import re

rawInput = AoCUtils.listLines(day="03", part="1")

inp_1 = [item for line in rawInput for item in re.findall('mul\([0-9]*,[0-9]*\)', line) ]
inp_2 = [item for l in inp_1 for item in re.findall('[0-9]*,[0-9]*', l)]
inp_3 = [int(item.split(',')[0]) * int(item.split(',')[1]) for item in inp_2]
output = sum(inp_3)

print(output)