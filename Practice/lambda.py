from functools import reduce

lst = [132, 309, 49, 44, 23, 45, 23]

lst1 = reduce(lambda x, y: x if (x%2==0) else y, lst )

print(lst1)