def average_rows1(mat):
    '''
    Use list comprehension to take the average of each row in the matrix and
    return it as a list.

    Parameters
    ----------
    mat : {list} of {list} of numbers ({int or float})

    Returns
    -------
    list : {list} of {float}

    Example
    -------
    >>> average_rows1([[4, 5, 2, 8], [3, 9, 6, 7]])
    [4.75, 6.25]
    '''
    return [float(sum(row))/len(row) for row in mat]


def average_rows2(mat):
    '''
    INPUT: 2 dimensional list of integers (matrix)
    OUTPUT: list of floats

    Use map to take the average of each row in the matrix and
    return it as a list.

    Example:
    >>> average_rows1([[4, 5, 2, 8], [3, 9, 6, 7]])
    [4.75, 6.25]
    '''
    return list(map(lambda row: float(sum(row))/len(row), mat))


def sort_rows(mat):
    '''
    Use list comprehension to modify each row of the matrix to be sorted.
    Notice that the matrix is modified in place

    Parameters
    ----------
    mat : {list} of {list} of {int}

    Returns
    -------
    None

    Example
    -------
    >>> M = [[4, 5, 2, 8], [3, 9, 6, 7]]
    >>> sort_rows(M)
    >>> M
    [[2, 4, 5, 8], [3, 6, 7, 9]]
    '''
    [row.sort() for row in mat]


def word_lengths1(phrase):
    '''
    Use list comprehension to find the length of each word in the phrase
    (broken by spaces) and return the values in a list.

    Parameters
    ----------
    phrase : {str}

    Returns
    -------
    list : {list} of {int}

    Example
    -------
    >>> word_lengths1("Welcome to the Data Science Immersive Program!")
    [7, 2, 3, 4, 7, 9, 8]
    '''
    return [len(word) for word in phrase.split()]


def word_lengths2(phrase):
    '''
    Use map to find the length of each word in the phrase
    (broken by spaces) and return the values in a list.

    Parameters
    ----------
    phrase : {str}

    Returns
    -------
    list : {list} of {int}

    Example
    -------
    >>> word_lengths2("Welcome to the Data Science Immersive Program!")
    [7, 2, 3, 4, 7, 9, 8]
    '''
    return list(map(lambda w: len(w), phrase.split()))


def even_odd1(L):
    '''
    Use list comprehension to return a list of the same length with the strings
    "even" or "odd" depending on whether the element in L is even or odd.

    Parameters
    ----------
    L : {list} of {int}

    Returns
    -------
    list : {list} of {str}

    Example
    -------
    >>> even_odd1([6, 4, 1, 3, 8, 5])
    ['even', 'even', 'odd', 'odd', 'even', 'odd']
    '''
    return [['even', 'odd'][i % 2] for i in L]


def even_odd2(L):
    '''
    Use map to return a list of the same length with the strings
    "even" or "odd" depending on whether the element in L is even or odd.

    Parameters
    ----------
    L : {list} of {int}

    Returns
    -------
    list : {list} of {str}

    Example
    -------
    >>> even_odd2([6, 4, 1, 3, 8, 5])
    ['even', 'even', 'odd', 'odd', 'even', 'odd']
    '''
    return list(map(lambda i: ['even', 'odd'][i % 2], L))


def digits_to_num(digits):
    '''
    Use reduce to take a list of digits and return the number that they
    correspond to. Do not convert the integers to strings.

    Parameters
    ----------
    digits : {list} of {int}

    Returns
    -------
    int : {int}

    Example
    -------
    >>> digits_to_num([5, 0, 3, 8])
    5038
    '''
    return reduce(lambda x, y: x * 10 + y, digits)


def intersection_of_sets(list_of_sets):
    '''
    Use reduce to take the intersection of a list of sets.
    Hint: the & operator takes the intersection of two sets.

    Parameters
    ----------
    list_of_sets : {list} of {set}

    Returns
    -------
    set : intersection of all sets in list_of_sets

    Example
    -------
    >>> intersection_of_sets([{1, 2, 3}, {2, 3, 4}, {2, 5}])
    set([2])
    '''
    return reduce(lambda A, B: A & B, list_of_sets)


def shift_on_character(string, char):
    '''
    Find the first occurence of the character char and return the string with
    everything before char moved to the end of the string. If char doesn't
    appear, return the same string.

    Parameters
    ----------
    string : {str}
    char : {str}

    Returns
    -------
    str

    Example
    -------
    >>> shift_on_character("galvanize", "n")
    'nizegalva'
    '''
    #  if char in string:
    #     return string[string.index(char) :] + string[: string.index(char)]
    # else:
    #     return string
    return ''.join([string[string.index(char):], string[: string.index(char)]
                    if char in string else string])


def is_palindrome(string):
    '''
    Return whether the given string is the same forwards and backwards.

    Parameters
    ----------
    string : {str

    Returns
    -------
    bool

    Example
    -------
    >>> is_palindrome("rats live on no evil star")
    True

    >>> is_palindrome("the moon waxes poetic in sunlight")
    False
    '''
    return string == string[:: -1]


def alternate(L):
    '''
    Use list slicing to return a list containing all the odd indexed elements
    followed by all the even indexed elements.

    Parameters
    ----------
    L : {list}

    Returns
    -------
    list : {list}

    Example
    -------
    >>> alternate(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    ['b', 'd', 'f', 'a', 'c', 'e', 'g']
    '''
    return L[1:: 2] + L[0:: 2]


