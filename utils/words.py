"""Utils for word list.

   The idea is to be able to combine arbirtarty frequensy lists to make things
   more interesting.

"""
from nltk.corpus import wordnet
import enchant, re


def filters():
    """
    If any of these functions returns true, the word "is" English.
    """
    return [enchant.Dict("en_GB").check, wordnet.synsets]


def is_english(word):
    return any([f(word) for f in filters()]) and word.isalpha()

def create_wordlist_csv(fname):
    """
    Loads a list from file. Returns normalized {word:freq} dictionary.

    Column1: words
    Column2: some frequency measure
    """
    f = open(fname, 'r')
    d = {}
    total = 0.0

    for line in f.readlines():
        word, freq = line.split()
        if is_english(word):
            d[word] = float(freq)
            total += float(freq)
    
    f.close()

    for word in d:
        d[word] /= total

    return d

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
