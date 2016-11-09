#### QUESTION 1 ####
#
# @desc : Resolve the Fractional KnapSack Problem
#

#### References ####
# 1 - len(list) => https://wiki.python.org/moin/TimeComplexity
#     time complexity = O(1)
# 2 - Algoritmos - teoria e pratica - Cormen
#     Cap. 6 - Heap Sort
# 3 - list.pop(0) => https://wiki.python.org/moin/TimeComplexity
#     time complexity = O(1)
# 4 - Problem definitions
#     http://www.geeksforgeeks.org/fractional-knapsack-problem/
# 5 - Python structures
#     https://docs.python.org/2/tutorial/datastructures.html

# Include External Modules
import sys
sys.path.insert(0, 'utilities')

from helpers_list import *

#
# @desc   : Fraction KnapSack Problem Algorithm
#
# @params : instances = lista de tuplas (a,b)
#           b_weight  = max weight of knapsack
#
# @ return : The Max Value
#
def fractional_knap(instances, b_weight):
	# Build a Max Heap
	structure    = build_max_heap(instances, len(instances)) # O(n)

	# Constant Values
	total_value  = 0
	total_weight = 0
	sub_t_weight = 0
	
	# First Step fill the knapsack with max integer values 
	# ordered by Heap Structure
	while (total_weight < b_weight) and (len(structure) > 0):
		root          = structure[0]
		total_weight += root[1]
		if total_weight < b_weight:
			total_value  += root[0]
			structure.pop(0)
			if len(structure) > 0:
				heapify(structure, len(structure), 0) # O (log n)
		else:
			sub_t_weight = total_weight - root[1]


	# Take the fractional Last Element
	if (sub_t_weight < b_weight) and (len(structure) > 0):
		root            = structure[0]
		diff            = (b_weight - sub_t_weight)
		root_perc_value = root[0] * (float(diff) / float(root[1]))
		total_value    += root_perc_value


	print "The Max Value of Fraction Knapsack Problem is: %f" , total_value


#### TEST CASE ####
a = [(10,5),(4,4),(4,3),(2,1)]
fractional_knap(a, 10)