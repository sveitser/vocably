#!/usr/bin/python2
#
# Utilities to calculate scores and fetch new words
#

import re, operator, random

# global reference dictionary
reference_wordlist = dict()

# global sorted wordlist
sorted_reference_wordlist = []

def percentile(): return 0.67
def words_in_language(): return len(reference_wordlist)
def wordlist_filename(): return "../data/corpusrank.txt"

class Word:
    """
    Word class
    """
    def __init__(self,rank,freq):
        self.rank = rank
        self.freq = freq

def create_reference_wordlist(fname):
    """
    d = create_dict(fname) create dictionary: d[word] = Word

    creates dict based on table of word occurences and normalizes it 
    
    rank: Word.rank
    frequency: Word.frequency

    fname is of the form:
    rank1 occurences1 word1
    rank2 occurences2 word2
    """
    def normalize():
        count = 0
        for i in d:
            count += d[i].freq
        for i in d:
            d[i].freq /= count

    d=dict()
    f = open(fname,'r')
    for line in f.readlines():
        data = line.split()
        try:
            d[data[2]] = Word(int(data[0]),float(data[1]));
        except:
            continue

    normalize()

    return d


def remove_quotes(string):
    """
    Remove all quotes from string
    """
    return re.sub(r'.*>.*', '', string)

def unique_words(string):
    """
    Returns list of unique (case insensitive) strings from a string.
    """
    string = remove_quotes(string)
    return list(set(re.findall("[a-z]+", string.lower())))

def filter_words(wordlist):
    """
    Remove words we don't have in our dictionary
    """
    return [word for word in wordlist if word in reference_wordlist]

def score_wordlist_percentile(wordlist):
    """
    Score user based on list of unique words in wordlist. Percentile approach.
    """
    d = reference_wordlist
    
    # sort words, reverse for performance
    sorted_words = sorted(filter_words(wordlist), \
        key = lambda x: d.get(x).rank, reverse=True)
    
    threshold_word = sorted_words[ int( (1 - percentile()) * len(sorted_words))]
    score = float( d[threshold_word].rank ) / words_in_language()
    
    return score

def score(wordlist):
    """
    Scores user based on wordlist.
    """
    return score_wordlist_percentile(wordlist)


def test_on_textfile(fname):
    """
    Loads text file and estimates number of words in vocabulary.
    """
    wl = filter_words( unique_words( open(fname, 'r').read()))
    return score(wl) * words_in_language()

def choose_words(userid):
    def get_word(target_word):
        r = rand * 0.1
    # query database for known words of user
    userwords = get_list(userid)

    # query database for user score
    userscore = get_score(userid)

    target = int(percentile() * userscore * words_in_language())
    target_word = userwords[target]
    nwords_to_send = 10
    

        


def initialize_module():
    global reference_wordlist
    global sorted_reference_wordlist
    
    reference_wordlist = create_reference_wordlist(wordlist_filename())
    sorted_reference_wordlist = sorted(reference_wordlist,
            key=lambda x: reference_wordlist.get(x).freq, reverse=True)

initialize_module()


