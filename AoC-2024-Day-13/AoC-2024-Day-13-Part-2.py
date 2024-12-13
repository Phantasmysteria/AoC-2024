import sys
sys.path.append('..')
import AoCUtils
import itertools, functools
from itertools import product, accumulate
from functools import reduce
import numpy as np
import re
import math

rawInput = AoCUtils.listLines(day="13", part="2")
inp_1 = [re.findall('\d+', item) for item in rawInput]
inp_2 = [ inp_1[i:i+3] for i in range(0, len(inp_1), 4)]
inp_3 = np.array(inp_2, dtype=int)

output = 0
for i in range(inp_3.shape[0]):
    x1, y1, x2, y2, xt, yt = inp_3[i].flatten()
    xt += 10000000000000
    yt += 10000000000000
    
    D = abs(x1*y2 - x2*y1)

    ma = abs((y2*xt - x2*yt)) // D if abs((y2*xt - x2*yt)) % D == 0 else -1
    if ma == -1:
        continue

    mb = abs((x1*yt - y1*xt)) // D if abs((x1*yt - y1*xt)) % D == 0 else -1 
    if mb == -1:
        continue

    output += 3*ma + mb

print(output)