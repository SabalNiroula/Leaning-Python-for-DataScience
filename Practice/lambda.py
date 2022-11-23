from functools import reduce

lst = [10, 309, 49, 43, 23, 45, 23]

lst1 = reduce(lambda x, y: x if x>y else y, lst )