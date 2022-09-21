# https://www.codingame.com/ide/puzzle/defibrillators

import math

lon = float(input().replace(',', '.')) # longtitude in degrees
lat = float(input().replace(',', '.')) # latitude in degrees
n = int(input()) # number of defibrillators
defib = [input().split(';') for i in range(n)] # description of each defibrillator

distances = {}

for i in defib:
    i[4] = float(i[4].replace(',', '.'))
    i[5] = float(i[5].replace(',', '.'))
    x = (i[4] - lon) * math.cos((lat + i[5])/2)
    y = i[5] - lat
    d = math.sqrt(x**2 + y**2) * 6371
    distances[d] = i[1]

# the name of the defibrillator closest to the user's position
print(distances[min(distances)])
