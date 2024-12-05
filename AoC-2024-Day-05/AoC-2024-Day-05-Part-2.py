import sys
sys.path.append('..')
import AoCUtils
import itertools, functools
from itertools import product, accumulate
from functools import reduce
import numpy as np
import re
import math

rawInput = AoCUtils.listLines(day="05", part="2")
sp = rawInput.index('')
rules, seqs = rawInput[0:sp], rawInput[sp+1:]

rules = [ tuple(map(int, item.split('|'))) for item in rules ]
seqs = [ list(map(int, item.split(','))) for item in seqs ]

# key, val = page, pages that must be print before key
rules_map_bf = {}
for pair in rules:
    if pair[1] not in rules_map_bf:
        rules_map_bf[pair[1]] = []
    rules_map_bf[pair[1]].append(pair[0])

incorrects = []
for seq in seqs:
    mid = seq[math.floor(len(seq) / 2)]
    correct = True
    for i in range(len(seq)):
        for l in seq[i:]:
            if (seq[i] in rules_map_bf) and (l in rules_map_bf[seq[i]]):
                correct = False
                break
    if not correct:
        incorrects.append(seq)

sorted_seqs = []

for seq in incorrects:
    copy_seq = seq[:]
    modified = False
    i = 0
    while i < len(copy_seq):
        for j in range(i+1, len(copy_seq)):
            if (copy_seq[i] in rules_map_bf) and (copy_seq[j] in rules_map_bf[copy_seq[i]]):
                copy_seq[i], copy_seq[j] = copy_seq[j], copy_seq[i]
                modified = True
            if modified:
                break
        if not modified:
            i += 1
        modified = False
    sorted_seqs.append(copy_seq)

mids = [ s[math.floor(len(s) / 2)] for s in sorted_seqs ]
output = sum(mids)
print(output)

