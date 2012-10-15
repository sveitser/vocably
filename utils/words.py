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

def filter_dictionary(function, dictionary):
    for w in dictionary:
        if not function(w):
            dictionary.pop(w)

    return dictionary



#f = open('data/en.txt','r')
#of = open('data/en_pyenchant_or_nltk_only.txt','w')
#en_dict = enchant.Dict("en_GB")
#rank = 1
#for line in f.readlines():
#    data = line.split()
#    try:
#        word = data[0]
#        if word.isalpha() and (en_dict.check(word) or wordnet.synsets(word)):
#            of.write(' '.join([str(rank), data[1], data[0]]) + '\n')
#            rank += 1
#    except:
#        pass
#
#
#print '%i words written' % rank 
#of.close()
#f.close()
