# https://www.codingame.com/ide/puzzle/the-descent

# game loop
while True:
    mountain_h = [int(input()) for i in range(8)] # height of the mountains

    # The index of the mountain to fire on.
    print(mountain_h.index(max(mountain_h)))
