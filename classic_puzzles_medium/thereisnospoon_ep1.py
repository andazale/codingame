# https://www.codingame.com/ide/puzzle/there-is-no-spoon-episode-1

import numpy as np

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
grid = [input() for i in range(height)]

def closest_bottom(row, column):
    while row < height:
        if grid[row][column] == '0':
            return column, row
        else: row = row + 1
    return -1, -1

def closest_right(row, column):
    while column < width:
        if grid[row][column] == '0':
            return column, row
        else: column = column + 1
    return -1, -1

for row in range(height):
    for column in range(width):
        if grid[row][column] == '0':
            x2, y2 = closest_right(row, column + 1)
            x3, y3 = closest_bottom(row + 1, column)
            print(column, row, x2, y2, x3, y3)
