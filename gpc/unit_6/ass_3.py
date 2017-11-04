
from collections import defaultdict


class Pmf(defaultdict):
    def __init__(self, prob_dict):
        defaultdict.__init__(self, int, prob_dict)
        if not self.is_a_probability():
            print "ERROR, NOT A PROBABILITY"

    def is_a_probability(self, tol = 0.001):
        total_p = reduce(lambda x, v: x + v, self.itervalues(), 0)
        return (abs(total_p - 1) < tol)

    def __add__(self, other):

        if type(other) == type(self):
            X1 = self
            X2 = other
            X3 = defaultdict(int)
            for x1 in X1:
                for x2 in X2:
                    X3[x1+x2] += X1[x1] * X2[x2]
            return Pmf(X3)

        if type(other) == int or type(other) == float:
            X = self
            X2 = {x + other : X[x] for x in X}
            return Pmf(X2)

    def __mul__(self, other):

        if type(other) == type(self):
            X1 = self
            X2 = other
            X3 = defaultdict(int)
            for x1 in X1:
                for x2 in X2:
                    X3[x1 * x2] += X1[x1] * X2[x2]
            return Pmf(X3)

        if type(other) == int or type(other) == float:
            X = self
            X2 = {x * other : X[x] for x in X}
            return Pmf(X2)


def sales_pmf(appt1, appt2, deluxe_sale, std_cost, deluxe_cost):
    '''INPUT:
    appt1: probability of making a sale at appointment one
    appt2: probability of making a sale at appointment two
    deluxe_sale: given a sale, probability of selling a deluxe model
    std_cost: cost of a standard model
    deluxe_cost: cost of a deluxe model

    OUTPUT:
    sales_pmf: dictionary showing probabilities of all possible sales totals
    '''
    sales=defaultdict(int)
    sales[0] = (appt1 - 1) * (appt2 -1)
    sales[std_cost] += (
                        appt1 * (1 - deluxe_sale) * (1 - appt2) +
                        appt2 * (1 - deluxe_sale) * (1 - appt1) )
    sales[deluxe_cost] += (
                        appt1 * deluxe_sale * (1 - appt2) +
                        appt2 * deluxe_sale * (1 - appt1) )
    sales[2 * std_cost] += appt1 * appt2 * (1 - deluxe_sale) ** 2
    sales[std_cost + deluxe_cost] += (
                        appt1 * (1 - deluxe_sale) * appt2 * deluxe_sale +
                        appt2 * (1 - deluxe_sale) * appt1 * deluxe_sale )
    sales[2 * deluxe_cost] += appt1 * appt2 * deluxe_sale ** 2
    return sales


def sales_pmf2(appt1, appt2, deluxe_sale, std_cost, deluxe_cost):
    s1 = Pmf({0: 1-appt1, std_cost: appt1*(1-deluxe_sale), deluxe_cost: appt1*deluxe_sale})
    s2 = Pmf({0: 1-appt2, std_cost: appt2*(1-deluxe_sale), deluxe_cost: appt2*deluxe_sale})
    s3 = s1 + s2
    return s3


import numpy as np
from scipy.stats import binom

def probability_rain(simulation_size=100000):
    '''
    choose the simulation_size

    returns
    -------
    probability that it will rain for at least two days in the next five days,
    knowing that the forecast says that in the next five days the chance of rain
    for each day is 25%
    '''
    tests= binom.rvs(5, 0.25, size = simulation_size)
    total = reduce(lambda t, x: t + (x >= 2), tests, 0)
    return float(total)/simulation_size

import numpy as np
from scipy.stats import geom

def probability_coin(p=0.8):
  '''
  INPUT:
  p: probability of tails on a single flip of the coin (default 0.8)

  returns
  -------
  a dictionary showing the probability of first seeing a head on the kth flip,
  for k in range 1 to 15,
  knowing that you have an unfair coin,
  with an p chance of getting tails.
  '''
  return {k: geom.pmf(k, p) for k in range(1, 16)}


if __name__ == '__main__':

    #print sales_pmf(0.3,0.6,0.5,500,1000)
    #print sales_pmf2(0.3,0.6,0.5,500,1000)
    #print probability_rain()
    print probability_coin()
