# PAA 2016.2
# Alexandre Werneck
# Gabriel de Quadros Ligneul

#### REFERENCES ####
# Sort complexity: http://svn.python.org/projects/python/trunk/Objects/listsort.txt

from math import ceil
import sys

# Itens
class Item(object):
    def __init__(self, index, value, weight, conflicts):
        self.index = index
        self.value = value
        self.weight = weight
        self.conflicts_list = conflicts
        self.conflicts = None

class SelectedItem(object):
    def __init__(self, item, frac):
        self.item = item
        self.frac = frac

# IO
def load_itens(input):
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
        conflicts = [int(c) - 1 for c in row[3:]]
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
    def comparison(x):
        if x.value == 0:
            return float('inf')
        else:
            return float(x.weight) / float(x.value)
    itens.sort(key = comparison)
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
    n = len(itens)
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
class BitSet:
    def __init__(self, size): # O(n)
        self.n_words = int(ceil(size / 32.0))
        self.data = [0 for _ in range(self.n_words)]

    def add(self, index): # O(1)
        self.data[index // 32] |= 1 << index % 32

    def union_empty(self, other): # O(n)
        assert self.n_words == other.n_words, 'invalid bitset comparison'
        for i in range(self.n_words):
            if self.data[i] & other.data[i] != 0:
                return False
        return True

def conflicts_knapsack(itens, W):
    # O(n^2)
    for i in itens:
        i.conflicts = BitSet(len(itens))

    # O(n + m)
    for i in itens:
        for c in i.conflicts_list:
            i.conflicts.add(c)
            itens[c].conflicts.add(i.index)

    # O(nlogn)
    def comparison(x):
        if x.value == 0:
            return float('inf')
        else:
            return float(x.weight) / float(x.value)
    itens.sort(key = comparison)

    # O(n^2)
    sack_set = BitSet(len(itens))
    sack_itens = []
    sack_weight = 0
    for i in itens:
        if sack_weight + i.weight <= W and i.conflicts.union_empty(sack_set):
            sack_set.add(i.index)
            sack_itens.append(SelectedItem(i, 1))
            sack_weight += i.weight
    return sack_itens

# Main
if __name__ == '__main__':
    assert len(sys.argv) == 3, 'invalid number of arguments'
    with open(sys.argv[1], 'r') as f:
        input = f.read()
    itens, W = load_itens(input)
    if sys.argv[2] == '1':
        result = fractional_knapsack(itens, W)
    elif sys.argv[2] == '2':
        result = integer_knapsack(itens, W)
    elif sys.argv[2] == '3':
        result = conflicts_knapsack(itens, W)
    else:
        assert false, 'invalid argument Q'
    print_result(result)

