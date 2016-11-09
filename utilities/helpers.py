#
# @desc   : arquivo auxiliar contendo funcoes de apoio a execucao dos
#           programas
#

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
	print instances

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
	left  = search_element(instances, i, 'left')
	right = search_element(instances, i, 'right')
	if (left <= n) and (instances[left] > instances[i]):
		maior = left
	else:
		maior = i
	if (right <= n) and (instances[right] > instances[maior]):
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
