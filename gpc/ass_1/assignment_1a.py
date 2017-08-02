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