def shuffle(L):
    '''
    Return the result of a "perfect" shuffle. You may assume that L has even
    length. You should return the result of splitting L in half and alternating
    taking an element from each.

    Parameters
    ----------
    L : {list}

    Returns
    -------
    list : {list}

    Example
    -------
    >>> shuffle([1, 2, 3, 4, 5, 6])
    [1, 4, 2, 5, 3, 6]
    '''
    return reduce(lambda n, m: n + m, [list(tup) for tup in
                   zip(L[0: len(L) / 2], L[len(L) / 2:])])
    #return reduce(operator.concat, [list(t) for t in
    #                zip(L[0: len(L) / 2], L[len(L) / 2:])])


def count_match_index(L):
    '''
    Use enumerate and other skills to return the count of the number
    of items in the list whose value equals its index.

    Parameters
    ----------
    L : {list} of {int}

    Returns
    -------
    int : {int}

    Example
    -------
    >>> count_match_index([0, 2, 2, 3, 6, 5])
    4
    '''
    return sum([tup[0]==tup[1] for tup in enumerate(L)])


def invert_list(L):
    '''
    Use enumerate and other skills to return a dictionary which has
    the values of the list as keys and the index as the value. You may assume
    that a value will only appear once in the given list.

    Parameters
    ----------
    L : {list}

    Returns
    -------
    dict : keys are entries in L, vallues are the index

    Example
    -------
    >>> invert_list(['a', 'b', 'c', 'd'])
    {'a': 0, 'c': 2, 'b': 1, 'd': 3}
    '''
    return {v: i for i, v in enumerate(L)}


def concatenate(L1, L2, connector=""):
    '''
    L1 and L2 have the same length. Use zip and other skills from above to
    return a list of the same length where each value is the two strings from
    L1 and L2 concatenated together with connector between them.

    Parameters
    ----------
    L1 : {list} of {str}
    L2 : {list} of {str}
    connector : {str} (optional)

    Returns
    -------
    list : {list} of {str}

    Example
    -------
    >>> concatenate(["A", "B"], ["b", "b"])
    ['Ab', 'Bb']
    >>> concatenate(["San Francisco", "New York", "Las Vegas", "Los Angeles"], \
                    ["California", "New York", "Nevada", "California"], ", ")
    ['San Francisco, California', 'New York, New York', 'Las Vegas, Nevada', 'Los Angeles, California']
    '''
    return [s1+connector+s2 for s1, s2 in zip(L1, L2)]


def transpose(mat):
    '''
    Return the transpose of the matrix. You may assume that the matrix is not
    empty. You can do this using a double for loop in a list comprehension.
    There is also a solution using zip.

    Parameters
    ----------
    mat : {list} of {list} of {int}

    Returns
    -------
    list : {list} of {list} of {int}

    Example
    -------
    >>> M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> transpose(M)
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    '''
    return [[row[i] for row in mat] for i in range(0,len(mat[0]))]


def acronym(phrase):
    '''
    Given a phrase, return the associated acronym by breaking on spaces and
    concatenating the first letters of each word together capitalized.

    Parameters
    ----------
    phrase : {str}

    Returns
    -------
    str : {str}

    Example
    -------
    >>> acronym("data science immersive")
    'DSI'
    '''
    return ''.join([word[0] for word in phrase.upper().split()])


def sort_by_ratio(L):
    '''
    Sort the list L by the ratio of the elements in the 2-tuples.
    For example, (1, 3) < (2, 4) since 1/3 < 2/4.
    Use the key parameter in the sort method.

    Parameters
    ----------
    L : {list} of 2-tuples ({tuple}) of {int}

    Returns
    -------
    None

    Example
    -------
    >>> L = [(2, 4), (8, 5), (1, 3), (9, 4), (3, 5)]
    >>> sort_by_ratio(L)
    >>> L
    [(1, 3), (2, 4), (3, 5), (8, 5), (9, 4)]
    '''
    return L.sort(key = lambda pair: float(pair[0])/pair[1])


def string_combinations(alphabet, n):
    '''
    Use itertools.combinations to return all the combinations of letters in
    alphabet with length at most n.

    Parameters
    ----------
    alphabet : {str}
    n : {int}

    Returns
    -------
    list : {list} of {str}

    Example
    -------
    >>> string_combinations('abc', 2)
    ['a', 'b', 'c', 'ab', 'ac', 'bc']
    '''
    import itertools
    combos=[]
    for i in range(1, n+1):
        tuples =list(itertools.combinations(alphabet,i))
        combos.extend([''.join(tup) for tup in tuples])
    return combos


def permutations_in_dict(string, words):
    '''
    Use itertools.permutations to return all the permutations of the string
    and return only the ones which are members of set words.

    Parameters
    ----------
    string : {str}
    words : {set}

    Returns
    -------
    list : {list} of {str}

    Example
    -------
    >>> permutations_in_dict('act', {'cat', 'rat', 'dog', 'act'})
    ['act', 'cat']
    '''
    import itertools
    return sorted(set([''.join(perm) for perm in list(itertools.permutations(string))]) & words)
