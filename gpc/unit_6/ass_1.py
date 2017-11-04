from collections import Counter
from math import factorial
import itertools


def count_strings(string):
    '''
    INPUT: a string
    OUTPUT: an integer

    returns the number of distinct strings that can be made from the characters inside the argument string

    use itertools.permutations

    You should be able to use the function like this:
    >>> my_string = 'ab'
    >>> count_strings(my_string)
    2

    '''
    counts = Counter(string)
    perms = factorial(len(string))
    for k in counts:
        perms /= factorial(counts[k])
    return perms


def make_fruit_salad(lst, k):
    '''
    return the list of possible combinations by taking k elements from lst

    use itertools.combinations

    You should be able to use the function like this:
    >>> my_fruits = ['pear', 'banana', 'apple']
    >>> make_fruit_salad(my_fruits, 2)
    [('pear', 'banana'), ('pear', 'apple'), ('banana', 'apple')]
    '''
    return len(itertools.combinations(lst, k))


if __name__ == '__main__':
    #print count_strings('better')



'''
5! = 120 ways for the cars to arrive, all equally probable
3!*2! = 12 ways for the lyfts to arrive first
2!*3! = 12 ways for the ubers to arrive first
'''
