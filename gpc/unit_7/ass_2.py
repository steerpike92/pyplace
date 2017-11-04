import pickle
import numpy as np
import scipy.stats as scs

# Don't change this. This fixes the randomness in sampling
np.random.seed(seed=1234)


# This loads in the list of numbers you are going to deal with
def load_pickle(file_name):
    """INPUT:
    - file_name(STR) [The name of the file]

    OUTPUT:
    - population(NUMPY ARRAY) [A array of numbers for the exercise]
    """
    return pickle.load(open(file_name))


def draw_sample(population, n):
    """INPUT:
    - population(NUMPY ARRAY) [The array containing all the numbers]
    - n(INT) [The number of sample you wanna draw]

    OUTPUT:
    - sample(NUMPY ARRAY) [A array that contains a subset of the population]

    Hint: Use np.random.choice(). Google it. Google is your best friend
    """
    return np.random.choice(population, n)


def get_mean(lst):
    """INPUT:
    - lst(NUMPY ARRAY) [The array of numbers where we find the mean of]

    OUTPUT:
    - mean_value(FLOAT)

    Hint: Don't use np.mean().
    Then use np.mean(arr) to see if you got the same value
    """
    return float(lst.sum())/lst.size


def get_variance(lst, sample=True):
    """INPUT:
    - lst(NUMPY ARRAY) [Either the sample or the population]
    - sample(BOOL) [True if sample variance, False if population variance]

    OUTPUT:
    - lst_variance(FLOAT) [Sample or population variance depending]
    """
    # E = lambda arr: get_mean(arr)
    # Var = E(lst * lst) - E(lst)**2
    Var = lst.var()
    correction = 1
    if sample:
        correction = lst.size/(lst.size-1.0)
    Var *= correction
    return Var

def get_sem(sample):
    """INPUT:
    - sample(NUMPY ARRAY)

    OUTPUT:
    - sem(FLOAT) [Standard Error Mean]
    """
    return (get_variance(lst = sample, sample = True) / sample.size)**0.5


if __name__ == '__main__':
    population = load_pickle('../data/population.pkl')
    #print 'First 5 element of the population: ', population[:5]
    #print draw_sample(population, 10)
    #print get_mean(population)
    #print population.mean()
    #print get_variance(population, False)
    #print get_sem(population)
    s_1000 = draw_sample(population, 1000)
    s_100 = draw_sample(population, 100)
    sem_100 = get_sem(s_100)
    sem_1000= get_sem(s_1000)
    var_100 = get_variance(s_100)
    var_1000 = get_variance(s_1000)
    print var_100, var_1000
    print round(100*var_100/var_1000, 3)
