
class Item(object):
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def to_string(self):
        return 'v: {} - w: {}'.format(self.value, self.weight)

class SelectedItem(object):
    def __init__(self, item, frac):
        self.item = item
        self.frac = frac

    def to_string(self):
        return self.item.to_string() + ' % {}'.format(self.frac)

def knapsack(itens, B):
    itens.sort(key = lambda x: float(x.weight) / x.value)
    sack_itens = []
    sack_weight = 0
    for i in itens:
        if sack_weight + i.weight <= B:
            frac = 1
        else:
            frac = float(B - sack_weight) / i.weight
        sack_itens.append(SelectedItem(i, frac))
        sack_weight += i.weight
        if sack_weight >= B:
            break
    return sack_itens

def print_itens(itens):
    for i in itens:
        print(i.to_string())

def do_test(itens, G):
    print('itens')
    print_itens(itens)
    print('sack')
    print_itens(knapsack(itens, G))

do_test([Item(10, 5), Item(4, 4), Item(4, 3), Item(2, 1)], 10)

