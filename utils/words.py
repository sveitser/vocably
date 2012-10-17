"""Utils for word list.

   The idea is to be able to combine arbirtarty frequensy lists to make things
   more interesting.

"""
import enchant, re, cPickle as pickle
from nltk.corpus import wordnet
en_check = enchant.Dict("en_GB").check

def wordlist_filename():
    return "data/en_filtered.txt"  
def wordlist_dumpfilename():
    return "data/reference_wordlist.dump"

def filters():
    """
    If any of these functions returns true, the word "is" English.
    """
    return [en_check, wordnet.synsets]

class Word:
    """
    Word class
    """
    def __init__(self, word, rank, freq):
        self.word = word
        self.rank = rank
        self.freq = freq

def is_english(word):
    return word.isalpha() and any([f(word) for f in filters()]) 

def setup_reference_wordlist():
    """
    Load reference wordlist from dump if available, create it from textfile
    otherwise.
    """
    try:
        d = pickle.load(open(wordlist_dumpfilename(), 'rb'))
        print "Loaded previously generated reference wordlist."
        return d
    except:
        print "Couldn't load reference wordlist."

    print "Creating reference wordlist from textfile. May take a while."
    d = create_wordlist_from_file(wordlist_filename())
    print "Dumping reference wordlist to file for next time."
    pickle.dump(d, open(wordlist_dumpfilename(), 'wb'), protocol=2)

    return d

def create_wordlist_from_file(fname):
    """
    Loads a list from file. Returns normalized {word:Word} dictionary.

    Column1: words
    Column2: some frequency measure in descending order
    """
    total = 0.0
    rank = 1
    d = {}

    l = load_wordlist(fname)

    for word, freq in l:
            d[word] = Word(word, rank, float(freq))
            rank += 1
            total += float(freq)
    
    # normalize
    for word in d:
        d[word].freq /= total

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
    fn = 'data/en.txt'
    fnf = 'data/en_filtered.txt'
    l = load_wordlist(fn)
    print "loaded"
    l = filter_wordlist(l)
    print "filtered"
    save_wordlist(fnf, l)
    print "saved"
    d = create_wordlist_from_file(fnf)
    print "wordlist created"
    print '"fuck" is the %i-th most used word' % d["fuck"].rank

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
