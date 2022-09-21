# https://www.codingame.com/ide/puzzle/winamax-battle

import sys
import math
from queue import Queue

def find_number(card):
    switch={
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }
    return switch.get(card[:-1], "Invalid unput")

n = int(input())  # the number of cards for player 1
cardp_1 = Queue(maxsize=0)
for i in range(n):
    cardp_1.put(find_number(input()))  # the n cards of player 1
m = int(input())  # the number of cards for player 2
cardp_2 = Queue(maxsize=0)
for i in range(m):
    cardp_2.put(find_number(input()))  # the m cards of player 2

draw = 0
# when war happens...
def war(p1folded, p2folded):
    # folding down the first three cards + last one to compare
    try:
        for i in range(4):
            p1folded.append(cardp_1.get_nowait())
            p2folded.append(cardp_2.get_nowait())
        if p1folded[-1] > p2folded[-1]:
            for j in p1folded:
                cardp_1.put(j)
            for m in p2folded:
                cardp_1.put(m)
        elif p1folded[-1] < p2folded[-1]:
            for j in p1folded:
                cardp_2.put(j)
            for m in p2folded:
                cardp_2.put(m)
        else: 
            war(p1folded, p2folded)
    except:
        print("Queue was empty", file=sys.stderr, flush=True)
        print('PAT')
        sys.exit()

rounds = 0
while not cardp_1.empty() and not cardp_2.empty():
    p1card = cardp_1.get_nowait()
    p2card = cardp_2.get_nowait()
    if p1card > p2card:
        cardp_1.put(p1card)
        cardp_1.put(p2card)
    elif p1card < p2card:
        cardp_2.put(p1card)
        cardp_2.put(p2card)
    else:
        war([p1card], [p2card])

    # counting the number of rounds needed for a win
    rounds = rounds +1

    # check if someone won and who
    if cardp_1.empty() and not draw:
        print(2, rounds)
    elif cardp_2.empty() and not draw:
        print(1, rounds)
