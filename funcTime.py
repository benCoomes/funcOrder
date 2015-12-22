import itertools
import stats
"""
takes two parellel lists and uses the data in them to determine the 
function order that best fits the point pairs
"""

def data_order(n_vals, time_vals):
    if len(n_vals) != len(time_vals):
        print "Warning: parameters to data_order do not have the same length"


    linear_deviation = linear_fitness(n_vals, time_vals)
    quadradic_deviation = quadradic_fitness(n_vals, time_vals)

    # poor model for the moment
    #TODO: make more informative, accurate
    if linear_deviation < quadradic_deviation:
        order = 1
    else:
        order = 2

    return order

"""
current implementation plan:
divide each time_val by its corresponding n_val
store these in a list called ratios
find the standard deviation of the list?
use the standard deviation to determine fitness:
    low standard deviations will result from sets that contain values
    which are all close to one another
    the values stored in ratios should be close to one another if the 
    relationship between the n_vals and the time_vals is linear_fitness

potential problems:
    standard deviation can be thrown off easilly by outliers
        - maybe use median absolute deviation?

    if there are only a few large values in n_vals, then the constant term, b,
    in y = mx + b may cause signifigent differences in the values stored in 
    ratios

"""

def linear_fitness(n_vals, time_vals):
    ratios = []

    #note: itertools.izip(list1, list2) returns a tuple iterator
    #      it stops when the shorter of the two lists is exhausted
    for nval, timeval in itertools.izip(n_vals, time_vals):
        ratios.append(float(timeval) / nval)

    fitness = stats.standard_deviation(ratios)
    return fitness

def quadradic_fitness(n_vals, time_vals):
    ratios = []

    for nval, timeval in itertools.izip(n_vals, time_vals):
        ratios.append(float(timeval) / (nval * nval))

    fitness = stats.standard_deviation(ratios)
    return fitness
