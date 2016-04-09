#dependencies nltk, get using pip download nltk
#wordnet, get by running python then typing 
#import nltk
#nltk.download()
#after that select wordnet from the list and close that window
from nltk.corpus import wordnet as wn

def getrelatedlist(words):
  rel = set([])
  for(word in words):
    rel = rel.union(getrelated(word))
  return list(rel)

#might want to filter out specific words
#human, man, and woman return some offensive words
def getrelated(word):
  synsets = wn.synsets(word)
  rel = []
  for s in synsets:
    slist = ([s] + s.hypernyms() + s.hyponyms() +
             s.member_meronyms() + s.part_meronyms() + s.substance_meronyms() +
             s.member_holonyms() +  s.part_holonyms() + s.substance_holonyms() +
             s.entailments())
    rel = rel + s2n(slist)
  return set(rel)

#synset2name
def s2n(li):
  l = map(lambda x: x.lemma_names(), li)
  #return flattened list
  return [item for sublist in l for item in sublist]
  