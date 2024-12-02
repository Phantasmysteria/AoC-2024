import sys
sys.path.append('..')
import AoCUtils
import itertools, functools
from itertools import product, accumulate
from functools import reduce
import numpy

rawInput = AoCUtils.listLines(day="02", part="1")

proc_1 = [list(map(int, x.split(" "))) for x in rawInput]
proc_2 = list(filter(lambda x: x == sorted(x) or x == sorted(x, reverse=True), proc_1))
proc_3 = []

for item in proc_2:
    item = sorted(item)
    proc_3.append([ True if ((item[j+1]-item[j]) > 0 and (item[j+1]-item[j]) < 4 )else False for j in range(len(item)-1) ])

output = sum([all(i) for i in proc_3])
print(output)