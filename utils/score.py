#
# Utilities to calculate scores and fetch new words
#

import re, random, enchant 
import words, database

# global reference dictionary
reference_wordlist = words.setup_reference_wordlist()

def percentile():
    return 0.8
def words_in_language():
    return len(reference_wordlist)

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
    sorted_words = sorted(filter_words(wordlist),
        key= lambda x: d.get(x).rank, reverse=True)

    threshold_word = sorted_words[int( (1 - percentile()) * len(sorted_words))]
    score = float(d[threshold_word].rank ) / words_in_language()

    return score


def score(data):
    """
    Scores based on list of words or one string.
    """
    if isinstance(data, type('')):
        return score_wordlist_percentile(filter_words(unique_words(data)))
    elif isinstance(data, type([])):
        return score_wordlist_percentile(data)
    else: 
        return None


def test_on_textfile(fname):
    """
    Loads text file and estimates number of words in vocabulary.
    """
    wl = filter_words(unique_words( open(fname, 'r').read()))
    return score(wl) * words_in_language()

def choose_words(email, nwords_to_send = 10):
    """
    Choose nwords_to_send words for user to learn. If less words are available
    only the available words will be sent.
    Words chosen are assumed to be learned by user and are added to the
    user vocabulary in db. User score in db is updated.
    """
    # query database for known words of user
    userwords = database.get_list(email)

    # create complete dict and remove known words
    unknown_words = reference_wordlist.copy()
    for w in userwords:
        unknown_words.pop(w,0)
 
    # convert unknown words dict to sorted list
    unknown_words = sorted(unknown_words,
            key=lambda x: unknown_words.get(x).freq, reverse=True)

    # at best we can send all the unknown words
    nwords_to_send = min(nwords_to_send, len(unknown_words))

    # query database for user score
    userscore = database.get_score(email)

    def add_word():
        target = int(percentile() * userscore * len(unknown_words))
        candidate = int(target * (1 + random.random() * (1 - percentile())))
        candidate = min(candidate, len(unknown_words) - 1)
        return unknown_words.pop(candidate)

    wordlist = [add_word() for i in range(nwords_to_send)]
  
    # new score and add words to db
    database.store_user_words(email, wordlist)
    newscore = score(wordlist + userwords)
    database.set_score(email, newscore)

    return wordlist

def score_user(email, text):
    """
    Score a new user based on text. User is assumed to be in database.
    """
    wordlist = filter_words(unique_words(text))
    userscore = score(wordlist)
    database.store_user_words(email, wordlist)
    database.set_score(email, userscore)
    print 'User %s knows %i words' % (email, userscore * words_in_language())
    return userscore

def get_score(email):
    return int(database.get_score(email) * words_in_language() )

if __name__ == "__main__":
    database.setup_db()
    text = """

           i don't speak english and this is a lot of junk
           e2tearkt[ rtt here warrs,t 1202f0Vsmi23;0arstm 
           blah blah >> go away
           hello mercury venus earth mars jupiter saturn uranus netpune
           """
    print "using input:", text
    print "removing quotes..."
    print remove_quotes(text)
    print "unique words:"
    print unique_words(text)
    print "scoring test user"
    print "score %f" % score_user("test@user.com",text)
    

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
