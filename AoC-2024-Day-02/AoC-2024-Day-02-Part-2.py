import sys
sys.path.append('..')
import AoCUtils
import itertools, functools
from itertools import product, accumulate
from functools import reduce
import numpy

rawInput = AoCUtils.listLines(day="02", part="2")

proc_1 = [list(map(int, x.split(" "))) for x in rawInput]
proc_2 = []

for item in proc_1:
    checks = [ [item[j] for j in range(len(item)) if j != i] for i in range(len(item)) ]
    checks = list(filter(lambda x: x == sorted(x) or x == sorted(x, reverse=True), checks))
    checks = [sorted(x) for x in checks]
    item_to_add = [10000]
    for check in checks:
        dec = [ 0 if ((check[j+1]-check[j]) > 0 and (check[j+1]-check[j]) < 4 ) else 1 for j in range(len(check)-1) ]
        if sum(dec) < sum(item_to_add):
            item_to_add = dec
    proc_2.append(item_to_add)
    
output = sum([not any(i) for i in proc_2])

print(output)