# PAA 2016.2
# Alexandre Werneck
# Gabriel de Quadros Ligneul

#### REFERENCES ####
# Sort complexity: http://svn.python.org/projects/python/trunk/Objects/listsort.txt

from math import ceil
import sys

# Configuration for question 3
# Prints the used heuristic
PRINT_HEURISTIC = False

# Used heuristics and its namaes
HEURISTICS = [
    lambda i, itens: i.ratio,
    lambda i, itens: 1.0 / i.value if i.value > 0 else float('inf'),
    lambda i, itens: sum(itens[c].value for c in i.conflicts),
    lambda i, itens: 1 / sum(itens[c].ratio for c in i.conflicts),
]
HNAMES = [
    'ratio',
    '1 / value',
    'sum of values',
    '1 / sum of ratios',
]

# Itens
class Item(object):
    def __init__(self, index, value, weight, conflicts):
        self.index = index
        self.value = value
        self.weight = weight
        self.conflicts = conflicts
        if self.value == 0:
            self.ratio = float('inf')
        else:
            self.ratio = float(self.weight) / float(self.value)

class SelectedItem(object):
    def __init__(self, item, frac):
        self.item = item
        self.frac = frac

# IO
def load_itens(input, readconflicts):
    lines = input.splitlines()
    assert len(lines) > 2, 'empty input' 
    header = lines[0].split()
    n_itens = int(header[0])
    W = int(header[1])
    itens = []
    for i in range(n_itens):
        row = lines[1 + i].split()
        assert int(row[0]) == i + 1, 'invalid index {}'.format(id)
        value = int(row[1])
        weight = int(row[2])
        if readconflicts:
            conflicts = [int(c) - 1 for c in row[3:]]
        else:
            conflicts = []
        itens.append(Item(i, value, weight, conflicts))
    return itens, W

def print_result(result):
    result.sort(key=lambda i: i.item.index)
    W, profit = 0, 0
    for i in result:
        W += i.item.weight * i.frac
        profit += i.item.value * i.frac
    print('{} {} {}'.format(len(result), W, profit))
    for i in result:
        print('{} {}'.format(i.item.index + 1, i.frac))

# Question 1
def fractional_knapsack(itens, W):
    itens.sort(key = lambda i: i.ratio)
    sack_itens = []
    sack_weight = 0
    for i in itens:
        if sack_weight + i.weight <= W:
            frac = 1
        else:
            frac = float(W - sack_weight) / float(i.weight)
        sack_itens.append(SelectedItem(i, frac))
        sack_weight += i.weight
        if sack_weight >= W:
            break
    return sack_itens

# Question 2
def integer_knapsack(itens, W):
    n = len(itens) # O(1)
    sack_value = [[0 for y in range(W + 1)] for x in range(n + 1)]
    sack_itens = [[False for y in range(W + 1)] for x in range(n + 1)]
    for i in range(1, n + 1): # O(nW)
        for w in range(W + 1):
            item_w = itens[i - 1].weight
            item_v = itens[i - 1].value
            sack_with_last_item = sack_value[i - 1][w]
            if item_w > w:
                sack_value[i][w] = sack_with_last_item
            else:
                sack_with_this_item = sack_value[i - 1][w - item_w] + item_v
                if sack_with_this_item > sack_with_last_item:
                    sack_value[i][w] = sack_with_this_item
                    sack_itens[i][w] = True
                else:
                    sack_value[i][w] = sack_with_last_item
    selected_itens = []
    curr_w = W
    for i in reversed(range(1, n + 1)): # O(n)
        item = itens[i - 1]
        if sack_itens[i][curr_w]:
            curr_w -= item.weight
            selected_itens.append(SelectedItem(item, 1))
    return selected_itens

# Question 3
def conflicts_knapsack_with_heuristic(itens, W, H):
    # Compute heuristic O(nlogn + n + m) => O(nlogn + m)
    itensh = itens[:]
    for i in itensh:
        i.heuristic = H(i, itens)
    itensh.sort(key = lambda i: i.heuristic)

    # O(n + m)
    hasconflict = [False for i in itens]
    sack_itens, sack_weight, sack_value = [], 0, 0
    for i in itensh:
        if not hasconflict[i.index] and sack_weight + i.weight <= W:
            sack_itens.append(SelectedItem(i, 1))
            sack_weight += i.weight
            sack_value += i.value
            for c in i.conflicts:
                hasconflict[c] = True
    return sack_itens, sack_value

def conflicts_knapsack(itens, W):
    # fix conflicts O(n + m)
    for i in itens:
        for c in i.conflicts:
            if c > i.index:
                itens[c].conflicts.append(i.index)
    best_sack, best_value, best_heuristic = None, 0, None
    for heuristic, hname in zip(HEURISTICS, HNAMES):
        sack, value = conflicts_knapsack_with_heuristic(itens, W, heuristic)
        if value > best_value:
            best_sack, best_value, best_heuristic = sack, value, hname
    if PRINT_HEURISTIC:
        print('Used heuristic: {}'.format(best_heuristic))
    return best_sack

# Main
if __name__ == '__main__':
    assert len(sys.argv) == 3, 'invalid number of arguments'
    with open(sys.argv[1], 'r') as f:
        input = f.read()
    if sys.argv[2] == '1':
        result = fractional_knapsack(*load_itens(input, False))
    elif sys.argv[2] == '2':
        result = integer_knapsack(*load_itens(input, False))
    elif sys.argv[2] == '3':
        result = conflicts_knapsack(*load_itens(input, True))
    else:
        assert false, 'invalid argument Q'
    print_result(result)

