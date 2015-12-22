import funcTime
import stats

test_set1 = [2, 4, 4, 4, 5, 5, 7, 9.0]
test_set2 = [4, 16, 10, 13, 36, 25, 50, 90]

print "Mean:", stats.mean(test_set1)

print "Standard deviation:", stats.standard_deviation(test_set1)

print "Linear Fitness:", funcTime.linear_fitness(test_set1, test_set2)

print "Quadradic Fitness:", funcTime.quadradic_fitness(test_set1, test_set2)

print "data order:", funcTime.data_order(test_set1, test_set2)