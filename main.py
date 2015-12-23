import funcTime
import stats
import lin_func
import timeit
import random
import matplotlib.pyplot as plt
"""
times = []
nvals = []
for num in range(10000, 200000, 10000):
    func_string = "lin_func.linear_function(" + str(num) + ")"
    print func_string
    t = timeit.Timer(func_string, "from __main__ import lin_func")
    nvals.append(num)
    times.append(t.timeit(20))

"""

nvals = range(1, 100000, 1000)
times = []

coef = [0, 0, 1, 1]
for value in nvals:
    value = float(value)
    times.append(coef[0] * pow(value, 3) + coef[1] * pow(value, 2) + 
                 coef[2] * pow(value, 1) + coef[3] * pow(value, 0))

order = funcTime.data_order(nvals, times, True)

print "order: %d" % (order)

#plt.plot(nvals, times, 'ro')
#plt.axis([0, 20000, 0, 0.5])
#plt.show()