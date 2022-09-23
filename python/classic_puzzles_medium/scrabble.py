# https://www.codingame.com/ide/puzzle/scrabble

import sys
from itertools import permutations

values = {
    'a' : 1, 'b' : 3, 'c' : 3, 'd' : 2, 'e' : 1, 'f' : 4, 'g' : 2, 'h' : 4, 'i' : 1, 'j' : 8,
    'k' : 5,  'l' : 1, 'm' : 3, 'n' : 1, 'o' : 1, 'p' : 3, 'r' : 1, 's' : 1, 't' : 1, 'u' : 1,
    'v' : 4, 'w' : 4, 'y' : 4, 'x' : 8, 'q' : 10, 'z' : 10
}

n = int(input()) # number of words
w = [input() for i in range(n)] # words in dictionary
letters = input() # the available letters

possible_words =[list(permutations(letters, i)) for i in range(8)] # finding permutations of all lengths
possible_words = [item for sub_list in possible_words for item in sub_list] # flatten into 1d
possible_words = [''.join(item) for item in possible_words] # from ntuples to string
possible_words = [i for i in w if i in possible_words] # keeping those permutations that match the dictionary values

# find point value for each word
def assign_points(word_list):
    word_scores = {}
    for word in word_list:
        score = 0
        for i in word:
            score += values[i]
        word_scores[word] = score
    return word_scores

word_scores = assign_points(possible_words)

print(max(word_scores, key= lambda x: word_scores[x]))
