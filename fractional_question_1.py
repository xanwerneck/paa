# Save the information in a list structure
# Create a list to save the ratio
# Calculate the ration on each item in O(n)
# Order by ration value desc
# Use a MaxHeap to fill the Knapsack

#### References ####
# 1 - len(list) => https://wiki.python.org/moin/TimeComplexity
# 2 - Algoritmos - teoria e pratica - Cormen
# 3 - list.pop(0) => https://wiki.python.org/moin/TimeComplexity

# Include External Modules
import sys
sys.path.insert(0, 'utilities')

from helpers_list import *


def fractional_knap(instances, b_value):
	structure    = build_max_heap(instances, len(instances)) # O(n)
	total_value  = 0
	total_weight = 0
	sub_t_weight = 0
	while (total_weight < b_value) and (len(structure) > 0):
		root          = structure[0]
		total_weight += root[1]
		if total_weight < b_value:
			total_value  += root[0]
			structure.pop(0)
			if len(structure) > 0:
				heapify(structure, len(structure), 0) # O (log n)
		else:
			sub_t_weight = total_weight - root[1]


	# Take the fractional Last Element
	if (sub_t_weight < b_value) and (len(structure) > 0):
		root            = structure[0]
		diff            = (b_value - sub_t_weight)
		root_perc_value = root[0] * (float(diff) / float(root[1]))
		total_value    += root_perc_value


	print "The Max Value of Fraction Knapsack Problem is: %f" , total_value


#### TEST CASE ####
a = [(10,5),(4,4),(4,3),(2,1)]
fractional_knap(a, 10)