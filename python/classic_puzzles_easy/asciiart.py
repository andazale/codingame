# https://www.codingame.com/ide/puzzle/ascii-art

import sys
import math
import numpy as np

l = int(input())
h = int(input())
t = input().lower()
rows = [input() for i in range(h)]

nums = [(ord(x) - 97) if x >= 'a' and x <= 'z' else 26 for x in t]

for x in rows:
    for i in range(len(nums)):
        print(x[l*nums[i] : l*(nums[i]+1)], end='\n' if i == len(nums)-1 else '')
