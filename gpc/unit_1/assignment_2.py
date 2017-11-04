'''
                Generating a random text: working with functions

Fill in each of the 3 functions below. Complete the 'if __name__' block.

Run "python -m doctest assignment_2a.py" at the command line to test your work.
'''

import random
import string
from collections import Counter, defaultdict
import sys

class PrettyDefaultDict(defaultdict):
    __repr__ = dict.__repr__


class PrettyCounter(Counter):
    __repr__ = dict.__repr__


def process_words(f):
    p = string.punctuation
    words = []
    for line in f:
        new_words = line.split()
        words.extend(
            map(lambda word: word.lstrip(p).rstrip(p).lower(), new_words))
    return words


def word_counts(f):
    '''
    INPUT: file
    OUTPUT: dictionary
    Return a dictionary whose keys are all the words in the file (broken by
    whitespace). The value for each word is a dictionary containing each word
    that can follow the key and a count for the number of times it follows it.
    You should lowercase everything.
    Use strip and string.punctuation to strip the punctuation from the words.
    Example:
    >>> #example.txt is a file containing: "The cat chased the dog."
    >>> with open('../data/example.txt') as f:
    ...     word_counts(f)
    {'the': {'dog': 1, 'cat': 1}, 'chased': {'the': 1}, 'cat': {'chased': 1}}
    '''

    words = process_words(f)
    counts = PrettyDefaultDict(PrettyCounter)
    for i in range(0,len(words)-1):
        word, next_word = words[i], words[i+1]
        counts[word][next_word] += 1

    return counts

def unigrams(f):
    '''
    INPUT: file
    OUTPUT: dictionary

    Return a dictionary where the key is an empty tuple and the only value is
    the list of all words in the file, words should appear as many times as
    they occur in the document.

    You should lowercase everything.
    Use strip and string.punctuation to strip the punctuation from the words.

    Example:
    >>> with open('../data/example.txt') as f:
    ...     d = unigrams(f)
    >>> d[()]
    ['the', 'cat', 'chased', 'the', 'dog']
    '''
    words = process_words(f)
    dic={(): words}
    return dic

def bigrams(f):
    '''
    INPUT: file
    OUTPUT: dictionary

    Return a dictionary where the keys are tuples of a single word in
    the file and the value for each key is a list of words that were found
    directly following the key.

    You should lowercase everything.
    Use strip and string.punctuation to strip the punctuation from the words.

    Words should be included in the list the number of times they appear.

    Suggestions on how to handle first words: create an entry in the dictionary
    with a first key None.

    Example:
    >>> with open('../data/alice.txt') as f:
    ...     d = bigrams(f)
    >>> d[('among', )]
    ['the', 'those', 'them', 'the', 'the', 'the', 'the', 'the', 'the', 'mad', 'the', 'them']
    '''
    words = process_words(f)
    dic = PrettyDefaultDict(list)
    for i in range(0, len(words)-1):
        word, next_word = words[i], words[i+1]
        dic[(word,)].append(next_word)
    return dic

def trigrams(f):
    '''
    INPUT: file
    OUTPUT: dictionary

    Return a dictionary where the keys are tuples of two consecutive words in
    the file and the value for each key is a list of words that were found
    directly following the key.

    You should lowercase everything.
    Use strip and string.punctuation to strip the punctuation from the words.

    Words should be included in the list the number of times they appear.

    Suggestions on how to handle first words: create an entry in the dictionary
    with a first key (None, None), a second key (None, word1)

    Example:
    >>> with open('../data/alice.txt') as f:
    ...     d = trigrams(f)
    >>> d[('among', 'the')]
    ['people', 'party', 'trees', 'distant', 'leaves', 'trees', 'branches', 'bright']
    '''
    words = process_words(f)
    dic = PrettyDefaultDict(list)
    for i in range(0, len(words)-2):
        word1, word2, word3 = words[i], words[i + 1], words[i + 2]
        dic[(word1, word2)].append(word3)
    return dic


def make_random_story(f, n_gram=2, num_words=200):
    '''
    INPUT: file, integer, interger
    OUTPUT: string

    Call n_grams (unigrams, bigrams or trigrams for n_gram set at 1, 2 or 3) on
    file f and use the resulting dictionary to randomly generate text with
    num_words total words.

    Choose the next word by using random.choice to pick a word from the list
    of possibilities given the (n_gram - 1) previous words.

    Use join method to turn a list of words into a string.

    Example:
    >>> # Seed the random number generator for consistent results
    >>> random.seed('Is the looking-glass is half full or half-empty?')
    >>> # Generate a random story
    >>> with open('../data/alice.txt') as f:
    ...     story = make_random_story(f, 2, 10)
    ...     story
    stick, and tumbled head over heels in its sleep 'twinkle,
    >>> len(story.split())  # Verify story length is 10 words
    10
    '''
    n_gram_funcs={1: unigrams, 2: bigrams, 3: trigrams}
    dic = n_gram_funcs[n_gram](f)
    story_tuple = random.choice(dic.keys())
    for i in range(n_gram, num_words+1):
        key = story_tuple[i-n_gram:]
        choices = dic[key]
        story_tuple += (random.choice(choices),)
    story = ' '.join(story_tuple)
    return story



# This code will be run if you on the command line run: python assignment_2a.py
if __name__ == '__main__':
    # open the 'alice.txt' file, in the data directory
    # call the 'make_random_story' to print a 100 word long story based on bigrams
    filename, n_gram, num_words = sys.argv[1:]
    filepath= '../data/' + filename
    n_gram, num_words = int(n_gram), int(num_words)
    with open( filepath ) as f:
        random.seed('Is the looking-glass is half full or half-empty?')
        story = make_random_story(f, n_gram, num_words)
        print story
