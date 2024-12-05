import sys
sys.path.append('..')
import AoCUtils
import itertools, functools
from itertools import product, accumulate
from functools import reduce
import numpy as np
import re
import math

rawInput = AoCUtils.listLines(day="05", part="1")
sp = rawInput.index('')
rules, seqs = rawInput[0:sp], rawInput[sp+1:]

rules = [ tuple(map(int, item.split('|'))) for item in rules ]
seqs = [ tuple(map(int, item.split(','))) for item in seqs ]

# key, val = page, pages that must be print before key
rules_map = {}
for pair in rules:
    if pair[1] not in rules_map:
        rules_map[pair[1]] = []
    rules_map[pair[1]].append(pair[0])

mids = []
for seq in seqs:
    mid = seq[math.floor(len(seq) / 2)]
    correct = True
    for i in range(len(seq)):
        for l in seq[i:]:
            if (seq[i] in rules_map) and (l in rules_map[seq[i]]):
                correct = False
                break
    if correct:
        mids.append(mid)

output = sum(mids)
print(output)

