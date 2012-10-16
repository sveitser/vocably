"""Utils for word list.

   The idea is to be able to combine arbirtarty frequensy lists to make things
   more interesting.

"""
from nltk.corpus import wordnet
import enchant, re
en_check = enchant.Dict("en_GB").check


def filters():
    """
    If any of these functions returns true, the word "is" English.
    """
    return [en_check, wordnet.synsets]


def is_english(word):
    return word.isalpha() and any([f(word) for f in filters()]) 

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

def load_wordlist(fname):
    with open(fname, 'r') as f:
        return [line.split() for line in f.readlines()]

def save_wordlist(fname,l):
    with open(fname, 'w') as f:
        for word, freq in l:
            f.write(word + ' ' + str(freq) + '\n')

def filter_wordlist(l):
    k = []
    for word, freq in l:
        if is_english(word):
            k.append([word, freq])
    return k
#    return [[word,freq] for word, freq in l if is_english(word)]


if __name__ == "__main__":
    l = load_wordlist('data/en.txt')
    print "loaded"
    l = filter_wordlist(l)
    print "filtered"
    save_wordlist('data/en_filtered.txt', l)


# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
