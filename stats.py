import math

"""
returns the standard deviation for a set of values
the set is assumed to be the entire population and not just a 
sample, so bessel's correction is not used.
"""
def standard_deviation(population):
    pop_mean = mean(population)

    squared_deviations = []
    for item in population:
        squared_deviations.append(pow(item - pop_mean, 2))

    variance = mean(squared_deviations)
    return math.sqrt(variance)


"""
returns the mean of a set of numbers
"""
def mean(set):
    sum = 0.0
    for i in set:
        sum += i

    return sum / len(set)
