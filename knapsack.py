# PUC-Rio
# PAA 2016.2
# Alexandre Werneck
# Gabriel de Quadros Ligneul

#### REFERENCES ####
# Sort complexity: http://svn.python.org/projects/python/trunk/Objects/listsort.txt

import sys

# Itens
class Item(object):
    def __init__(self, id, value, weight, conflicts):
        self.id = id
        self.value = value
        self.weight = weight
        self.conflicts = conflicts

class SelectedItem(object):
    def __init__(self, item, frac):
        self.item = item
        self.frac = frac

# IO
def load_itens(input):
    lines = input.splitlines()
    assert len(lines) > 2, 'empty input' 
    header = lines[0].split(' ')
    n_itens = int(header[0])
    W = int(header[1])
    itens = []
    for i in range(n_itens):
        row = lines[1 + i].split(' ')
        id = int(row[0])
        value = float(row[1])
        weight = float(row[2])
        conflicts = [int(i) for i in row[3:] if i != '']
        itens.append(Item(id, value, weight, conflicts))
    return itens, W

def print_result(result):
    W, profit = 0, 0
    for i in result:
        W += i.item.weight * i.frac
        profit += i.item.value * i.frac
    print('{} {} {}'.format(len(result), W, profit))
    for i in result:
        print('{} {}'.format(i.item.id, i.frac))

# Question 1
def fractional_knapsack(itens, W):
    def comparison(x):
        if x.value == 0:
            return float('inf')
        else:
            return x.weight / x.value
    itens.sort(key = comparison)
    sack_itens = []
    sack_weight = 0
    for i in itens:
        if sack_weight + i.weight <= W:
            frac = 1
        else:
            frac = float(W - sack_weight) / i.weight
        sack_itens.append(SelectedItem(i, frac))
        sack_weight += i.weight
        if sack_weight >= W:
            break
    return sack_itens

# Main
if __name__ == '__main__':
    assert len(sys.argv) == 3, 'invalid number of arguments'
    with open(sys.argv[1], 'r') as f:
        input = f.read()
    itens, W = load_itens(input)
    if sys.argv[2] == '1':
        result = fractional_knapsack(itens, W)
    else:
        assert false, 'invalid argument Q'
    print_result(result)

