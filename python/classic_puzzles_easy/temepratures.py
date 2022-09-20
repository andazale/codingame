# https://www.codingame.com/ide/puzzle/temperatures

import sys
import math
import numpy as np


n = int(input())  # the number of temperatures to analyse
t = np.array([])
for i in input().split():
    t = np.append(t, int(i))

if n != 0:
    result = 5526
    for i in t:
        if abs(i) < abs(result):
            result = int(i)
        elif abs(i) == abs(result) and i != result:
            result = abs(int(i))
else: result = 0
print(result)
