#
# @desc   : arquivo auxiliar contendo funcoes de apoio a execucao dos
#           programas
#


#
# @desc   : Compute the float ratio
#
# @params : a = first value
#           b = second value
#
# @ return : The ratio value in float representation
#
def ratio(a,b):
	return float(a) / float(b)

#
# @desc   : Build a Max Heap
#
# @params : instances = array de valores em ponto flutuante
#           n = size of array
#
# @ return : A Max Heap Structure
#
def build_max_heap(instances, n):
	for i in range(n / 2, 0, -1):
		heapify(instances, n, i - 1)
	return instances

#
# @desc   : Find Element in a Heap - Left / Right / Parent
#
# @params : instances = array de valores em ponto flutuante
#           i = position from
#           position = left / right / parent
#
# @ return : The index of element in instances structure
#
def search_element(instances, i, position='parent'):
	if position == 'parent':
		return i / 2
	if position == 'left':
		return 2 * i
	if position == 'right':
		return (2 * i) + 1

#
# @desc   : Update heap structure
#
# @params : instances = array de valores em ponto flutuante
#           n = number of itens in instances
#           i = position of element to update in array
#
# @ return : The Element at position i is greater than its childrens
#
def heapify(instances, n, i):
	if n == 1:
		return instances
	left  = search_element(instances, i, 'left')
	right = search_element(instances, i, 'right')
	if (left <= n) and ( ratio(instances[left][0],instances[left][1]) > ratio(instances[i][0],instances[i][1]) ):
		maior = left
	else:
		maior = i
	if (right <= n) and ( ratio(instances[right][0],instances[right][1]) > ratio(instances[maior][0],instances[maior][1]) ):
		maior = right

	if maior != i:
		tmp = instances[i]
		instances[i] = instances[maior]
		instances[maior] = tmp
		heapify(instances, n, maior)


#### TEST CASE ####
# a = [2,7,26,25,19,17,1,90,3,36]
# build_max_heap(a, 10)
### expected value ####
#[90,36,26,25,19,17,1,7,3,2]#
