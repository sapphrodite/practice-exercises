# Basic Markov Chain
import random
import numpy as np
from itertools import chain

"""Part A"""
dict1 = {}
dict2 = {}
dict3 = {}
total = 0
filebee = open("markovTestData.txt", encoding="utf8").read().split()

# Transitions
total = len(filebee)
for x, key, in enumerate(filebee):
    if total > (x + 1):
        word = filebee[x + 1]
        if key not in dict1:
            dict1[key] = [word]
        else:
            dict1[key].append(word)

# Probability
for word in dict1:
    if word in dict2:
        dict2[word] += 1
    else:
        dict2[word] = 1
total2 = sum(dict2.values())

probab = dict2[word] / total2
dict1.update(probab)
print(dict1)

# dictionary = dict.fromkeys(probab, dict1)
# print(dictionary)

"""Part B"""
# first_word = np.random.choice(total2)
# chain = first_word
# n_words = 30
# for i in range(n_words):
#     chain.append(np.random.choice(total2[chain[-1]]))
# ' '.join(chain)
