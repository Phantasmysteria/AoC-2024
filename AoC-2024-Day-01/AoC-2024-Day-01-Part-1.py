import sys
sys.path.append('..')
import AoCUtils
import itertools, functools
from itertools import product, accumulate
from functools import reduce

rawInput = AoCUtils.listLines(day="01", part="1")

inp_1 = list(map(lambda x: tuple(x.split('   ')), rawInput))
inp_2 = reduce(lambda acc, next: (acc[0] + " " + next[0], acc[1] + " " + next[1]), inp_1)
inp_3 = list(map(lambda x: x.split(' '), inp_2))
inp_4 = list(map(lambda x: sorted(list(map(lambda y: int(y), x))),inp_3))
inp_5 = [ abs(inp_4[0][i] - inp_4[1][i]) for i in range(len(inp_4[0])) ]
output = reduce(lambda acc, next: acc + next, inp_5)

print(output)
