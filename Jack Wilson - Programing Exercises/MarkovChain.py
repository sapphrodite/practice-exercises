# Markov chain (Jack Wilson)
import numpy as np
import random
from collections import defaultdict

def MarkovSentenceGenerator(graph, sentenceAmount, firstWord=None):
  if sentenceAmount <= 0:
    return []
  else:
    firstWord = random.choice(list(graph.keys()))
    wordAmount = np.array(list(markovGraph[firstWord].values()),dtype=np.float64)
    wordAmount /= wordAmount.sum()
    choices = list(markovGraph[firstWord].keys())
    randomWord = np.random.choice(choices, None, p=wordAmount)
    return [randomWord] + MarkovSentenceGenerator(graph, sentenceAmount=sentenceAmount-1,firstWord=randomWord)

punctuation='''!()-[]{};:'"\,<>./?@#$%^&*_~1234567890'''
script=""
scriptFile=open("C:/Users/jw867/python_exercises/markovChain/markovTestData.txt","r",encoding="utf8")
scriptWithPunctuation=scriptFile.read()
for words in scriptWithPunctuation:
   if words not in punctuation:
      script=script+words
editiedScript=script.replace('"Bee Movie" - JS REVISIONS 8/13/07','')
scriptList=editiedScript.split()
scriptFile.close

lastWord = scriptList[0]
markovGraph = defaultdict(lambda: defaultdict(int))
for word in scriptList[1:]:
  word = word.lower()
  markovGraph[lastWord][word] += 1
  lastWord = word
sentenceWordNumber=int(input("How many words would you like in the sentence?: "))
randomSentence=MarkovSentenceGenerator(markovGraph,sentenceWordNumber)
for words in randomSentence:
   print(words,end=' ')