def get_mean(lst):
    """
    INPUT: list of ints/floats
    RETURNS: the mean value of the input list as a float

    """
    return sum(lst)/float(len(lst))


def get_median(lst):
    """
    INPUT: list of ints/floats
    RETURNS: the median value of the input list as a float

    """
    s_list = sorted(lst)
    n = len(lst)
    if n % 2 == 0:
        return (s_list[n/2-1]+s_list[n/2])/2.0
    else:
        return float(s_list[int(n/2)])

def get_mode(lst):
    """
    INPUT: list of ints/floats
    RETURNS: the modal value of the input list as a float

    """
    keys = set(lst)
    counts = {k: sum([1 for i in lst if i == k]) for k in keys}
    return float(max(counts, key = lambda i: counts[i]))


import numpy as np

def get_range(lst):
    """
    INPUT: list of ints/floats
    RETURNS: the range of the input list - the distance from the minimum value to the maximum value

    """
    lst.sort()
    return abs(lst[-1] - lst[0])


def get_IQR(lst):
    """
    INPUT: list of ints/floats
    RETURNS: the interquartile range of the input list - the distance from Q1 (25th percentile) to Q3 (75th percentile)

    hint: use [np.percentile](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.percentile.html)

    """
    return np.percentile(lst,75)-np.percentile(lst,25)

from itertools import ifilterfalse

def remove_outliers(lst):
    """
    INPUT: list of ints/floats
    RETURNS: two lists
              - a list of all data points that fall either 3 times the IQR above Q3 or 3 times the IQR below Q1
              - a list of all remaining points

    """
    Q1 = np.percentile(lst,25)
    Q3 = np.percentile(lst,75)

    IQR = Q3 - Q1
    lower_bound = Q1 - 1 * IQR
    upper_bound = Q3 + 1 * IQR
    print "Q1", Q1
    print "Q3", Q3
    print "IQR", IQR
    print "lower bound", lower_bound
    print "upper_bound", upper_bound
    is_outlier = lambda x: (x < lower_bound or x > upper_bound)

    outliers = filter(is_outlier, lst)
    inliers = list(ifilterfalse( is_outlier, lst))

    return outliers, inliers

if __name__ == "__main__":
    data = [0.4, 0.8, 10.7, 11.2, 13.5, 13.6, 14.2, 14.4, 15.0, 17.1, 20.6, 30.2, 31.2]
    # print get_mean(data)
    # print get_median(data)
    # print get_mode(data)
    #print get_range(data)
    print get_IQR(data)
    print remove_outliers(data)




#pad
