# https://www.codingame.com/ide/puzzle/horse-racing-duals

n = int(input()) # number of horses
pi = [int(input()) for i in range(n)] # horse strengths

# find minimum difference
pi = sorted(pi)
answer = 10**20

for i in range(n-1):
    if pi[i+1] - pi[i] < answer:
        answer = pi[i+1] - pi[i]

print(answer)
